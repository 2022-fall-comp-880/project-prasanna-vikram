
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

* Initialize `self.movies_info` variable to `movie_info` by accessing with self parameter.        

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

### def imdb_score_ranges(self) -> dict:
        """
        Group imdb scores into ranges.

        Ranges are (for example) '1.0-2.0 rating', '2.0-3.0 rating', '3.0-4.0 rating',
        and so on.
        Ranges are determined based on the data-set, and cannot be hard-coded.

        Returns: dictionary
            keys: str, representing IMDB score rating ranges
            values: list of strings, with titles in that IMDB score ranges
        """

* Initialize a variable `ranges` and assign it with an empty dictionary to store the output.
* Also initialize `lst` and assign it to empty list to sore the list of titles as values in `ranges` dictionary.
* Taking for-loop iterate through each element `movies` in `self.movies_info`:
  * Append rating which is `float[movies[3]]` to `lst` accumulator list.
* Initialize the variables `mini` and `maxi` for getting the minimum and maximum salaries in `self.movies_info`.
* Assign `mini` and `maxi` with the minimum and maximum rating values in `lst` and consider `min1` as `min2`.
* Using `while` loop and if min2 < max1:
  * Create and initialize `value1`, Format "{} - {} rating" with corresponding values and make this as one of the keys in the dictionary as `ranges[value1]`, make the value for the key as [].
    * Increment the `min2` value.
* If `min1` and `max1` are equal and `float(max1)` is 10.0 , Format "{} - {} rating" with corresponding values and make this as one of the keys in the dictionary as `ranges[value1]`, make the value for the key as [].
* Taking for-loop iterate through each element `movies` in `self.movies_info`:
  * Assign `min1` to variable `value`.
  * Using `while` loop and if value < max1:
    * If `float(movies[3])` greater than or equal to `value` and less than or equal to `value+ 1`.
      * Create and initialize `val1`, Format "{} - {} rating" with corresponding values and make this as one of the keys in the dictionary as `ranges[value1]`, make the value for the key as [].
      * Append `movies[0]` to `ranges[val[1]]`.
    * Else increment the `value`.
  * If `min1` and `max1` are equal and `float(max1)` is 10.0 , Format "{} - {} rating" with corresponding values and make this as one of the keys in the dictionary as `ranges[value1]`, make the value for the key as [].
    * Create and initialize `val1`, Format "{} - {} rating" with corresponding values and make this as one of the keys in the dictionary as `ranges[value1]`, make the value for the key as [].
    * Append `movies[0]` movies title to `ranges[val[1]]`.
* Compare each value of rating in `self.movies_info` with `mini` and `maxi` using `if` statement.
* Return `ranges` as output dictionary with rating ranges in string format as keys and the list of movie titles in str format as values to ranges dictionary.

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
