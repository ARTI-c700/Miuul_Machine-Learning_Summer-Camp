from Feature_Engineering.Outliers.Acquisition_of_Functioning_1 import *
from Feature_Engineering.Outliers.Acquisition_of_Functioning_1 import *
from Feature_Engineering.Required_Packages import *

#####################################################################
# Finding the variables which hold outliers and solve these problems:
# 1) Exploring the outliers for specific variables
# 2) Getting index info (or not)
# 3) Having head() function when outlier values are more than e g 10


def grab_outliers(dataframe, column, index=False):
    outliers, outlier_indexes = show_outliers_and_indexes(dataframe, column)
    if outliers.shape[0] > 10:
        print(outliers.head())
    else:
        print(outliers)

    if index:
        return outlier_indexes


grab_outliers(load_titanic(), "Age")
grab_outliers(load_titanic(), "Age", True)
