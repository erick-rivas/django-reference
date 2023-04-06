"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Example domain tests
"""

import json
from unittest import TestCase
from seed.util.test_util import assert_json

class TestExample(TestCase):

    def setUp(self):
        pass

    def test_math_floor(self):
        with self.subTest():
            inp = 3
            test = inp ** 2
            out = 9
            self.assertEqual(out, test)

        with self.subTest():
            inp = 9
            test = inp // 2
            out = 4
            self.assertEqual(out, test)

    def test_delete_dic(self):
        with self.subTest():
            inp = { "a": 1, "b": 2}
            test = inp
            del inp["b"]
            out = { "a": 1 }
            self.assertEqual(out, test)