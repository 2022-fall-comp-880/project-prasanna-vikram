# HOWTO

## Clone the project:
* Clone the project into your local machine from Github as ` https://github.com/2022-fall-comp-880/project-prasanna-vikram.git`.

## Setting-up virtual environment:
* Open the project folder in PyCharm after cloning in local machine.
* In the status bar (at the bottom of the IDE window), click Python 3.10 and select Interpreter Settings.
* Select Virtualenv Environment.
* Check off New environment.
* Location should be the path to your project folder.
  * If the location is different, change it. 
  * Base interpreter should be Python 3.10 you have installed at the system level.
* Now you can now see the .venv folder with Lib,Scripts sub folders in it under our project in our file structure.

## Install Requirements:
* Import the libraries csv, os and unittest as below:  

     `import os`
     `import csv`
     `import unittest`

## Run the program:
* Run the whole program using the command `python -m apps.main` from terminal.

## Run the tests:
* Run the tests for the method `average_runtime_by_genre` as `python -m tests.test_average_runtime_by_genre`.
* Run the tests for the method `languages_by_genre` as `python -m tests.test_languages_by_genre`.
* Run the tests for the method `imdb_score_ranges` as `python -m tests.test_imdb_score_ranges`.
