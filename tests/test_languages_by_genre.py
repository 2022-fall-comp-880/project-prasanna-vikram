"""Test NetflixOriginals methods."""

import unittest
import os
from unittest import TestCase
from apps.main import read_dataset


class TestNetflixOriginals(TestCase):
    """Test languages_by_genre() method."""

    def setUp(self):
        """Create NetflixOriginals objects for the three testing cases."""
        data_dir = os.path.dirname(__file__) + "/../data"
        self.NetflixOriginals_data_1 = read_dataset(f'{data_dir}/data_1.txt')
        self.NetflixOriginals_data_5 = read_dataset(f'{data_dir}/data_5.txt')
        self.NetflixOriginals_data_10 = read_dataset(f'{data_dir}/data_10.txt')
        self.NetflixOriginals_all = read_dataset(f'{data_dir}/original.txt')

    def test_languages_by_genre_one(self):
        """Test using `self.NetflixOriginals_data_1`."""
        data_dir = os.path.dirname(__file__) + "/../data"
        input_file = data_dir + "/data_1.txt"
        read_dataset(input_file)
        actual_res1 = self.NetflixOriginals_data_1.languages_by_genre()
        expected_res1 = {'Documentary': {'English'}}
        print(actual_res1)
        self.assertDictEqual(actual_res1, expected_res1)
        # self.fail("TODO: Implement test")

    def test_languages_by_genre_five(self):
        """Test using `self.NetflixOriginals_data_5`."""
        data_dir = os.path.dirname(__file__) + "/../data"
        input_file = data_dir + "/data_5.txt"
        read_dataset(input_file)
        actual_res2 = self.NetflixOriginals_data_5.languages_by_genre()
        expected_res2 = {'Action comedy': {'English'}, 'Romantic comedy':
                         {'Hindi'}, 'Drama': {'Korean'}, 'Science fiction':
                         {'English'},
                         'Documentary': {'Hindi'}}
        print(actual_res2)
        self.assertDictEqual(actual_res2, expected_res2)

    def test_languages_by_genre_ten(self):
        """Test using `self.NetflixOriginals_data_10`."""
        data_dir = os.path.dirname(__file__) + "/../data"
        input_file = data_dir + "/data_10.txt"
        read_dataset(input_file)
        actual_res3 = self.NetflixOriginals_data_10.languages_by_genre()
        expected_res3 = {'Documentary': {'English', 'Ukranian'},
                         'Romantic comedy': {'Dutch'}, 'Drama': {'English'},
                         'Comedy ': {'English'}, 'Western': {'English'}}
        print(actual_res3)
        self.assertDictEqual(actual_res3, expected_res3)


if __name__ == '__main__':
    unittest.main()
