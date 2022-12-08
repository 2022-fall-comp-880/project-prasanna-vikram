
## DESIGN DOCUMENT

**Contributors** : Lakshmi Prasanna, Vikram

## class NetflixOriginals:
    """
    Represent a data-set of Netflix Originals information.

    Concepts:
        Data processing functionality.
        Reading and writing from CSV files.
    """

### def __init__(self, movie_info: list):
       """
        Create and initialize the class attributes.

        Attributes: a list of tuples of:
            title: string
            genre: string
            IMDB rating: float
            Runtime : integer
            language : string
        """

* Initialize `self.movies_info` variable to movie_info by accessing with self parameter.        

### def write(self, filename: str):
        """
        Write a CSV file with Netflix Originals info.

        A record is a row in the file, with 5 columns, corresponding to
        Title,Genre,Runtime,IMDB Score and Language.

        filename: filename to write data to
        """
* Open the txt file `file_obj` in write mode using `open()` function.
* Taking for-loop iterate for each element of title, genre, runtime, imdb_Score, language in `self.movies_info` list.
* Create a variable , using f-strings concatinate title, genre, runtime, imdb_Score, language
  as a string for every Netflix Original.
* Assign the whole f-string value to `movie_info_row` variable.
* Add or write that variable into another CSV file as `file_obj.write(movie_info_row)` and result is a CSV file with all Netflix Originals data.
  
1. Get the unique languages based on genre type.
### def language_by_genre(self) -> dict:
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

* Create and initialize an empty dictionary and assign it to an accumulator pattern variable `lang_genre`.
* Taking for loop iterate through each element in `self.movies_info` .
 * Check if the language `lang` is already present in the accumulator dictionary, if not:
   * Create a new set of languages as value and map that to genre as key in accumulator dictionary `lang_genre`.
 * Else if language is not already mapped to genre present in `lang_genre` accumulator dictionary,
 * Add the language as value to existing genre which is a key in string format.
* After completion of loop iteration finally return the accumulator dictionary variable `lang_genre`  with genres are keys and 
list of languages in string format as values to that genre.

2. What is the average runtime for each genre ? 
 
### def average_runtime_by_genre(self) -> dict:
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

* Create and initialize an empty dictionary `avg_runtime_by_genre` as an accumulator variable.
* Also initialize a set variable for `genre` and for the runtimes of genre create a list.
* Taking for loop iterate through each element `movie_data` in `self.movies_info`:
  * Add the second element of self.movies_info `movie_data[1]` to `genre` set.
* Taking another for-loop iterate through each element 'ele' in `genre` set:
  * Clear the runtimes list .
* Taking for loop iterate through each element `movie_data` in `self.movies_info`:
  * If the movie_data[1] of `self.movies_info` is equal to `ele`.
  * Append the second element of `self.movies_info` i.e., movie_data[2] to `runtimes` accumulator list.
  * Continue this loop iteration until the last element of movies_info.
* Calculate the average_runtime and assign it to dictionary accum variable as `avg_runtime_by_genre[ele]` by finding the average as `round(sum(runtimes) / len(runtimes), 2)`
* Return the `avg_runtime_by_genre` as output dictionary with `genre` in str format as keys, average runtime of genre in float format as values to that genre.

3. Get the list of movie titles based on the range of IMDB scores
 ### def find_range(imdb_score: float):
        """Group salary into ranges."""
* Taking nested-if conditional statements group the IMDB scores into various ranges.
* If `imdb_score` less than 4.0 ,return `Below 4 Rating`.
* Elif `imdb_score` less than 5.0 ,return `4.0-5.0 Rating`.
* Elif `imdb_score` less than 6.0 ,return `5.0-6.0 Rating`.
* Elif `imdb_score` less than 7.0 ,return `6.0-7.0 Rating`.
* Elif `imdb_score` less than 8.0 ,return `7.0-8.0 Rating`.
* Elif `imdb_score` less than 9.0 ,return `8.0-9.0 Rating`.
* If the `imdb_score` greater than that, return `more than 9 rating`.

### def imdb_score_ranges(self) -> dict:
        """
        Group imdb scores into ranges.

        Ranges are (for example) 'Below 4 rating', '4.0-5.0 rating', '5.0-6.0 rating',
        and so on.
        Ranges are determined based on the data-set, and cannot be hard-coded.

        Returns: dictionary
            keys: str, representing IMDB score ranges
            values: list of strings, with titles in that IMDB score ranges
        """

* Create and initialize an empty dictionary and assign it to an accumulator pattern variable `imdb_range`.
* Taking for loop iterate through each element `movie` in `self.movies_info` .
 * Check if that rating range `range1` is present in the accumulator dictionary, if it satisfies:
   * Append the corresponding list of movie titles `movie[0]` in that range in string format as value
    to that imdb score range as key in string format .
 * Else create a list of movie titles as values and map that to imdb score range as keys in accumulator dictionary variable.
* After completion of loop iteration finally return the accumulator dictionary variable `imdb_range` as output
where IMDB score range are keys and 

### def str(self):
       """Create string representation of data."""
* Return the `self.movie_info` as output string

### def read_dataset(filename: str) -> PlayerData:
        """Read a CSV text file that holds 5-element records."""

* Create an empty list `movies` as an accumulator.
* Open the file `filename` in read mode as `file_open`.
* Read the file using `csv.reader`, taking `,` as delimiter . 
* Read the entire file by going to every line and take it as `file_read`.
* `__next__` is used to skip the first row of titles and read from next row .
* Taking for-loop iterate through each `row` in file_read:
  * Append every `tuple(row)` to `movies` accumulator list with each row data in tuple format.
* Return `NetflixOriginals(movies)` where movies as object to NetflixOriginals class, as an output
with list of tuples having each row of NetflixOriginals info in tuple format.
