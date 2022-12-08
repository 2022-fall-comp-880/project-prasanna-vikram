"""Test NetflixOriginals methods."""

import unittest
import os
from unittest import TestCase
from apps.main import read_dataset


class TestNetflixOriginals(TestCase):
    """Test average_runtime_by_genre() method."""

    def setUp(self):
        """Create NetflixOriginals objects for the three testing cases."""
        data_dir = os.path.dirname(__file__) + "/../data"
        self.NetflixOriginals_data_1 = read_dataset(f'{data_dir}/data_1.txt')
        self.NetflixOriginals_data_5 = read_dataset(f'{data_dir}/data_5.txt')
        self.NetflixOriginals_data_10 = read_dataset(f'{data_dir}/data_10.txt')
        self.NetflixOriginals_all = read_dataset(f'{data_dir}/original.txt')

    def test_average_runtime_by_genre_one(self):
        """Test using `self.NetflixOriginals_data_1`."""
        actual_res1 = self.NetflixOriginals_data_1.average_runtime_by_genre()
        expected_res1 = {'Teen comedy horror': 85.0}
        self.assertDictEqual(actual_res1, expected_res1)

    def test_average_runtime_by_genre_five(self):
        """Test using `self.NetflixOriginals_data_5`."""
        actual_res2 = self.NetflixOriginals_data_5.average_runtime_by_genre()
        expected_res2 = {'Drama': 132.0, 'Romantic comedy': 133.0,
                         'Documentary': 39.0, 'Science fiction': 126.0,
                         'Action comedy': 108.0}
        self.assertDictEqual(actual_res2, expected_res2)

    def test_average_runtime_by_genre_ten(self):
        """Test using `self.NetflixOriginals_data_10`."""
        actual_res3 = self.NetflixOriginals_data_10.average_runtime_by_genre()
        expected_res3 = {'Romantic comedy': 97.0, 'Western': 119.0,
                         'Drama': 136.0, 'Documentary': 84.0, 'Comedy ': 56.0}
        self.assertDictEqual(actual_res3, expected_res3)


if __name__ == '__main__':
    unittest.main()
