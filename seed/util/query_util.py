"""
__Seed builder__
  (Read_only) Query util
"""

import re

from django.db.models import Q

def multi_q(query):
    """
    | Return a Q Object base on a multilevel query
    | Example [{key_1: 1, key_2: 2}, {key_3: 3}] returns Q(OR(AND(key_1=1, key_2=2), key_3=3)

    :param query: query object
    :return: Q object
    """
    if isinstance(query, dict):  # Single query (ands)
        return Q(**query)
    else:  # Multiple queries (or, ands)
        res = Q()
        for sub in query:
            res |= multi_q(sub)
        return res

def sql_alike_q(query):
    """
    | Return a Q Object base on an SQL alike query
    | Example \"(key_1=1 AND key_2=2) OR (key_3=3)\" returns Q(OR(AND(key_1=1, key_2=2), key_3=3)

    :param query: SQL alike query
    :return: Q object
    """
    hsh = dict()
    stack = [0]
    hsh_idx = 0
    overflow = 0
    str_vals = dict()
    query, str_vals = get_str_vals(query, str_vals)
    while query.find('(') != -1 and overflow < 100:
        idx_ini = query[stack[-1] + 1: len(query)].find('(') + stack[-1] + 1
        idx_end = query[stack[-1] + 1: len(query)].find(')') + stack[-1] + 1
        if idx_ini < idx_end and query[stack[-1] + 1: len(query)].find('(') != -1:
            stack.append(idx_ini)
        else:
            sub_con = query[stack[-1]: idx_end + 1]
            sub_query = _get_query(sub_con[1: len(sub_con) - 1], hsh, str_vals)
            sub_name = 'Q[' + str(hsh_idx) + ']'
            query = query.replace(sub_con, sub_name, 1)
            hsh[sub_name] = sub_query
            hsh_idx += 1
            stack.pop(-1)
        overflow += 1
    res = _get_query(query, hsh, str_vals)
    return res

def get_str_vals(query, str_vals):
    def get_next_limiter_pos():
        lim1_pos = query.find("\"") if query.find("\"") != -1 else 1e10
        lim2_pos = query.find("\'") if query.find("\'") != -1 else 1e10
        lim3_pos = query.find("`") if query.find("`") != -1 else 1e10
        next_pos = min(lim1_pos, lim2_pos, lim3_pos)
        if next_pos == 1e10:
            return -1
        return next_pos

    query = query.replace("\\\"", "|#{QUOTE}#|")
    query = query.replace("\\\'", "|#{APOS}#|")
    query = query.replace("\\`", "|#{QUOTE_B}#|")

    iteration = 0
    while get_next_limiter_pos() != -1 and iteration < 1000:
        idx_ini = get_next_limiter_pos()
        limiter = query[idx_ini]
        idx_end = idx_ini + query[idx_ini + 1:].find(limiter) + 1
        raw_str_val = query[idx_ini:idx_end + 1]
        str_vals_idx = len(str_vals)
        str_id = "|#{}#|".format(str_vals_idx)
        str_vals[str_id] = raw_str_val[1:-1]
        query = query.replace(raw_str_val, str_id, 1)
        iteration += 1
    return query, str_vals

def _snake_case(name):
    s_1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s_1).lower()

def _is_float(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

def _get_query(data, hsh, str_vals):
    res = Q()
    queries = [i.strip() for i in data.split(' OR ')]
    for query in queries:
        filters = [i.strip() for i in query.split(' AND ')]
        values = []
        for flt in filters:
            if flt.startswith('Q['):
                values.append(_get_sub_query(flt, hsh))
            else:
                val_s = {}
                opt = _get_opt(flt)
                ele = flt.split(opt[0])
                if len(ele) > 1:
                    val_l = _get_val(ele, str_vals)
                    val_k = _snake_case(ele[0].strip()).replace(".", "__")
                    if opt[0] == '=':
                        val_s[val_k] = val_l
                    else:
                        val_s[val_k + '__' + opt[1]] = val_l
                    q_s = Q(**val_s)
                    values.append(q_s)
        res |= Q(*values)
    return res

def _get_opt(flt):
    opt = ('=', '')
    if '>=' in flt:
        opt = ('>=', 'gte')
    elif '<=' in flt:
        opt = ('<=', 'lte')
    elif '<>' in flt:
        opt = ('<>', 'ne')
    elif '>' in flt:
        opt = ('>', 'gt')
    elif '<' in flt:
        opt = ('<', 'lt')
    elif 'ILIKE' in flt:
        opt = ('ILIKE', 'icontains')
    elif 'LIKE' in flt:
        opt = ('LIKE', 'contains')
    return opt

def _get_val(ele, str_vals):
    val_l = ele[1].strip()
    if val_l in str_vals:
        val_l = str_vals[val_l]
        val_l = val_l.replace("|#{QUOTE}#|", "\"")
        val_l = val_l.replace("|#{APOS}#|", "\'")
        val_l = val_l.replace("|#{QUOTE_B}#|", "`")
    elif ele[1].isdigit():
        val_l = int(ele[1])
    elif _is_float(ele[1]):
        val_l = float(ele[1])
    elif ele[1].strip().upper() == 'TRUE':
        val_l = True
    elif ele[1].strip().upper() == 'FALSE':
        val_l = False
    return val_l

def _get_sub_query(sub_content, hsh):
    idx_ini = sub_content.find('[')
    idx_end = sub_content.find(']')
    idx = sub_content[idx_ini + 1: idx_end]
    return hsh['Q[' + str(idx) + ']']