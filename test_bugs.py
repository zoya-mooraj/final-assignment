# -*- coding: utf-8 -*-
"""
Final Assignment - Zoya Mooraj

Data Testing Script

A script to test the the data and the bugs.csv script. 

Ensures all values in the csv file that are necessary for the analyses in 
'bugs_analysis.py' correspond to what is expected.

Can be updated as new variables are of interest/included in the analyses.

Particularly useful if new participants' data is added to the existing csv file.

Will carry out assertions. 
If true, nothing will occur. 
If false, an AssertionError will be raised.
"""

#pytest-flake8

# %% Import Packages
import os
import numpy as np
import pandas as pd
import seaborn as sns
sns.set_style('white')
from pandas_summary import DataFrameSummary
from bug_classification import bug_classification

# %% Load Data
cwd = os.getcwd()
filename = 'bugs.csv'
filepath = os.path.join(cwd, filename)
df = pd.read_csv(filepath)

df = bug_classification(df)


# %% Automated Tests for Data Completeness

def check_data_completeness(df):
    """
    Automated test to ensure data is complete and has no missing values.
    """
    df_summary = DataFrameSummary(df).summary()
    for col in df_summary.columns:
        assert df_summary.loc['missing', col] == 0, f'{col} has missing values'


def test_bugtype_completeness():
    """
    Automated test to ensure each entry in the bugs.csv has been assigned a 
    bug type value.
    """
    df = pd.read_csv(filepath)
    check_data_completeness(df)


# %% Automated Test for Data Types
# To test if the data type is that which it should be
def test_column_disgust_dtype():
    """
    Checks that the dtype of the 'Disgust' column is a string.
    """
    assert df['Disgust'].dtype == np.object

def test_column_fear_dtype():
    """
    Checks that the dtype of the 'Fear' column is a string.
    """
    assert df['Fear'].dtype == np.object  


def test_column_killrating_dtype():
    """
    Checks that the dtype of the 'KillRating' column is a float.
    """
    assert df['KillRating'].dtype == float

    
def test_column_bugtype_dtype():
    """
    Checks that the dtype of the 'BugType' column is an integer.
    """
    assert df['BugType'].dtype == pd.category
  
    
 # %% Test for Value Correctness
 
def check_killrating_range(df, lower=0, upper=10):
    """
    To ensure KillRating values are between 0 and 10.
    """
    assert min(df['Disgust']) >= lower, f"minimum value less than {lower}"
    assert max(df['Disgust']) <= upper, f"maximum value greater than {upper}"


def check_bugtype_range(df, lower=1, upper=4):
    """
    To ensure BugType values range from 1 to 4 as there are only 4 conditions.
    This can be changed as and when needed.
    >>> e.g. if there are 8 conditions, upper=8)
    """
    assert min(df['Disgust']) >= lower, f"minimum value less than {lower}"
    assert max(df['Disgust']) <= upper, f"maximum value greater than {upper}"


