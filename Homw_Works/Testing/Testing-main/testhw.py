import unittest
from unittest.mock import patch
import tempfile
import json
import os
from homework import take_from_list, calculate

class TestHomework(unittest.TestCase):

    def test_take_from_list_with_invalid_types(self):
        with self.assertRaises(ValueError):
            take_from_list([1, 2, 3], "1")
        with self.assertRaises(ValueError):
            take_from_list([1, 2, 3], [1, "2"])
        with self.assertRaises(ValueError):
            take_from_list([1, 2, 3], [1.5])

    def test_take_from_list_with_out_of_bound_indices(self):
        with self.assertRaises(IndexError):
            take_from_list([1, 2, 3], [3])
        with self.assertRaises(IndexError):
            take_from_list([1, 2, 3], [0, 4])
    
    def test_take_from_list_valid_case(self):
        self.assertEqual(take_from_list([1, 2, 3], 0), [1])
        self.assertEqual(take_from_list([1, 2, 3], [0, 2]), [1, 3])

    def test_calculate_with_tempdir(self):
        with tempfile.TemporaryDirectory() as tempdir:
            input_file = os.path.join(tempdir, 'input.json')
            output_file = os.path.join(tempdir, 'output.json')
            data = {
                "list": [1, 2, 3, 4, 5],
                "indices": [0, 2, 4]
            }

            with open(input_file, 'w') as f_p:
                json.dump(data, f_p)

            calculate(input_file, output_file)

            with open(output_file, 'r') as f_p:
                result = json.load(f_p)

            self.assertEqual(result, [1, 3, 5])

    @patch('homework.take_from_list')
    def test_calculate_with_mock(self, mock_take_from_list):
        mock_take_from_list.return_value = [1, 2, 3]
        with tempfile.TemporaryDirectory() as tempdir:
            input_file = os.path.join(tempdir, 'input.json')
            output_file = os.path.join(tempdir, 'output.json')
            data = {
                "list": [10, 20, 30, 40],
                "indices": [1, 2, 3]
            }

            with open(input_file, 'w') as f_p:
                json.dump(data, f_p)

            calculate(input_file, output_file)

            mock_take_from_list.assert_called_once_with([10, 20, 30, 40], [1, 2, 3])

            with open(output_file, 'r') as f_p:
                result = json.load(f_p)

            self.assertEqual(result, [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
