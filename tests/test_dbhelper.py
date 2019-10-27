from unittest import TestCase
from unittest.mock import patch
from src.db_helper import DbHelper


class TestDbHelper(TestCase):

    @patch('src.db_helper.DbHelper')
    def test_get_maximum_salary_with_mocking(self, MockDbHelper):
        db_helper = MockDbHelper()  # create a mock object of DbHelper class
        db_helper.get_maximum_salary.return_value = "700"
        actual = db_helper.get_maximum_salary()
        expected = "700"
        self.assertEqual(actual, expected)

    @patch('src.db_helper.DbHelper')
    def test_get_minimum_salary_with_mocking(self, MockDbHelper):
        db_helper = MockDbHelper()       # create a mock object of DbHelper class
        db_helper.get_minimum_salary.return_value = "556"
        actual = db_helper.get_minimum_salary()
        expected = "556"
        self.assertEqual(actual, expected)


