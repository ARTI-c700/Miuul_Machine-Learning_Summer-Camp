from Feature_Engineering.Required_Packages import *

#################################################
# Cathing Outliers
######
# using histogram
sns.boxplot(x=load_titanic()["Age"])
plt.show()

# Using different techniques
up_limit = load_titanic()["Age"].quantile(0.75) + 1.5*(
    load_titanic()["Age"].quantile(0.75) - load_titanic()["Age"].quantile(0.25)
)

low_limit = load_titanic()["Age"].quantile(0.25) - 1.5*(
    load_titanic()["Age"].quantile(0.75) - load_titanic()["Age"].quantile(0.25)
)

load_titanic()[ (df["Age"] > up_limit) | (df["Age"] < low_limit)]

type(load_titanic()["Age"] > up_limit)
type(load_titanic()[ (load_titanic()["Age"] > up_limit) | (load_titanic()["Age"] < low_limit)])

# Indexes of Outliers
load_titanic()[ (load_titanic()["Age"] > up_limit) | (load_titanic()["Age"] < low_limit)].index

# If we want to learn about having any outlier or not in a data
load_titanic()[(load_titanic()["Age"] > up_limit) | (load_titanic()["Age"] < low_limit)].any(axis=None)

#########################################
# Result:
# Identified a threshold
# Found outliers
# Asked about having any outlier or not
#########################################

