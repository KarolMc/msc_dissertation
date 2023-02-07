# -*- coding: utf-8 -*-
"""pca_feature_selected.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1j6VMGFcXGv_qldtVbi7lGHXN8CcqUMu0
"""

import joblib

import pandas as pd
import numpy as np

# Import SVC from sklearn.svm and accuracy_score from sklearn.metrics
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.model_selection import train_test_split, StratifiedKFold

from sklearn.preprocessing import StandardScaler
import xgboost as xgb
from sklearn.ensemble import RandomForestClassifier

from sklearn.pipeline import Pipeline

from sklearn.model_selection import GridSearchCV

from sklearn.model_selection import RandomizedSearchCV

from sklearn.metrics import make_scorer

import random

random_seed = random.seed(42)

from sklearn.preprocessing import LabelEncoder

from sklearn.metrics import accuracy_score, confusion_matrix

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report
import matplotlib.pyplot as plt

X_train = pd.read_csv('/content/drive/MyDrive/NHANES/file_files/X_train_multiselected.csv', index_col=[0])
y_train = pd.read_csv('/content/drive/MyDrive/NHANES/file_files/y_train_ROS.csv', index_col=[0])
X_test = pd.read_csv('/content/drive/MyDrive/NHANES/file_files/X_test_multiselected.csv', index_col=[0])
y_test = pd.read_csv('/content/drive/MyDrive/NHANES/file_files/y_test.csv', index_col=[0])

train_features = X_train.columns

from google.colab import drive
drive.mount('/content/drive')

diabetes_data = X_train

diabetes_data.head()

diabetes_labels = y_train

diabetes_labels.head()

diabetes_training_data = pd.concat([diabetes_data, diabetes_labels], axis = 1)

diabetes_training_data.shape

diabetes_training_data.head()

diabetes_training_data['Diabetes_status'].value_counts()

normal_training_data_df = diabetes_training_data[diabetes_training_data['Diabetes_status'] == 1]
prediabetes_training_data_df = diabetes_training_data[diabetes_training_data['Diabetes_status'] == 2]
diabetes_training_data_df = diabetes_training_data[diabetes_training_data['Diabetes_status'] == 3]

# import libraries
import matplotlib.pyplot as plt
import seaborn as sns

# set figure size
plt.figure(figsize=(2^15, 2^15))

# Generate a mask to onlyshow the bottom triangle
mask = np.triu(np.ones_like(normal_training_data_df.corr(), dtype=bool))

# generate heatmap
sns_plt = sns.heatmap(normal_training_data_df.corr(), annot=False, mask=mask, vmin=-1, vmax=1, cmap = 'coolwarm')
plt.title('Correlation Coefficient Of Predictors: Normal Diabetes Status')
plt.show()

# set figure size
plt.figure(figsize=(2^15, 2^15))

# Generate a mask to onlyshow the bottom triangle
mask = np.triu(np.ones_like(prediabetes_training_data_df.corr(), dtype=bool))

# generate heatmap
sns_plt = sns.heatmap(prediabetes_training_data_df.corr(), annot=False, mask=mask, vmin=-1, vmax=1, cmap = 'coolwarm')
plt.title('Correlation Coefficient Of Predictors: Prediabetes Diabetes Status')
plt.show()

# set figure size
plt.figure(figsize=(2^15, 2^15))

# Generate a mask to onlyshow the bottom triangle
mask = np.triu(np.ones_like(diabetes_training_data_df.corr(), dtype=bool))

# generate heatmap
sns_plt = sns.heatmap(diabetes_training_data_df.corr(), annot=False, mask=mask, vmin=-1, vmax=1, cmap = 'coolwarm')
plt.title('Correlation Coefficient Of Predictors: Diabetes Diabetes Status')
plt.show()

correlation = diabetes_training_data.corr()

mask = correlation.columns[:-1]

exclude = correlation.drop(mask)

exclude.transpose()

exclude.apply(pd.to_numeric)

exclude.style.background_gradient(cmap='coolwarm', axis = 1)

features = list(diabetes_training_data.columns)

from sklearn.preprocessing import StandardScaler
x = diabetes_training_data.loc[:, features].values
x = StandardScaler().fit_transform(x) # normalizing the features

x.shape

np.mean(x),np.std(x)

feat_cols = ['feature'+str(i) for i in range(x.shape[1])]

normalised_diabetes = pd.DataFrame(x,columns=feat_cols)

normalised_diabetes.tail()

