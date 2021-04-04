"""
__Seed builder__v0.2.0
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
    while query.find('(') != -1 and overflow < 100:
        idx_ini = query[stack[-1] + 1: len(query)].find('(') + stack[-1] + 1
        idx_end = query[stack[-1] + 1: len(query)].find(')') + stack[-1] + 1
        if idx_ini < idx_end and query[stack[-1] + 1: len(query)].find('(') != -1:
            stack.append(idx_ini)
        else:
            sub_con = query[stack[-1]: idx_end + 1]
            sub_query = _get_query(sub_con[1: len(sub_con) - 1], hsh)
            sub_name = 'Q[' + str(hsh_idx) + ']'
            query = query.replace(sub_con, sub_name, 1)
            hsh[sub_name] = sub_query
            hsh_idx += 1
            stack.pop(-1)
        overflow += 1
    res = _get_query(query, hsh)
    return res


def _snake_case(name):
    s_1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s_1).lower()


def _is_float(val):
    try:
        float(val)
        return True
    except ValueError:
        return False


def _get_query(data, hsh):
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
                    val_l = _get_value(ele)
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
    elif '>' in flt:
        opt = ('>', 'gt')
    elif '<' in flt:
        opt = ('<', 'lt')
    elif 'ILIKE' in flt:
        opt = ('ILIKE', 'icontains')
    elif 'LIKE' in flt:
        opt = ('LIKE', 'contains')
    return opt

def _get_value(ele):
    val_l = ele[1].strip()
    if ele[1].startswith('"') and ele[1].endswith('"') or \
            ele[1].startswith('\'') and ele[1].endswith('\''):
        val_l = str(ele[1][1:-1])
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