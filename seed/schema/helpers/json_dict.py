"""
__Seed builder__
  (Read_only) Schema helper
"""

import json

from graphql import Undefined
from graphql.language.ast import StringValueNode

from graphene.types import Scalar

class JSONDict(Scalar):

    @staticmethod
    def serialize(data):
        return data

    @staticmethod
    def parse_literal(node, _variables=None):
        if isinstance(node, StringValueNode):
            try:
                return json.loads(node.value)
            except Exception as error:
                raise ValueError(f"Badly formed JSONString: {str(error)}")
        return Undefined

    @staticmethod
    def parse_value(value):
        return json.loads(value)