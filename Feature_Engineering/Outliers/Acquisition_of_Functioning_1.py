from Feature_Engineering.Required_Packages import *


#######################################################
# (FUNCTION) declaring thresholds for accepted variable
def outlier_thresholds(dataframe, col_name, qt1=0.25, qt3=0.75):
    q1 = dataframe[col_name].quantile(qt1)
    q3 = dataframe[col_name].quantile(qt3)
    iqr = q3 - q1
    low_limit = q1 - 1.5 * iqr
    upper_limit = q3 + 1.5 * iqr

    return low_limit, upper_limit


titanic_dataset = load_titanic()
# low, up = outlier_thresholds(titanic_dataset, "Age")


#################################
# Finding outliers from a dataset
# outliers = titanic_dataset[(titanic_dataset["Age"] < low) | (titanic_dataset["Age"] > up)]
# outlier_indexes = outliers.index


# applying function:
def show_outliers_and_indexes(dataframe, col_name, qt1=0.25, qt3=0.75):
    low, up = outlier_thresholds(dataframe, col_name, qt1, qt3)
    outliers = dataframe[(dataframe[col_name] < low) | (dataframe[col_name] > up)]
    outlier_indexes = outliers.index
    return outliers, outlier_indexes


#######################################################
# (FUNCTION) checking of having outliers in the dataset
def check_outlier(dataframe, col_name, qt1=0.25, qt3=0.75):
    low, up = outlier_thresholds(dataframe, col_name, qt1, qt3)
    # return dataframe[(dataframe[col_name] < low) | (dataframe[col_name] > up)].any(axis=None)
    result = dataframe[(dataframe[col_name] < low) | (dataframe[col_name] > up)].any(axis=None)
    if result:
        return True
    else:
        return False


check_outlier(titanic_dataset, "Age")  # (result) True
