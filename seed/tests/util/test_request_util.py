from unittest import TestCase

from rest_framework.exceptions import ValidationError
from seed.util.request_util import has_fields_or_400


class TestReqUtil(TestCase):
    def test_has_fields_or_400(self):
        input_data = {"key": "value"}
        has_fields_or_400(input_data, "key")
        with self.assertRaises(ValidationError):
            has_fields_or_400(input_data, "missing")