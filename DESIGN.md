## DESIGN DOCUMENT

## class NetflixOriginals:
    
    Represent a data-set of Netflix Originals information.

    Concepts:
        Data processing functionality.
        Reading and writing from CSV files.
    

### def __init__(self, movie_info: list):
        
        Create and initialize the class attributes.

        Attributes: a list of tuples of:
            title: string
            genre: string
            IMDB rating: float
            Runtime : integer
            language : string

* Initialize `self.movie_info` variable to movie_info by accessing with self parameter.        

### def write(self, filename: str):
        
        Write a CSV file with Netflix Originals info.

        A record is a row in the file, with 5 columns, corresponding to
        Title,Genre,Runtime,IMDB Score and Language.

        filename: filename to write data to

* Open txt file in write mode using `open()` function.
* Taking for-loop iterate for each element of title, genre, runtime, IMDB score and language in `self.movie_info` list.
* Create a variable , using f-strings concatinate title, genre, runtime, IMDB score and language
  as a string for every Netflix Original.
* Assign the whole f-string value to that variable.
* Add or write that variable in another CSV file which is Netflix Originals data and result is a CSV file with all Netflix Originals data.
        
### def language_by_genre(self) -> dict:
        
        create a dictionary of languages by genre type .

        Creates and returns a dictionary whose keys are genres in string format
             and values are lists of languages corresponding to the genre.

        Return:
            dictionary
                keys: str, representing genre
                value: list of strings, representing languages corresponding
                to the genre .

* Create and initialize an empty dictionary and assign it to an accumulator pattern variable.
* Taking for loop iterate through each element in `self.movie_info` .
 * Check if the language is already present in the accumulator dictionary, if it satisfies:
   * Append the language as value to existing genre which is a key in string format.
 * Else create a new list of languages as value and map that to genre as key in accumulator dictionary variable.
* After completion of loop iteration finally return the accumulator dictionary variable where genres are keys and 
list of languages in string format as values to that genre.

### def average_runtime_by_genre(self) -> dict:

        Create a dictionary of average runtime by genres .

        Creates and returns a dictionary whose keys are genres in string format
            and values are averages of runtime corresponding to the same
            genre.

        Returns:
            dictionary
                keys: str, representing genre.
                value: float, average of runtime corresponding to the same
                    genre type .

* Create and initialize an empty dictionary as an accumulator variable.
* Taking for loop iterate through each element in `self.movie_info`.
* Import `statistics` module and using `mean()` function in statistics module find the average runtime.
* Map or assign the average runtime in float format as value to corresponding genre as key of accumulator dictionary variable
* Iterate the loop until end and return the accumulator dictionary as an output.

### def imdb_score_ranges(self) -> dict:
        
        Group imdb scores into ranges.

        Ranges are (for example) "1.0-4.0 ", "4.0-5.0 ", "5.0-6.0 ",
        and so on.
        Ranges are determined based on the data-set, and cannot be hard-coded.

        Returns: dictionary
            keys: float, representing IMDB score ranges
            values: list of strings, with titles in that IMDB score ranges

* Taking nested-if conditional statements group the IMDB scores into various ranges.
* Create and initialize an empty dictionary and assign it to an accumulator pattern variable.
* Taking for loop iterate through each element in `self.movie_info` .
 * Check if that rating range is present in the accumulator dictionary, if it satisfies:
   * Append the corresponding list of movie titles in that range in string format as value
    to that imdb score range in float format which is a key in string format.
 * Else create a list of movie titles as values and map that to imdb score range as keys in accumulator dictionary variable.
* After completion of loop iteration finally return the accumulator dictionary variable where IMDB score range are keys and 
list of titles in string format as values in that range of imdb scores.

### def str(self):
        Create string representation of data.

* Return the `self.movie_info` as output string

### def read_dataset(filename: str) -> NetflixData:
        Read a CSV text file that holds 5-element records.

* Create an empty list  `movies_info` as an accumulator.
* Open the file `filename` in read mode as `file_open`.
* Iterate each element `ai` in  `file_open.readlines()` by taking for loop.
 * perform stripping on the hard code data in txt file and separate each element with `,`, convert te entire data into tuples from.
 * Append the data into accumulator variable `movies_info` .
* Close the opened file using `close()` function.
* Return list as an output to `NetflixData`.

