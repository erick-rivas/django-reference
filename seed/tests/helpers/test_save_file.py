import os
from unittest import TestCase
from seed.helpers.save_file import save_file, save_file_obj
from app.settings import MEDIA_ROOT

class TestSaveFile(TestCase):

    def setUp(self):
        self.input_01 = "file.txt"
        with open(self.input_01, "a") as file:
            file.write("A")
        self.file_01 = open(self.input_01, "r")

    def tearDown(self):
        os.remove(self.file_01.name)

    def test_save_file(self):
        test_01 = save_file(self.input_01)
        self.assertEqual(test_01.name[32:], "_" + self.input_01)
        self.assertEqual(test_01.size, 1)
        self.assertEqual(test_01.url.endswith(self.input_01), True)
        os.remove(MEDIA_ROOT + "/" + test_01.name)

    def test_save_file_obj(self):
        test_01 = save_file_obj(self.file_01)
        self.assertEqual(test_01.name[32:], "_" + self.input_01)
        self.assertEqual(test_01.size, 1)
        self.assertEqual(test_01.url.endswith(self.input_01), True)
        os.remove(MEDIA_ROOT + "/" + test_01.name)