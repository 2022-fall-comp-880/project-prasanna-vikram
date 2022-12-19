
# Project Report

## 1. Purpose 

* The dataset for the project `Netflix Original Films & IMDB Scores` consists of all Netflix original films, documentaries, specials and their corresponding IMDB Scores as of 06/01/21.
* The Motivation behind choosing this dataset is based on IMDB score, Genre type we can recommend movies or series available in Netflix to any person in their preferred languages.
* The dataset is taken from `https://www.kaggle.com` , the size of dataset is 584 rows. The source for dataset is `https://en.wikipedia.org/wiki/Lists_of_Netflix_original_films`.
* Luiscorter,a Kaggle contributor and Data analyst created the dataset . He made his recent update in 2021 .
* **Dataset attributes**:
  * `Title` : Name or title of the Netflix original
  * `Genre` : genre or type of Netflix series or movie
  * `Runtime` : Runtime or duration of movie
  * `IMDB Score`: Rating given for the movie by IMDB
  * `Language` : Language of the movie 
* Dataset version number or date : version 1, 06/01/2021
* Dataset owner : Luiscorter
* Who can access this dataset : It's in public domain, so everybody can access it.
* What does each item/data point represent : a movie/film
* How many items are in the dataset? : 584
* What data is available about each item : Title of movie, Run time, language , IMDB rating , Genre.

* **Investigative Questions**:

1. What are the unique languages present in each genre?

2. What is the average runtime for each genre ?  

3. Get the list of movie titles based on the range of IMDB scores 
 

## 2. Approach 

* I am planning to use data structures like lists,sets and dictionaries in my project to represent the data.
* Also perform transformations on data structures like converting the input data in list of tuples,csv format to dictionaries as output by writing methods, functions within the class.
* Create `apps` folder with `main.py` module, with a main method and other methods to implement the investigative questions .
* Also create a `data` directory which has multiple data files from our project dataset with 1-entry, 5-entry, 10-entry data files in .txt format that is used for unit testing.
* Create `tests` folder and write testing classes for each question in separate files with each file having 3 testing methods for 1,5 and 10 entries.

### 1. What are the unique languages present in each genre?

* Create and initialize an empty dictionary and assign it to an accumulator pattern variable `lang_genre`.
* Taking for loop iterate through each element in `self.movies_info` .
 * Check if the language `lang` is already present in the accumulator dictionary, if not:
   * Create a new set of languages as value and map that to genre as key in accumulator dictionary `lang_genre`.
 * Else : Add the language as value to existing genre which is a key in string format.
* After completion of loop iteration finally return the accumulator dictionary variable `lang_genre`  with genres are keys and 
list of languages in string format as values to that genre.

### 2. What is the average runtime of each genre ? 

* Create and initialize an empty dictionary `avg_runtime_by_genre` as an accumulator variable.
* Also initialize a set variable for `genre` and for the runtimes of genre create a list.
* Taking for loop iterate through each element `movie_data` in `self.movies_info`, Add the second element of self.movies_info `movie_data[1]` to `genre` set.
* Taking another for-loop iterate through each element 'ele' in `genre` set:
* Taking for loop iterate through each element `movie_data` in `self.movies_info`:
  * If the movie_data[1] of `self.movies_info` is equal to `ele`.
    * Append the second element of `self.movies_info` i.e., movie_data[2] to `runtimes` accumulator list.
  * Continue this loop iteration until the last element of movies_info.
* Calculate the average_runtime and assign it to dictionary accum variable as `avg_runtime_by_genre[ele]` by finding the average as `round(sum(runtimes) / len(runtimes), 2)`
* Return the `avg_runtime_by_genre` as output dictionary with `genre` in str format as keys, average runtime of genre in float format as values to that genre.
 
### 3. Get the list of movie titles based on the range of IMDB scores

* Initialize a variable `ranges` and assign it with an empty dictionary to store the output.
* Also initialize `lst` and assign it to empty list to sore the list of titles as values in `ranges` dictionary.
* Taking for-loop iterate through each element `movies` in `self.movies_info`:
* Initialize the variables `mini` and `maxi` for getting the minimum and maximum salaries in `self.movies_info`.
* Assign `mini` and `maxi` with the minimum and maximum rating values in `lst` and consider `min1` as `min2`.
* Taking `while` loop if min2 < max1 then create and initialize `value1`, Format "{} - {} rating" with corresponding values and make this as one of the keys in the dictionary as `ranges[value1]`, make the value for the key as [].
* If `min1` and `max1` are equal and `float(max1)` is 10.0 , Format "{} - {} rating" with corresponding values and make this as one of the keys in the dictionary as `ranges[value1]`, make the value for the key as [].
* Compare each value of rating in `self.movies_info` with `mini` and `maxi` using `if` statement.
* Return `ranges` as output dictionary with rating ranges in string format as keys and the list of movie titles in str format as values to ranges dictionary.

## 3. Testing 

Unittest library is used for testing the project results. This library can be imported by using import unittest.

### class TestLanguagesByGenre(TestCase)
* The class TestLanguagesByGenre(TestCase) has testing methods to test the method languages_by_genre in the class NetflixOriginals.

