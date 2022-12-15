"""
Represent a data-set of information about Netflix Originals.

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
            for title, genre, runtime, imdb_score, language in \
                            self.movies_info:
                movie_info_row = f'{title},{genre},{runtime},{imdb_score},' \
                                 f'{language}\n'
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

    def imdb_score_ranges(self) -> dict:
        """
        Group imdb scores into ranges.

        Ranges are (for example) "1.0-2.0 rating", "2.0-3.0 rating ",
        "3.0-4.0 rating",
        and so on.
        Ranges are determined based on the data-set, and cannot be hard-coded.

        Returns: dictionary
        keys: string, representing IMDB score  rating ranges
        values: list of strings, with titles in that IMDB score ranges
        """
        ranges = {}
        lst = []
        for movies in self.movies_info:
            lst.append(float(movies[3]))
        min1 = int(min(lst))
        max1 = int(max(lst))
        min2 = min1

        while min2 < max1:
            value1 = "{} - {} rating".format(float(min2), float(min2) + 1)
            ranges[value1] = []
            min2 = min2 + 1
        if min1 == max1:
            if float(max1) == 10.0:
                value1 = "{} - {} rating".format(float(min2) - 1, float(min2))
                ranges[value1] = []
            else:
                value1 = "{} - {} rating".format(float(min2), float(min2) + 1)
                ranges[value1] = []

        for movies in self.movies_info:
            value = min1
            while value < max1:
                if value <= float(movies[3]) <= (value + 1):
                    val1 = "{} - {} rating".format(float(value),
                                                   float(value) + 1)
                    ranges[val1].append(movies[0])
                    break
                else:
                    value = value + 1
            if min1 == max1:
                if float(max1) == 10:
                    val1 = "{} - {} rating".format(float(min2) - 1,
                                                   float(min2))
                    ranges[val1].append(movies[0])
                else:
                    val1 = "{} - {} rating".format(float(min2),
                                                   float(min2) + 1)
                    ranges[val1].append(movies[0])
        return ranges

    def str(self):
        """Create string representation of data."""
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
        file_read.__next__()
        for row in file_read:
            movies.append(tuple(row))
    return NetflixOriginals(movies)


def main():
    """Run read_dataset."""
    filename = "C:/Users/unhmguest/comp880/finalproject/" \
               "project-prasanna-vikram/data/original.txt"
    netflix_data1 = read_dataset(filename)
    print(netflix_data1.languages_by_genre())
    print(netflix_data1.str())
    print(netflix_data1.average_runtime_by_genre())
    print(netflix_data1.imdb_score_ranges())


if __name__ == '__main__':
    main()