from sklearn.decomposition import PCA
pca_diabetes = PCA(n_components=10)
principalComponents_diabetes = pca_diabetes.fit_transform(x)

principal_diabetes_Df = pd.DataFrame(data = principalComponents_diabetes
             , columns = ['principal component 1', 'principal component 2', 'principal component 3', 'principal component 4',
                         'principal component 5', 'principal component 6', 'principal component 7', 'principal component 8',
                         'principal component 9', 'principal component 10'])

principal_diabetes_Df.head()

print('Explained variation per principal component: {}'.format(pca_diabetes.explained_variance_ratio_))

PCA(copy=True, iterated_power='auto', n_components=0.9, random_state=None,
  svd_solver='auto', tol=0.0, whiten=False)

from sklearn.decomposition import PCA
diabetes_pca = PCA(n_components = 10)
components = diabetes_pca.fit(x).components_
components = pd.DataFrame(components).transpose()
components.columns = ['Comp1', 'Comp2', 'Comp3', 'Comp4', 'Comp5', 'Comp6', 'Comp7', 'Comp8', 'Comp9', 'Comp10']
#components.index =  x_train.columns
print(components)

var_ratio = diabetes_pca.explained_variance_ratio_
var_ratio= pd.DataFrame(var_ratio).transpose()
var_ratio.columns = ['Comp1', 'Comp2', 'Comp3', 'Comp4', 'Comp5', 'Comp6', 'Comp7', 'Comp8', 'Comp9', 'Comp10']

var_ratio.index = ['Proportion of Variance']
print(var_ratio)

PC_values = np.arange(diabetes_pca.n_components_) + 1
plt.plot(PC_values, diabetes_pca.explained_variance_ratio_, 'o-', linewidth=2, color='blue')
plt.title('Scree Plot')
plt.xlabel('Principal Component')
plt.ylabel('Variance Explained')
plt.show()

diabetes_pcomp = diabetes_pca.fit_transform(x)
diabetes_pcomp = pd.DataFrame(diabetes_pcomp)
diabetes_pcomp = diabetes_pcomp.iloc[:,0:6]
diabetes_pcomp.columns = ['Comp1', 'Comp2', 'Comp3', 'Comp4', 'Comp5', 'Comp6']
print(diabetes_pcomp.head())

import seaborn as sns

diabetes_pcomp.shape

diabetes_pcomp['y'] = y_train

imaging_comp = diabetes_pcomp[['Comp1', 'Comp2', 'y']]

sns.set_style("darkgrid")

plt.figure(figsize=(16,10))
sns.scatterplot(
    x="Comp1", y="Comp2",
    hue="y",
    palette=sns.color_palette("hls", 3),
    data=imaging_comp,
    legend="full",
    alpha=0.3
)

normal_df = diabetes_pcomp[diabetes_pcomp['y'] == 1]
prediabetes_df = diabetes_pcomp[diabetes_pcomp['y'] == 2]
diabetes_df = diabetes_pcomp[diabetes_pcomp['y'] == 3]

from mpl_toolkits.mplot3d import Axes3D

sns.set(style = "darkgrid")

colors=['orangered', 'lightgreen', 'slateblue'] 
fig = plt.figure(figsize=(14,14))
ax = fig.add_subplot(111, projection = '3d')

p1 = ax.plot(normal_df['Comp1'],
                normal_df['Comp2'],  
             normal_df['Comp3'], 
             'o', color=colors[0],                                              
             alpha = 0.6, label='Normal',                        
             markersize=3, 
             markeredgecolor='black',
             markeredgewidth=0.1)

p2 = ax.plot( prediabetes_df['Comp1'],prediabetes_df['Comp2'],
             prediabetes_df['Comp3'], 
             'o', color=colors[1],                                     
             alpha = 0.6, label='Prediabetes',                            
             markersize=3, 
             markeredgecolor='black',
             markeredgewidth=0.1)


p2 = ax.plot( diabetes_df['Comp1'],diabetes_df['Comp2'], 
             diabetes_df['Comp3'], 
             'o', color=colors[2],                                                
             alpha = 0.6, label='Diabetes',                            
             markersize=3, 
             markeredgecolor='black',
             markeredgewidth=0.1)



ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.set_zlabel("PC3")

fig.legend(fontsize = 'x-small', loc='upper center', markerscale=2)
plt.autoscale()
plt.rcParams["figure.dpi"] = 1000                                 
plt.show()



# Incremental PCA

from sklearn.decomposition import IncrementalPCA

