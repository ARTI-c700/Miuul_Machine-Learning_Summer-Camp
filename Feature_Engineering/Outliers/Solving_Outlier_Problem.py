import pandas as pd
from Feature_Engineering.Outliers.Acquisition_of_Functioning_1 import *
from Feature_Engineering.Outliers.Getting_Outlier_Values import *
from Feature_Engineering.Outliers.Acquisition_of_Functioning_2 import *
from Feature_Engineering.Required_Packages import *

#####################################
# Removing

low, up = outlier_thresholds(load_titanic(), "Fare")
df = load_titanic()

total_shape = load_titanic().shape

# outliers, index = show_outliers_and_indexes(df, "Fare")
are_outliers = df[(df["Fare"] < low) | (df["Fare"] > up)]
are_outliers.shape

not_outliers = df[~((df["Fare"] < low) | (df["Fare"] > up))]
shape = df[~((df["Fare"] < low) | (df["Fare"] > up))].shape


# If we want to detect all outliers from all variables:
# (FUNCTION)

def remove_outlier(dataframe, column_name):
    low_limit, up_limit = outlier_thresholds(dataframe, column_name)
    return dataframe[~((dataframe[column_name] < low_limit) | (dataframe[column_name] > up_limit))]


cat, num, cat_in_num, car_in_cat = grab_col_names(df)
num = [column for column in num if column not in "PassengerId"]

new_df = pd.DataFrame()

for col in num:
    new_df = remove_outlier(df, col)

show_outliers_and_indexes(new_df, "Age")
show_outliers_and_indexes(df, "Age")
for col in num:
    print(f"{col} : {check_outlier(new_df, col)}")

################################################################################
# Problem in the function "remove_outlier()"

# Issue: In the same dataframe there is different outliers based on different variables
# In the cleaning (or removing) process each variable can require the cleaning of different rows
# As a result, there should be used an integration of all results based on their variables

""" Declaring DataFrame using Lists (required)
import pandas as pd
 
# initialize list of lists
data = [['tom', 10], ['nick', 15], ['juli', 14]]
 
# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age'])
 
# print dataframe.
print(df)

"""

""" Declaring DataFrame using

def generate_dataframe(dataframe, cols):
    iframes = []
    i2frames = []

    for col in cols:
        iframes = iframes + list((remove_outlier(dataframe, col)).values)

    for els in iframes:
        els = list(els)
        i2frames.append(els)

    for els in i2frames:
        if i2frames.count(els) > 1:
            i2frames.remove(els)

    for els in cols:
        low1, up1 = outlier_thresholds(dataframe, els)
        i2frames = [els for els in i2frames if ]

    new_dataframe = pd.DataFrame(i2frames, columns=list(dataframe.columns))
    return new_dataframe


iframes = []
i2frames = []

for col in num:
    iframes = iframes + list((remove_outlier(df, col)).values)

for els in iframes:
    els = list(els)
    i2frames.append(els)


for el in i2frames:
    print(el)
    if iframes.count(el) > 1:
        print(el)
    else:
        print("-------------------------------------")

"""