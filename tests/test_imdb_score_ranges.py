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
        expected_res1 = {'more than 9 Range': ['The Babysitter']}
        self.assertDictEqual(actual_res1, expected_res1)

    def test_imdb_score_ranges_five(self):
        """Test using `self.NetflixOriginals_data_5`."""
        actual_res2 = self.NetflixOriginals_data_5.imdb_score_ranges()
        expected_res2 = {'5.1-6.0 Range': ['The Do-Over'], '6.1-7.0 Range':
                         ['Love per Square Foot', 'Night in Paradise'],
                         'more than 9 Range': ['Mute'],
                         '0.0-4.0 Range': ['Ladies First']}
        self.assertDictEqual(actual_res2, expected_res2)

    def test_imdb_score_ranges_ten(self):
        """Test using `self.NetflixOriginals_data_10`."""
        actual_res3 = self.NetflixOriginals_data_10.imdb_score_ranges()
        expected_res3 = {'6.1-7.0 Range': ['My Own Man'], '7.1-8.0 Range':
                         ['The Other One: The Long Strange Trip of Bob Weir',
                          'What Happened Miss Simone?',
                          'Keith Richards: Under the Influence',
                          'Beasts of No Nation'],
                         '0.0-4.0 Range': ['Hot Girls Wanted',
                                           'The Ridiculous 6'],
                         '4.1-5.0 Range': ['Just Say Yes'], '8.1-9.0 Range':
                             ['Winter on Fire: Ukraine Fight for Freedom'],
                         '5.1-6.0 Range': ['A Very Murray Christmas']}

        self.assertDictEqual(actual_res3, expected_res3)


if __name__ == '__main__':
    unittest.main()
