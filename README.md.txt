Mind and Brain Python Course Final Assignment
Winter Semester '19
Zoya Mooraj

Project #3 - Data analysis: Bugs

A Python script for analysing data in the file 'bugs.csv'.

Clone this repository to download the files and then switch to the newly-cloned directory:
git clone https://github.com/zoya-mooraj/final-assignment.git
cd final-assignment

Contents:
1) bugs.csv
cvs file with data to be used for the analyses

2) bugs_analysis.py
Python script to carry out data analysis

3) test_data.py
Python script to test bugs_analysis.py

4) style_check.py
Python script to check the style and syntax of bugs.csv

5) sources.txt 
Source list of external sources referenced while writing the scripts

6) bug_classification.py
Module to classify bugs according to conditions


Testing:
Testing Data with test_data.py
In order to test the quality of the data, the 'test_data.py' script should be run. This will ensure the data is complete and of the type we expect it to be.
1. First, install pytest (pip install pytest)
2. In terminal, navigate to the root folder (final-assignment)
3. Run py.test

Testing Code with style_check.py:
Run style_check.py script.
In the case that many style errors are shown, an automated style formater can be run using the following line directly in the command window:
#! black [bugs_analysis.py]


Requirements:
These scripts were written using Python 3, thus that is recommended.
Certain installations from the terminal may be required:
pytest
missingo
pandas-summary
black


