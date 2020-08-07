"""
=============================
Python Assignment - Zoya Mooraj
=============================

A script to analyze data from 'bugs.csv'

"""

# %% Packages
import os
from matplotlib import pyplot
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf
from bug_classification import bug_classification

# %% Helper function

def print_section(content, title):
    """
    Seperate output into sections with title.
    """
    header = "#### {} ####".format(title)
    print(header, content, sep="\n\n", end="\n\n\n")



# %% Load Data

cwd = os.getcwd()
filename = "bugs.csv"
filepath = os.path.join(cwd, filename)
df = pd.read_csv(filepath)

print_section(df, "Data frame")



# %% Create BugType Column

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
df = bug_classification(df)    

print_section(df, "Data frame with Bug Type")



# %% Summaries

# Mean desire to kill rating, irrespective of bug condition
mean_kr = np.mean(df["KillRating"])
print_section(round(mean_kr, 2), "Mean Kill Rating Accross all Bug Types")

# Summary statistics (minimum, maximum, mean, median and standard deviation)
# For desire to kill according to bug type
summary_stats = [min, max, np.mean, np.median, np.std]
summary = df.groupby("BugType").aggregate({"KillRating": summary_stats})
print_section(round(summary, 2), "Kill Ratings Per Bug Type")

# For desire to kill according to sex
summary = df.groupby("Sex").aggregate({"KillRating": summary_stats})
print_section(round(summary, 2), "Kill Ratings Per Participants' Sex")



# %% Linear Model

"""
OLS linear regression model
Does bug type serve as a predictor for desire to kill?
Outcome variable = KillRating
Predictor variable = BugType

Whether the difference is statistically significant can be seen from the p-value,
shown under the column labeled P>|t|.

If the p-value is significant according to the defined threshold (0.05), there 
is evidence of a linear association between the variables 'BugType' and 
'KillRating'.
"""


# Main proposed model
# OLS Regression Model
formula_linear = "KillRating ~ BugType"
m_linear = smf.ols(formula_linear, data=df).fit()
print_section(m_linear.summary(), "Model: " + formula_linear)


# Reporting OLS Regression Model Results
# Intercept and Slope
r_params = round(m_linear.params, 2)
print_section(r_params, "Regression Paramaters")


# Standard Errors
r_se = m_linear.bse
print_section(m_linear.bse, "Standard errors ")


# p-value
# from regression output
p_values = round(m_linear.pvalues, 4)
print_section(p_values, "p-value")


# R-squared Value
"""
Percentage variation in outcome variable (KillRating) that is explained by the 
predictor variable (BugType) 
Higher value = better the explainability of the model
"""
# r-squared value
# from regression output
rsquared = round(m_linear.rsquared, 2)
rsquared_percentage = "{:.0%}".format(rsquared)
print_section(rsquared, "R-Squared Value")
print("The R-squared value of", rsquared, "implies that", rsquared_percentage,
    "of the variation in the variable 'KillRating' is explained by the variable" 
    "'BugType'", end="\n\n\n")


# Predictions based on model
prediction1 = m_linear.predict({"BugType": 1})
prediction2 = m_linear.predict({"BugType": 2})
prediction3 = m_linear.predict({"BugType": 3})
prediction4 = m_linear.predict({"BugType": 4})

predictions = [
    {"Bug Type 1 Prediction": prediction1},
    {"Bug Type 2 Prediction": prediction2},
    {"Bug Type 3 Prediction": prediction3},
    {"Bug Type 4 Prediction": prediction4},
]

print_section(predictions, "Model Predictions for Kill Rating per Bug Type")


# Plot
sns.lmplot(x="BugType", y="KillRating", data=df)
pyplot.xlabel("BugType")
pyplot.ylabel("KillRating")
pyplot.show()



# %% Plot
# To visualize the desire to kill as a function of fear and disgust

# Style
sns.set(style="darkgrid", palette="muted")
pyplot.figure(figsize=(10, 10))


# Boxplot
# x axis = 'Disgust', y axis = 'KillRatings' (labelled as desire to kill)
# hue = fear (to discern between low fear and high fear conditions)
ax = sns.boxplot(x="Disgust", y="KillRating", hue="Fear", palette=["r", "c"], data=df)

# Stripplot
# to visualize distribution of kill rating for each condition
sp = sns.stripplot(
    x="Disgust",
    y="KillRating",
    hue="Fear",
    dodge=True,
    marker="o",
    alpha=1,
    palette=["r", "c"],
    linewidth=1,
    data=df,
)
# Title
pyplot.title("Distribution of Kill Ratings for Each Bug Condition")

# Axes labels
pyplot.ylabel("Desire to Kill")
pyplot.xlabel("Disgust")

# Customize legend
pyplot.legend(loc="center left", bbox_to_anchor=(1, 0.5), frameon=False, title="Fear")

# Customize ticks
ax.tick_params(left=True, bottom=True, direction="out", length=3, width=1)
pyplot.yticks(np.arange(0, 11, step=1))

# Save plot figure
pyplot.savefig("bugs.png")
pyplot.savefig("bugs.svg")

# TODO:  join the legend entries
# TODO: which saving format better


# %% Plot
# To visualize desire to kill as a function of bug type and gender

# Style
sns.set(style="darkgrid", palette="muted")
pyplot.figure(figsize=(10, 10))


# Barplot
# x axis = 'BugType, y axis = 'KillRatings' (labelled as desire to kill)
# hue = fear (to discern between the low fear and high fear conditions)
ax = sns.barplot(x="BugType", y="KillRating", hue="Sex", palette=["r", "c"], data=df)

# Title
pyplot.title("Desire to Kill for Each Bug Type according to Participant's Sex")

# Axes labels
pyplot.ylabel("Desire to Kill")
pyplot.xlabel("Bug Type")

# Customize legend
pyplot.legend(loc="center left", bbox_to_anchor=(1, 0.5), frameon=False, title="Gender")

# Customize ticks
ax.tick_params(left=True, bottom=True, direction="out", length=3, width=1)
pyplot.yticks(np.arange(0, 11, step=1))
positions = (0, 1, 2, 3)
labels = (
    "Low Disgust/Low Fear",
    "Low Disgust/High Fear",
    "High Disgust/Low Fear",
    "High Disgust/HighFear",
)
pyplot.xticks(positions, labels)

# Save plot figure
pyplot.show


