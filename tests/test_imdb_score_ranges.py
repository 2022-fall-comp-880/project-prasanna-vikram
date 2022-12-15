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

    def test_imdb_score_ranges_one(self):
        """Test using `self.NetflixOriginals_data_1`."""
        actual_res1 = self.NetflixOriginals_data_1.imdb_score_ranges()
        expected_res1 = {'9.0 - 10.0 rating': ['The Babysitter']}
        self.assertDictEqual(actual_res1, expected_res1)

    def test_imdb_score_ranges_five(self):
        """Test using `self.NetflixOriginals_data_5`."""
        actual_res2 = self.NetflixOriginals_data_5.imdb_score_ranges()
        expected_res2 = {'4.0 - 5.0 rating': ['The Do-Over'],
                         '5.0 - 6.0 rating': [], '6.0 - 7.0 rating': ['Mute'],
                         '7.0 - 8.0 rating': ['Love per Square Foot',
                                              'Ladies First'],
                         '8.0 - 9.0 rating': []}

        self.assertDictEqual(actual_res2, expected_res2)

    def test_imdb_score_ranges_ten(self):
        """Test using `self.NetflixOriginals_data_10`."""
        actual_res3 = self.NetflixOriginals_data_10.imdb_score_ranges()
        expected_res3 = {'0.0 - 1.0 rating': ['Hot Girls Wanted'],
                         '1.0 - 2.0 rating': [], '2.0 - 3.0 rating': [],
                         '3.0 - 4.0 rating': [],
                         '4.0 - 5.0 rating': ['Just Say Yes'],
                         '5.0 - 6.0 rating': ['A Very Murray Christmas'],
                         '6.0 - 7.0 rating': ['My Own Man',
                                              'The Ridiculous 6'],
                         '7.0 - 8.0 rating': ['The Other One: The Long Strange'
                                              ' Trip of Bob Weir',
                                              'What Happened Miss Simone?',
                                              'Keith Richards: Under the '
                                              'Influence',
                                              'Beasts of No Nation']}

        self.assertDictEqual(actual_res3, expected_res3)


if __name__ == '__main__':
    unittest.main()
