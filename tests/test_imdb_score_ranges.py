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
        data_dir = os.path.dirname(__file__) + "/../data"
        input_file = data_dir + "/data_1.txt"
        read_dataset(input_file)
        actual_res1 = self.NetflixOriginals_data_1.imdb_score_ranges()
        expected_res1 = {'6.0-7.0 Rating': ['The Babysitter']}
        print(actual_res1)
        self.assertDictEqual(actual_res1, expected_res1)
        # self.fail("TODO: Implement test")

    def test_average_runtime_by_genre_five(self):
        """Test using `self.NetflixOriginals_data_5`."""
        data_dir = os.path.dirname(__file__) + "/../data"
        input_file = data_dir + "/data_5.txt"
        read_dataset(input_file)
        actual_res2 = self.NetflixOriginals_data_5.imdb_score_ranges()
        expected_res2 = {'5.0-6.0 Rating': ['The Do-Over', 'Mute'],
                        '7.0-8.0 Rating': ['Love per Square Foot',
                                           'Ladies First'],
                        '6.0-7.0 Rating': ['Night in Paradise']}
        print(actual_res2)
        self.assertDictEqual(actual_res2, expected_res2)

    def test_average_runtime_by_genre_ten(self):
        """Test using `self.NetflixOriginals_data_10`."""
        data_dir = os.path.dirname(__file__) + "/../data"
        input_file = data_dir + "/data_10.txt"
        read_dataset(input_file)
        actual_res3 = self.NetflixOriginals_data_10.imdb_score_ranges()
        expected_res3 = {'6.0-7.0 Rating': ['My Own Man', 'Hot Girls Wanted'],
                         '7.0-8.0 Rating':
                             ['The Other One: The Long Strange'
                              ' Trip of Bob Weir',
                              'What Happened, Miss Simone?',
                              'Keith Richards: Under the Influence',
                              'Beasts of No Nation'], '4.0-5.0 Rating':
                             ['Just Say Yes', 'The Ridiculous 6'],
                         '8.0-9.0 Rating':
                             ["Winter on Fire: Ukraine's Fight for Freedom"],
                         '5.0-6.0 Rating': ['A Very Murray Christmas']}

        print(actual_res3)
        self.assertDictEqual(actual_res3, expected_res3)


if __name__ == '__main__':
    unittest.main()
