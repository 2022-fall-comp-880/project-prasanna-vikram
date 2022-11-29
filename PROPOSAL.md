# Netflix Original Films & IMDB Score

**Author**: Lakshmi Prasanna Malempati 
**Date**: 28 Nov 2022


## Motivation 
  The Motivation behind choosing this data set is based on IMDB score, Genre type we can recommend movies or series available in Netflix to any person in preferred languages.  

The dataset for the project `Netflix Original Films & IMDB Scores` consists of all Netflix original films, documentaries, specials and their corresponding IMDB Scores as of 06/01/21.

## Investigative Questions 
The dataset has 6 attributes: Title, Genre, Premiere, Runtime, IMDB score and language. In My project I want to investigate and provide some insights about attributes such as genre, language , IMDB score of various Netflix Original Films.

1. What are the languages present in each genre?  

2. what is the average IMDB score for each genre ?  

3. Get the Runtime of Netflix movies based on their genre type

## Approach 

* The dataset is taken from `https://www.kaggle.com` , the size of dataset is 584 rows. The source for dataset is `https://en.wikipedia.org/wiki/Lists_of_Netflix_original_films`.
* Luiscorter,a Kaggle contributor and Data analyst created the dataset . He made his recent update in 2021 .
* I am planning to use data structures like lists and dictionaries in my project to represent the data.
* Also perform transformations like converting the input data in lists to dictionaries as output and vice versa by writing methods, functions within the class.
* Create `apps` folder with `main.py` module, with a main method and other methods to implement the investigative questions .
* Also create a `data` directory which has multiple data files from our project dataset with 1-entry, 5-entry, 10-entry data files in .txt format that is used for unit testing.
* The `DESIGN.md` file should be created in which we describe the design implementation steps in markdown file for all the methods, functions we will write in `apps.main` module .

## Expected Results 
1. Genre as keys in string format and list of languages for that genre type as values are produced as output to 'Netflix Originals present in each genre' in dictionary format.
2. Average IMDB score for each genre in float format are taken as value to corresponding Genre as key where genre is in string format.
3. Runtime for each genre in float format are taken as value to corresponding netflix title as key where title is in string format and this entire datastructure in dictionary format is mapped as values to `Genre` key , the entire output will be in nested dictionary format.

## New Python Packages or Modules 

* `import os`: The OS module in Python provides functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory.
* `import csv` : The csv module implements classes to read and write tabular data in CSV format.
* `import unittest` : The framework implemented by unittest supports fixtures, test suites, and a test runner to enable automated testing for your code.
 

## Dataset Documentation

* Dataset name : Netflix Original Films & IMDB Scores
* Dataset attributes:
  * `Title` : Name or title of the Netflix original
  * `Genre` : genre or type of Netflix series or movie
  * `Premiere` : Date on which the movie is premiered
  * `Runtime` : Runtime or duration of movie
  * `IMDB Score`: Rating given for the movie by IMDB
  * `Language` : Language of the movie 
* Dataset version number or date : version 1, 06/01/2021
* Dataset owner : Luiscorter
* Who can access this dataset : It's in public domain, so everybody can access it.
* What does each item/data point represent : a movie/film
* How many items are in the dataset? : 584
* What data is available about each item : Title of movie, Premiere, Run time, language , IMDB rating , Genre.
 
