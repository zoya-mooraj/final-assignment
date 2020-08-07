# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 22:37:36 2020

@author: ZOYA
"""

import pycodestyle
import ast
import traceback

# %% Check style of bugs_analysis.py
fchecker = pycodestyle.Checker('bugs_analysis.py', show_source=True)
file_errors = fchecker.check_all()
print("Found %s errors (and warnings)" % file_errors)        


# %% Check syntax of bugs_analysis.py
filename = 'bugs_analysis.py'
with open(filename) as f:
    source = f.read()
valid = True
try:
    ast.parse(source)
except SyntaxError:
    valid = False
    traceback.print_exc()  # Remove to silence any errros
print(valid)