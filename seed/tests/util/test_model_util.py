from unittest import TestCase

from seed.util.model_util import _inherit_permissions_query


class TestModelUtil(TestCase):
    def test_inherit_permissions_query(self):
        attr = "attr"
        input_01 = {"key_01": "val_01", "key_02": "val_02"}
        test_01 = _inherit_permissions_query(input_01, attr)
        output_01 = {"attr__key_01": "val_01", "attr__key_02": "val_02"}
        with self.subTest():
            self.assertEqual(test_01, output_01)

        input_02 = [{"key_01": "val_01"}, {"key_02": "val_02"}]
        test_02 = _inherit_permissions_query(input_02, attr)
        output_02 = [{"attr__key_01": "val_01"}, {"attr__key_02": "val_02"}]
        with self.subTest():
            self.assertEqual(test_02, output_02)