from Feature_Engineering.Outliers.Acquisition_of_Functioning_1 import *
from Feature_Engineering.Required_Packages import *

# grab_col_names

# Functionalities Categorical, Numeric, Seems categorical but cardinal variables (or column names) In Categorical
# variables there are also numeric variables in which main functionality is based from categorical concepts

res = [cols for cols in load_titanic() if load_titanic()[cols].dtypes != "O"]
load_titanic().head()


def grab_col_names(dataframe, cat_th=10, car_th=20):
    categorical_cols = [cols for cols in dataframe.columns if dataframe[cols].dtypes == "O"]
    numeric_cols = [cols for cols in dataframe.columns if dataframe[cols].dtypes != "O"]

    only_cardinal_in_cat = [
        cols for cols in dataframe.columns
        if dataframe[cols].nunique() > car_th and dataframe[cols].dtypes == "O"
    ]
    only_categorical_in_num = [
        cols for cols in dataframe.columns
        if dataframe[cols].nunique() < cat_th and dataframe[cols].dtypes != "O"
    ]

    categorical_cols = [
        cols for cols in categorical_cols
        if cols not in only_cardinal_in_cat
    ]

    categorical_cols = categorical_cols + only_categorical_in_num
    numeric_cols = [cols for cols in numeric_cols if cols not in only_categorical_in_num]

    print(f"Observation: {dataframe.shape[0]}")
    print(f"Variables(columns): {dataframe.shape[1]}")
    print(f"cat_cols: {len(categorical_cols)}")
    print(f"num_cols: {len(numeric_cols)}")
    print(f"cat_but_car: {only_cardinal_in_cat}")
    print(f"num_but_cat: {only_categorical_in_num}")

    return categorical_cols, numeric_cols, only_categorical_in_num, only_cardinal_in_cat


##############################################
# (additional) Checking having outliers or not
# cat_cols, num_cols, num_but_cat, cat_but_car = grab_col_names(load_application_train())

cat_cols, num_cols, num_but_cat, cat_but_car = grab_col_names(load_titanic())
num_cols = [column for column in num_cols if column != "PassengerId"]

outliers, indexes = show_outliers_and_indexes(load_titanic(), num_cols)

# 1 #
for column in num_cols:
    outliers, indexes = show_outliers_and_indexes(load_titanic(), column)
    print(f"{outliers[column]} ::\n {indexes}")
    print("--------------------------------------------------------------")


# 2 #
for column in num_cols:
    print(f"{column} : {check_outlier(load_titanic(), column)}")
    print(show_outliers_and_indexes(load_titanic(), column)[1])