transformer = IncrementalPCA(n_components = 10, batch_size = 200)

incrementalPCA_Diabetes = transformer.fit(X_train)

components = incrementalPCA_Diabetes.components_
components = pd.DataFrame(components).transpose()
components.columns = ['Comp1', 'Comp2', 'Comp3', 'Comp4', 'Comp5', 'Comp6', 'Comp7', 'Comp8', 'Comp9', 'Comp10']
#components.index =  x_train.columns
print(components)

var_ratio = incrementalPCA_Diabetes.explained_variance_ratio_
var_ratio= pd.DataFrame(var_ratio).transpose()
var_ratio.columns = ['Comp1', 'Comp2', 'Comp3', 'Comp4', 'Comp5', 'Comp6', 'Comp7', 'Comp8', 'Comp9', 'Comp10']

var_ratio.index = ['Proportion of Variance']
print(var_ratio)

PC_values = np.arange(incrementalPCA_Diabetes.n_components_) + 1
plt.plot(PC_values, incrementalPCA_Diabetes.explained_variance_ratio_, 'o-', linewidth=2, color='blue')
plt.title('Scree Plot')
plt.xlabel('Principal Component')
plt.ylabel('Variance Explained')
plt.show()

diabetes_pinccomp = incrementalPCA_Diabetes.fit_transform(x)
diabetes_pinccomp = pd.DataFrame(diabetes_pinccomp)
diabetes_pinccomp = diabetes_pinccomp.iloc[:,0:3]
diabetes_pinccomp.columns = ['Comp1', 'Comp2', 'Comp3']
print(diabetes_pinccomp.head())

diabetes_pinccomp['y'] = y_train

imaging_comp = diabetes_pinccomp[['Comp1', 'Comp2', 'y']]

plt.figure(figsize=(16,10))
sns.scatterplot(
    x="Comp1", y="Comp2",
    hue="y",
    palette=sns.color_palette("hls", 3),
    data=imaging_comp,
    legend="full",
    alpha=0.3
)

normal_i_df = diabetes_pinccomp[diabetes_pinccomp['y'] == 1]
prediabetes_i_df = diabetes_pinccomp[diabetes_pinccomp['y'] == 2]
diabetes_i_df = diabetes_pinccomp[diabetes_pinccomp['y'] == 3]

from mpl_toolkits.mplot3d import Axes3D

sns.set(style = "darkgrid")

colors=['orangered', 'lightgreen', 'slateblue']  
fig = plt.figure(figsize=(16,16))
ax = fig.add_subplot(111, projection = '3d')

p1 = ax.plot(normal_i_df['Comp1'],
                normal_i_df['Comp2'],  
             normal_i_df['Comp3'], 
             'o', color=colors[0],                                                 
             alpha = 0.6, label='Normal',                            
             markersize=3, 
             markeredgecolor='black',
             markeredgewidth=0.1)

p2 = ax.plot( prediabetes_i_df['Comp1'],prediabetes_i_df['Comp2'],
             prediabetes_i_df['Comp3'], 
             'o', color=colors[1],                                                
             alpha = 0.6, label='Prediabetes',                            
             markersize=3, 
             markeredgecolor='black',
             markeredgewidth=0.1)


p2 = ax.plot( diabetes_i_df['Comp1'],diabetes_i_df['Comp2'], 
             diabetes_i_df['Comp3'], 
             'o', color=colors[2],                                                
             alpha = 0.6, label='Diabetes',                            
             markersize=3, 
             markeredgecolor='black',
             markeredgewidth=0.1)



ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.set_zlabel("PC3")

fig.legend(fontsize = 'x-small', loc='upper center', markerscale=2)
plt.autoscale()
plt.rcParams["figure.dpi"] = 1000                                   
plt.show()

# correlations

# import libraries
import matplotlib.pyplot as plt
import seaborn as sns

# set figure size
plt.figure(figsize=(2^15, 2^15))

# Generate a mask to onlyshow the bottom triangle
mask = np.triu(np.ones_like(diabetes_training_data.corr(), dtype=bool))

# generate heatmap
sns_plt = sns.heatmap(diabetes_training_data.corr(), annot=False, mask=mask, vmin=-1, vmax=1, cmap = 'coolwarm')
plt.title('Correlation Coefficient Of Predictors')
plt.show()

plt.savefig('saving-a-high-resolution-seaborn-plot.png', dpi=300)







!pip install statsmodels

# load statmodels functions
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant

