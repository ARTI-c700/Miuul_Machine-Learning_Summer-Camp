from Feature_Engineering.Required_Packages import *
from Feature_Engineering.Outliers.Acquisition_of_Functioning_1 import *

# An outlier can depend on two or more variables
# For example, A person aged 17 married 3 times.

####################################################
# Applying LOF method
####################################################

dataframe = sns.load_dataset('diamonds')
dataframe = dataframe.select_dtypes(include=['float64', 'int64'])
dataframe = dataframe.dropna()
dataframe.head()

for col in dataframe.columns:
    print(f"{col} : {check_outlier(dataframe, col)}")

low, up = outlier_thresholds(dataframe, 'carat')

dataframe[(dataframe['carat'] < low) | (dataframe['carat'] > up)].shape


low, up = outlier_thresholds(dataframe, 'depth')

dataframe[(dataframe['depth'] < low) | (dataframe['depth'] > up)].shape


clf = LocalOutlierFactor(n_neighbors=20)
clf.fit_predict(dataframe)

df_scores = clf.negative_outlier_factor_
df_scores[0:5]

# df_scores = -df_scores

np.sort(df_scores)[:5]

##################################
# graphic method (elbow method)

scores = pd.DataFrame(np.sort(df_scores))
scores.plot(stacked=True, xlim=[0, 50], style='.-')
plt.show()

threshold = np.sort(df_scores)[3]

dataframe[df_scores < threshold]
