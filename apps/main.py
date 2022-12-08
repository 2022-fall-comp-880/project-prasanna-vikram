"""
Represent a data-set of information about Netflix Originals
released until 2021.
Authors:
  - https://github.com/lm1298
  - https://github.com/Vikramkumar8915
"""
import csv


class NetflixOriginals:
    """
        Represent a data-set of Netflix Originals information.

        Concepts:
            Data processing functionality.
            Reading and writing from CSV files.
        """

    def __init__(self, movie_info: list):
        """
         Create and initialize the class attributes.

         Attributes: a list of tuples of:
             title: string
             genre: string
             IMDB rating: float
             Runtime : integer
             language : string
         """
        self.movies_info = movie_info

    def write(self, filename: str):
        """
         Write a CSV file with Netflix Originals info.

         A record is a row in the file, with 5 columns, corresponding to
         Title,Genre,Runtime,IMDB Score and Language.

         filename: filename to write data to
        """
        with open(filename, 'w', encoding='utf8') as file_obj:
            for Title, Genre, Runtime, IMDB_Score, Language in \
                                    self.movies_info:
                movie_info_row = f'{Title},{Genre},{Runtime},{IMDB_Score},' \
                                 f'{Language}\n'
                file_obj.write(movie_info_row)

    def languages_by_genre(self) -> dict:
        """
        Create a dictionary of languages by genre type .

        Creates and returns a dictionary whose keys are genres in string format
             and values are lists of languages corresponding to the genre.

        Return:
            dictionary
                keys: str, representing genre
                value: list of strings, representing languages corresponding
                to the genre .
        """

    def average_runtime_by_genre(self) -> dict:
        """
        Create a dictionary of average runtime by genres .

        Creates and returns a dictionary whose keys are genres in string format
            and values are averages of runtime corresponding to the same
            genre.

        Returns:
            dictionary
                keys: str, representing genre.
                value: float, average of runtime corresponding to the same
                    genre type .
        """

    def imdb_score_ranges(self) -> dict:
        """
        Group imdb scores into ranges.

        Ranges are (for example) "1.0-4.0 ", "4.0-5.0 ", "5.0-6.0 ",
        and so on.
        Ranges are determined based on the data-set, and cannot be hard-coded.

        Returns: dictionary
        keys: float, representing IMDB score ranges
        values: list of strings, with titles in that IMDB score ranges
        """

    def str(self):
        """ Create string representation of data."""


@staticmethod
def read_dataset(filename: str) -> NetflixOriginals:
    """Read a CSV text file that holds 5-element records.

        Title of movie, Run time, language , IMDB rating , Genre.
        """


def main():
    """Run read_dataset."""


if __name__ == '__main__':
    main()
