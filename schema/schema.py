"""
__Seed builder__v1.0
"""

import graphene

from seed.schema.schema import _Query
from seed.schema.schema import _Mutation

class Query(_Query):
    pass

class Mutation(_Mutation):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)