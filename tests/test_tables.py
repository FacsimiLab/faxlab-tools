import unittest
import pandas as pd
import numpy as np
from faxlab_tools.tables.sanitization import find_and_replace_df, fix_column_dtype
from faxlab_tools.tables.slicing import filter_columns_substring, drop_columns_regex

class TestSanitization(unittest.TestCase):
    def test_find_and_replace_df(self):
        df = pd.DataFrame({'A': ['foo', 'bar', 'foo'], 'B': [1, 2, 3]})
        result = find_and_replace_df(df, 'A', 'foo', 'baz')
        self.assertListEqual(result['A'].tolist(), ['baz', 'bar', 'baz'])

    def test_fix_column_dtype_all_types(self):
        # Read synthetic DataFrame from CSV
        df = pd.read_csv('tests/test_sample_df.csv')

        # Path to dtype CSV
        csv_path = 'tests/test_dtype_dict.csv'
        # Run fix_column_dtype
        result = fix_column_dtype(df, csv_path=csv_path)

        # Check dtypes
        self.assertTrue(np.issubdtype(result['col_int'].dtype, np.integer))
        self.assertTrue(np.issubdtype(result['col_float'].dtype, np.floating))
        self.assertTrue(result['col_str'].dtype == object or result['col_str'].dtype == 'string')
        self.assertTrue(result['col_cat'].dtype.name == 'category')
        self.assertTrue(np.issubdtype(result['col_int_str'].dtype, np.integer))
        self.assertTrue(np.issubdtype(result['col_float_str'].dtype, np.floating))

        # # Check values
        # self.assertEqual(result['col_int'][0], 1)
        # self.assertAlmostEqual(result['col_float'][1], 1.1)
        # self.assertEqual(result['col_str'][2], 'z')
        # self.assertEqual(result['col_cat'][1], 'cat2')
        # self.assertEqual(result['col_int_str'][2], 6)
        # self.assertAlmostEqual(result['col_float_str'][0], 7.1)

class TestSlicing(unittest.TestCase):
    def test_filter_columns_substring(self):
        df = pd.DataFrame({'foo_col': [1], 'bar_col': [2], 'baz': [3]})
        result = filter_columns_substring(df, ['foo', 'baz'])
        self.assertCountEqual(result, ['foo_col', 'baz'])

    def test_drop_columns_regex(self):
        df = pd.DataFrame({'foo1': [1], 'bar2': [2], 'foo2': [3]})
        result = drop_columns_regex(df, r'^foo\d')
        self.assertListEqual(list(result.columns), ['bar2'])

if __name__ == '__main__':
    unittest.main()
