"""
__Seed builder__v0.2.0
  (Read_only) Builder util
"""
import re

from django.db.models import Q


def multi_Q(qs):
    if type(qs) is dict:  # Single query (ands)
        return Q(**qs)
    else:  # Multiple queries (or, ands)
        res = Q()
        for q in qs:
            res |= multi_Q(q)
        return res


def str_Q(query):
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
            sub_query = get_query(sub_con[1: len(sub_con) - 1], hsh)
            sub_name = 'Q[' + str(hsh_idx) + ']'
            query = query.replace(sub_con, sub_name, 1)
            hsh[sub_name] = sub_query
            hsh_idx += 1
            stack.pop(-1)
        overflow += 1
    res = get_query(query, hsh)
    return res


def snake_case(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def is_float(val):
    try:
        float(val)
        return True
    except ValueError:
        return False


def get_query(data, hsh):
    res = Q()
    queries = [i.strip() for i in data.split(' OR ')]
    for q in queries:
        filters = [i.strip() for i in q.split(' AND ')]
        values = []
        for f in filters:
            if f.startswith('Q['):
                values.append(get_sub_query(f, hsh))
            else:
                val_s = {}
                opt = ('=', '')
                if '>=' in f:
                    opt = ('>=', 'gte')
                elif '<=' in f:
                    opt = ('<=', 'lte')
                elif '>' in f:
                    opt = ('>', 'gt')
                elif '<' in f:
                    opt = ('<', 'lt')
                elif 'ILIKE' in f:
                    opt = ('ILIKE', 'icontains')
                elif 'LIKE' in f:
                    opt = ('LIKE', 'contains')

                ele = f.split(opt[0])
                if len(ele) > 1:
                    val_l = ele[1].strip()
                    if ele[1].startswith('"') and ele[1].endswith('"') or \
                            ele[1].startswith('\'') and ele[1].endswith('\''):
                        val_l = str(ele[1][1:-1])
                    elif ele[1].isdigit():
                        val_l = int(ele[1])
                    elif is_float(ele[1]):
                        val_l = float(ele[1])
                    elif ele[1].strip().upper() == 'TRUE':
                        val_l = True
                    elif ele[1].strip().upper() == 'FALSE':
                        val_l = False

                    val_k = snake_case(ele[0].strip()).replace(".", "__")
                    if opt[0] == '=':
                        val_s[val_k] = val_l
                    else:
                        val_s[val_k + '__' + opt[1]] = val_l
                    q_s = Q(**val_s)
                    values.append(q_s)
        res |= Q(*values)
    return res


def get_sub_query(sub_content, hsh):
    idx_ini = sub_content.find('[')
    idx_end = sub_content.find(']')
    idx = sub_content[idx_ini + 1: idx_end]
    return hsh['Q[' + str(idx) + ']']