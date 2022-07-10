"""
__Seed builder__
  (Read_only) Test util
"""

import json


def assert_json(json_a, json_b):
    """
    Compare the content of two json objects

    :param json_a: First json object
    :param json_b: Second json object
    :return: True if they are equal false otherwise
    """
    return \
        json.dumps(json_a, indent=2, sort_keys=True) == json.dumps(json_b, indent=2, sort_keys=True)