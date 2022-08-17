import unittest
from parameterized import parameterized
from unittest.mock import patch
from main import get_doc_owner_name, check_document_existance, get_all_doc_owners_names, \
    add_new_shelf, remove_doc_from_shelf, append_doc_to_shelf, delete_doc, get_doc_shelf,\
    move_doc_to_shelf, add_new_doc

fixture = [
    ["2207 876234", True],
    ["11-2", True],
    ["10006", True],
    ["10007", False]
]

class TestFunctions(unittest.TestCase):

    @parameterized.expand(fixture)
    def test_check_document_existance(self, a, b):
        self.assertEqual(check_document_existance(a), b)

    @patch('builtins.input', side_effect=['10006'])
    def test_get_doc_owner_name(self, mock_input):
        self.assertEqual(get_doc_owner_name(mock_input), 'Аристарх Павлов')

    def test_get_all_doc_owners_names(self):
        self.assertEqual(get_all_doc_owners_names(), {'Василий Гупкин', 'Аристарх Павлов', 'Геннадий Покемонов'})

    def test_remove_doc_from_shelf(self):
        self.assertEqual(remove_doc_from_shelf('11-2'), (['2207 876234','5455 028765']))

    @patch('builtins.input', side_effect=['4'])
    def test_add_new_shelf(self, mock_input):
        a = mock_input()
        self.assertEqual(add_new_shelf(a), ('4', True))

    def test_append_doc_to_shelf(self):
        self.assertEqual(append_doc_to_shelf('1234', '2'), ['10006', '1234'])

    @patch('builtins.input', side_effect=['11-2'])
    def test_delete_doc(self, mock_input):
        self.assertEqual(delete_doc(), ('11-2', True))

    @patch('builtins.input', side_effect=['11-2'])
    def test_get_doc_shelf(self, mock_input):
        self.assertEqual((get_doc_shelf()), '1')

    @patch('builtins.input', side_effect=['2207 876234', '3'])
    def test_move_doc_to_shelf(self, mock_input):
        self.assertEqual(move_doc_to_shelf(), ('2207 876234', '3'))

    @patch('builtins.input', side_effect=['41 06 999888', 'Паспорт', 'Антон Борисов', '3'])
    def test_add_new_doc(self, mock_input):
        result = add_new_doc()
        self.assertEqual(result, '3')