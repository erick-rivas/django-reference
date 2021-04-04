from unittest import TestCase

from django.db.models import Q
from seed.util.query_util import multi_q, sql_alike_q


class TestQueryUtil(TestCase):
    def test_multi_q(self):
        input_01 = [{"key_01": "val_01"}, [{"key_02": "val_02"}, {"key_03": "val_03"}]]
        test_01 = multi_q(input_01)
        output_01 = Q(key_01="val_01") | Q(key_02="val_02") | Q(key_03="val_03")
        self.assertEqual(test_01, output_01)

    def test_sql_alike_q(self):
        input_01 = "key_01=val_01 AND key_02=val_02 OR key_03=val_03"
        test_01 = sql_alike_q(input_01)
        output_01 = Q(Q(key_01="val_01"), Q(key_02="val_02")) | Q(Q(key_03="val_03"))
        with self.subTest():
            self.assertEqual(test_01, output_01)

        input_02 = "key_01 > val_01 AND key_02 < val_02 AND key_03 >= val_03 AND key_04 <= val_04"
        test_02 = sql_alike_q(input_02)
        output_02 = Q(Q(key_01__gt="val_01"), Q(key_02__lt="val_02"), Q(key_03__gte="val_03"), Q(key_04__lte="val_04"))
        with self.subTest():
            self.assertEqual(test_02, output_02)

        input_03 = "key_01 LIKE val_01 AND key_02 ILIKE val_02"
        test_03 = sql_alike_q(input_03)
        output_03 = Q(Q(key_01__contains="val_01"), Q(key_02__icontains="val_02"))
        with self.subTest():
            self.assertEqual(test_03, output_03)

        input_04 = "key_01t=true AND key_01f=false AND key_02=17 AND key_03=3.1416 AND key_04='Hola mundo'"
        test_04 = sql_alike_q(input_04)
        output_04 = Q(Q(key_01t=True), Q(key_01f=False), Q(key_02=17), Q(key_03=3.1416), Q(key_04='Hola mundo'))
        with self.subTest():
            self.assertEqual(test_04, output_04)

        input_05 = "keyV1=val_01 AND keyV2=val_02"
        test_05 = sql_alike_q(input_05)
        output_05 = Q(Q(key_v1="val_01"), Q(key_v2="val_02"))
        with self.subTest():
            self.assertEqual(test_05, output_05)

        input_06 = "(key_01=val_01 OR key_02=val_02) AND key_03=val_03"
        test_06 = sql_alike_q(input_06)
        output_06 = Q(Q(Q(key_01="val_01")) | Q(Q(key_02="val_02")), Q(key_03="val_03"))
        with self.subTest():
            self.assertEqual(test_06, output_06)

        input_07 = "(key_01=val_01 OR (key_02=val_02 AND key_03=val_03)) AND key_04=val_04"
        test_07 = sql_alike_q(input_07)
        output_07 = Q(Q(Q(key_01="val_01")) | Q(Q(key_02="val_02"), Q(key_03="val_03")), Q(key_04="val_04"))
        with self.subTest():
            self.assertEqual(test_07, output_07)