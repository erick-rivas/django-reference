"""
__Seed builder__v0.1.8
  (Read_only) Builder util
"""

import re
from django.db.models import Q

def snake_case(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def parse_query(data, model):
    hsh = dict()
    stack = [0]
    hsh_idx = 0
    overflow = 0
    while data.find('(') != -1 and overflow < 100 :
        idx_ini = data[stack[-1]+1: len(data)].find('(') + stack[-1] + 1
        idx_end = data[stack[-1]+1: len(data)].find(')') + stack[-1] + 1
        if idx_ini < idx_end and data[stack[-1]+1: len(data)].find('(') != -1:
            stack.append(idx_ini)
        else:
            sub_con = data[stack[-1]: idx_end + 1]
            sub_query = get_query(sub_con[1: len(sub_con)-1], hsh)
            sub_name = "Q[" + str(hsh_idx) + "]"
            data = data.replace(sub_con, sub_name, 1)
            hsh[sub_name] = sub_query
            hsh_idx += 1
            stack.pop(-1)
        overflow += 1
    res = get_query(data, hsh)
    return model.objects.filter(res).distinct()


def get_sub_query(sub_content, hsh):
    idx_ini = sub_content.find('[')
    idx_end = sub_content.find(']')
    idx = sub_content[idx_ini + 1: idx_end]
    return hsh["Q[" + str(idx) + "]"]

def get_query(data, hsh):
    data = data.replace(".", "__")
    res = Q()
    queries = [i.strip() for i in data.split("OR")]
    for q in queries:
        if q.startswith("Q["):
            res |= get_sub_query(q, hsh)
        else:
            filters = [i.strip() for i in q.split("AND")]
            values = []
            for f in filters:
                if f.startswith("Q["):
                    values.append(get_sub_query(f, hsh))
                else:
                    val_s = {}
                    opt = ("=", "")
                    if ">=" in f:
                        opt = (">=", "gte")
                    elif "<=" in f:
                        opt = ("<=", "lte")
                    elif ">" in f:
                        opt = (">", "gt")
                    elif "<" in f:
                        opt = ("<", "lt")
                    elif "ILIKE" in f:
                        opt = ("ILIKE", "icontains")
                    elif "LIKE" in f:
                        opt = ("LIKE", "contains")

                    ele = f.split(opt[0])
                    if len(ele) > 1:
                        if opt[0] == "=":
                            val_s[snake_case(ele[0].strip())] = ele[1].strip()
                        else:
                            val_s[snake_case(ele[0].strip()) + "__" + opt[1]] = ele[1].strip()
                        q_s = Q(**val_s)
                        values.append(q_s)
            res |= Q(*values)
    return res
