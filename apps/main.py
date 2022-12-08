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
        lang_genre = {}
        for netflix_data in self.movies_info:
            if netflix_data[1] not in lang_genre:
                lang_genre[netflix_data[1]] = {netflix_data[4]}
            else:
                if netflix_data[4] not in lang_genre[netflix_data[1]]:
                    lang_genre[netflix_data[1]].add(netflix_data[4])
        return lang_genre

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
        genre = set()
        runtimes = []
        avg_runtime_by_genre = {}
        for movie_data in self.movies_info:
            genre.add(movie_data[1])
        for ele in genre:
            runtimes.clear()
            for movie_data in self.movies_info:
                if movie_data[1] == ele:
                    runtimes.append(int(movie_data[2]))
            avg_runtime_by_genre[ele] = round(sum(runtimes) / len(runtimes), 2)
        return avg_runtime_by_genre

    @staticmethod
    def find_range(self, imdb_score: float):
        """Group salary into ranges."""
        if 1 < imdb_score < 4:
            return "Below 4 Rating"
        elif 4 < imdb_score < 5:
            return "4.0-5.0 Rating"
        elif 5 < imdb_score < 6:
            return "5.0-6.0 Rating"
        elif 6 < imdb_score < 7:
            return "6.0-7.0 Rating"
        elif 7 < imdb_score < 8:
            return '7.0-8.0 Rating'
        elif 8 < imdb_score < 9:
            return '8.0-9.0 Rating'
        else:
            return '9.0-10.0 Rating'
    def imdb_score_ranges(self) -> dict:
        """
        Group imdb scores into ranges.

        Ranges are (for example) "1.0-4.0 ", "4.0-5.0 ", "5.0-6.0 ",
        and so on.
        Ranges are determined based on the data-set, and cannot be hard-coded.

        Returns: dictionary
        keys: string, representing IMDB score  rating ranges
        values: list of strings, with titles in that IMDB score ranges
        """

    def str(self):
        """ Create string representation of data."""
        return str(self.movies_info)


@staticmethod
def read_dataset(filename: str) -> NetflixOriginals:
    """
    Read a CSV text file that holds 5-element records.

    Title of movie, Run time, language , IMDB rating , Genre.
    """
    movies = []
    with open(filename) as file:
        file_read = csv.reader(file, delimiter=',')
        file_read._next_()
        for row in file_read:
            movies.append(tuple(row))
    return NetflixOriginals(movies)



def main():
    """Run read_dataset."""
    filename = "C:/Users/unhmguest/comp880/finalproject/" \
               "project-prasanna-vikram/data/data_10.txt"
    Netflix_data1 = read_dataset(filename)
    print(Netflix_data1.languages_by_genre())
    print(Netflix_data1.str())
    print(Netflix_data1.average_runtime_by_genre())
    # print(Netflix_data1.imdb_score_ranges())


if __name__ == '__main__':
    main()