def test_languages_by_genre_one(self):
* This method tests the method languages_by_genre over a single entity data file netflix_one.txt and validates result using assertDictEqual statements.
* In this method, first read_dataset method is called on the data file and the output of this function call will be a list which is given as an argument to `imdb_score_ranges_one` method.
* The output will be a dictionary which will be stored in actual_result and it will be validated with expected_result using assertDictEqual statements.

def test_languages_by_genre_five(self):
* This method tests the method languages_by_genre over 5 entities data file `netflix_five.txt` and validates result using assertDictEqual statements.
* In this method, first read_dataset method is called on the data file and the output of this function call will be a list which is given as an argument to `languages_by_genre` method.
* The output will be a dictionary which will be stored in actual_result and it will be validated with expected_result using assertDictEqual statements. 

def test_languages_by_genre_ten(self):
* This method tests the method languages_by_genre over 10 entities data file `netflix_ten.txt` and validates result using assertDictEqual statements.
* In this method, first read_dataset method is called on the data file and the output of this function call will be a list which is given as an argument to `languages_by_genre` method.
* The output will be a dictionary which will be stored in actual_result and it will be validated with expected_result using assertDictEqual statements.

### class TestImdbScoreRanges(TestCase)
* The class TestImdbScoreRanges(TestCase) has testing methods to test the method `imdb_score_ranges()` in the class NetflixOriginals.

def test_imdb_score_ranges_one(self):
* This method tests the method imdb_score_ranges over a single entity data file netflix_one.txt and validates result using assertDictEqual statements.
* In this method, first read_dataset method is called on the data file and the output of this function call will be a list which is given as an argument to `imdb_score_ranges` method.
* The output will be a dictionary which will be stored in actual_result and it will be validated with expected_result using assertDictEqual statements. 

def test_imdb_score_ranges_five(self):
* This method tests the method imdb_score_ranges over 5 entities data file `netflix_five.txt` and validates result using assertDictEqual statements.
* In this method, first read_dataset method is called on the data file and the output of this function call will be a list which is given as an argument to `imdb_score_ranges` method.
* The output will be a dictionary which will be stored in actual_result and it will be validated with expected_result using assertDictEqual statements.

def test_imdb_score_ranges_ten(self):
* This method tests the method imdb_score_ranges over 10 entities data file `netflix_ten.txt` and validates result using assertDictEqual statements.
* In this method, first read_dataset method is called on the data file and the output of this function call will be a list which is given as an argument to `imdb_score_ranges` method.
* The output will be a dictionary which will be stored in actual_result and it will be validated with expected_result using assertDictEqual statements.

### class TestAverageRuntimeByGenre(TestCase)

The class TestAverageRuntimeByGenre(TestCase) has testing methods to test the method languages_by_genre in the class NetflixOriginals.
 
def test_average_runtime_by_genre_one(self):
* This method tests the method average_runtime_by_genre over a single entity data file `netflix_one.txt` and validates result using assertDictEqual statements.
* In this method, first read_dataset method is called on the data file and the output of this function call will be a list which is given as an argument to `average_runtime_by_genre` method.
* The output will be a dictionary which will be stored in actual_result and it will be validated with expected_result using assertDictEqual statements.

def test_average_runtime_by_genre_five(self):
* This method tests the method average_runtime_by_genre over 5 entities data file `netflix_five.txt` and validates result using assertDictEqual statements.
* In this method, first read_dataset method is called on the data file and the output of this function call will be a list which is given as an argument to `average_runtime_by_genre` method.
* The output will be a dictionary which will be stored in actual_result and it will be validated with expected_result using assertDictEqual statements.

def test_average_runtime_by_genre_ten(self):
* This method tests the method average_runtime_by_genre over 10 entities data file `netflix_ten.txt` and validates result using assertDictEqual statements.
* In this method, first read_dataset method is called on the data file and the output of this function call will be a list which is given as an argument to `average_runtime_by_genre` method.
* The output will be a dictionary which will be stored in actual_result and it will be validated with expected_result using assertDictEqual statements.

* pytest can also be used for testing the results. It also supports unittest test cases execution. It has benefits like supporting built in assert statement, filtering of test cases, returning from last failing test etc.


## 4. Results 

**def languages_by_genre(self) -> dict:**

*  The output is a dictionary. Genre as keys in string format and languages as set of strings for that genre type as values are produced as output to languages present in each genre in dictionary format.

**def average_runtime_by_genre(self) -> dict:**

* The output is a dictionary. Average runtime for each genre in float format are taken as value to corresponding Genre as key where genre is in string format is generated in dictionary format as an output to average runtime of each genre.

**def imdb_score_ranges(self) -> dict:**

* The output is a dictionary. IMDB score ranges in string format as keys and list of titles in string format as values to the keys are generated as output in dictionary format.

## 5. Evaluation 

### 5.1 What Works and Scope Assumptions
From the dataset that we have taken from kaggle we are able to get the information about in each genre what languages are present, categorize movies based on imdb score ranges and average runtime for each genre. 
### 5.2 Immediate Further Development

* We can visually represent the findings in bar, histogram format and build dashboard using tableau software.
* We can also find what are the top five genres that has more than 8 rating and limited runtime.