# compute the vif for all given features
def compute_vif(considered_features):
    
    X = diabetes_training_data[considered_features]
    # the calculation of variance inflation requires a constant
    X['intercept'] = 1
    
    # create dataframe to store vif values
    vif = pd.DataFrame()
    vif["Variable"] = X.columns
    vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    vif = vif[vif['Variable']!='intercept']
    return vif

vifs_df = compute_vif(features)

vif_df = vifs_df.sort_values(by=['VIF'], ascending = False)
inf_vif_df = vif_df.loc[vif_df['VIF']== np.inf]

# inf_vif_df
# vif_df = vif_df.replace([np.inf, -np.inf], np.nan, inplace=True)
# vif_df.head()
# vif_df = vif_df.dropna(subset=["VIF"], how="all", inplace=True)
# vif_df = vif_df[vif_df.VIF < inf]
vif_df.head(30)

# Feature selection

from sklearn.feature_selection import chi2, f_classif, mutual_info_classif

from sklearn.feature_selection import SelectKBest, SequentialFeatureSelector, RFE

!pip install lightgbm

import lightgbm

lgbm = joblib.load('lgbm_tuned.joblib')

estimator = lgbm
selectior = RFE(lgbm, n_features_to_select = 0.3, step = 1)

le = LabelEncoder()
y_train = le.fit_transform(y_train)

y_test = le.fit_transform(y_test)

X_train_val, X_validation, y_train_val, y_validation = train_test_split(X_train, y_train, test_size=0.25)

training_data = {'X_train':X_train_val,'y_train':y_train_val,
                'X_val': X_validation,'y_val':y_validation,
                'X_test': X_test,'y_test':y_test}

selector = selectior.fit(training_data['X_train'].values, training_data['y_train'], 
          eval_set=[(training_data['X_train'].values, training_data['y_train']), (training_data['X_val'].values, training_data['y_val'])],
          verbose=10)

lgbm_mask = selector.support_

reduced_X = X_train.loc[:, lgbm_mask]

len(reduced_X.columns)

RFE_features = list(reduced_X.columns)

RFE_features

# Feature Selection with Select K Best

lgbm_model = estimator.fit(training_data['X_train'].values, training_data['y_train'], 
          eval_set=[(training_data['X_train'].values, training_data['y_train']), (training_data['X_val'].values, training_data['y_val'])])

len(lgbm_model.feature_importances_)

len(X_train.columns)

lgbm_features = pd.DataFrame()
lgbm_features['feature'] = X_train.columns

lgbm_features['importance'] = lgbm_model.feature_importances_

lgbm_features = lgbm_features.sort_values(by=['importance'], ascending = False)

lgbm_features = lgbm_features[lgbm_features['importance']>= 400]
lgbm_features.shape

importances_cols = lgbm_features['feature'].to_list()

from sklearn.feature_selection import SelectKBest, chi2
# Create and fit selector

selector = SelectKBest(f_classif, k=51)

selector.fit(X_train, y_train)
# Get columns to keep and create new dataframe with those only
cols = selector.get_support(indices=True)
features_df_f_classif = X_train.iloc[:,cols]

features_df_f_classif.head()

f_classif_cols = features_df_f_classif.columns
len(f_classif_cols)

# Create and fit selector

selector = SelectKBest(chi2, k=51)
selector.fit(X_train, y_train)
# Get columns to keep and create new dataframe with those only

cols = selector.get_support(indices=True)

features_df_chi2 = X_train.iloc[:,cols]

chi2_cols = features_df_chi2.columns
len(chi2_cols)

from collections import Counter
from itertools import chain

feature_lists = [RFE_features, importances_cols, f_classif_cols, chi2_cols]

no_of_lists_per_name = Counter(chain.from_iterable(map(set, feature_lists)))

for name, no_of_lists in no_of_lists_per_name.most_common():
    if no_of_lists == 1:
        break # since it is ordered by count, once we get this low we are done\n",
    print(f"'{name}' is in {no_of_lists} lists")

sets = [set(names) for names in feature_lists]
feature_set = list(sets[0].union(sets[1], sets[2], sets[3]))

len(feature_set)





X_train_Sselected = X_train[features]

X_test_Sselected = X_test[features]

X_train_Sselected.to_csv('/Users/karolmccaul/Documents/Uni_of_Bath/research_project/vs_code/resampled_data/X_train_Sselected.csv')

X_test_Sselected.to_csv('/Users/karolmccaul/Documents/Uni_of_Bath/research_project/vs_code/resampled_data/X_test_Sselected.csv')

