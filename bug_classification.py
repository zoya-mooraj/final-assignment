# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 22:11:23 2020

@author: ZOYA
"""
import os
import pandas as pd

# %% Load Data 
cwd = os.getcwd()
filename = 'bugs.csv'
filepath = os.path.join(cwd, filename)
df = pd.read_csv(filepath)

# %% Function
def bug_classification(df):

    # Creates a new column called 'BugTypes' in order to classify the responses
    # according to which bug type condition the participant is responding
    """
    Bug type classifications created based on disgust and fear conditions.
    Conditions: high fear or low fear, high disgust or low disgust.
    Bug types: 
        1 = low disgust/low fear
        2 = low disgust/high fear 
        2 = high disgust/low fear
        4 = high disgust/high fear
    If new bug type conditions are added to the file, the existing lines of code
    can be adapted to reflect this.
    >>> e.g. if a third column is added to bugs.csv denoting the condition color
        (either dark or light), the code could be adapted as follows:
    bugtype1 = low disgust, low fear, dark color
    df.loc[(df.Disgust == 'low') & (df.Fear == 'low') & (df.Color == 'dark'), 'BugType'] += 1
    bugtype2 = low disgust, low fear, light color
    df.loc[(df.Disgust == 'low') & (df.Fear == 'low') & (df.Color == 'light'), 'BugType'] += 2
        and so on.
    
    Changes will not be written back to the existing .csv file.
    Can be written back to the existing .csv file if needed:
    >>> df.to_csv(filepath, index=False)
    Can be written to the new dataframe (including BugType column) to a new file:
    >>> filename_new = 'bugs_w_type.csv'
    df.to_csv(filename_new, index = False)
    """
    df["BugType"] = 0  
    # Bugtype1 = low disgust, low fear
    df.loc[(df.Disgust == "low") & (df.Fear == "low"), "BugType"] += 1
    # Bugtype2 = low disgust, high fear
    df.loc[(df.Disgust == "low") & (df.Fear == "high"), "BugType"] += 2
    # Bugtype3 = high disgust, low fear
    df.loc[(df.Disgust == "high") & (df.Fear == "low"), "BugType"] += 3
    # Bugtype4 = high disgust, high fear
    df.loc[(df.Disgust == "high") & (df.Fear == "high"), "BugType"] += 4
    df.BugType = df.BugType.astype('category')
    return df

bug_classification(df)    