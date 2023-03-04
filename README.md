# Using Artificial Intelligence to Predict Diabetes Status and Explain Risk Factors
Repository for Dissertation code/Data

This repository contains all the notebooks containing the code created for the research project and is intended to be reviewed in the following order: 

<img width="247" alt="image" src="https://user-images.githubusercontent.com/24702718/222908233-97c149e6-4089-4f81-b391-4849bb155581.png">

1.	Data collection and selection

NHANES data are available in individual SAS files from the Centers for Disease Control website, https://www.cdc.gov/nchs/nhanes/index.htm, which need to be converted into comma-separated value files for processing. Features not reproduced across the ten years of interest and data relating to examinations which were unlikely to have an impact on the models were removed. 

The notebooks for this work can be found at:
https://github.com/KarolMc/msc_dissertation/blob/main/step_1_lab_raw_data_input.ipynb and  
https://github.com/KarolMc/msc_dissertation/blob/main/step_1_exam_raw_dropped_data.ipynb 

Following the data selection, the dataset comprised 50,588 observations of 217 features to be cleaned.  (This data comprises a 40MB file so will not be uploaded)

2. Data cleaning: https://github.com/KarolMc/msc_dissertation/blob/main/step_3_data_cleaning.ipynb

Data cleaned to identify observations of interest, remove features with high missing values and fill missing values for the reamining. 


3.	Exploratory data analysis and feature selection: https://github.com/KarolMc/msc_dissertation/blob/main/feature_reduction.ipynb  
After selecting and cleaning the data, a target feature was to be constructed which would include the three categories of interest: whether a participant had normal markers for blood glucose and whether they had markers for prediabetes or diabetes. 

4. Resampling: https://github.com/KarolMc/msc_dissertation/blob/main/imbalance.ipynb

It is apparent that there was a significant imbalance across the three classes. 
This issue can be addressed using resampling methods, most often over- or under-sampling. 
At this point, I removed 30% of the observations to hold as a testing dataset. This was to ensure consistency across future experiments. I then carried out random oversampling, random under-sampling, SMOTE oversampling and combined over and under-sampling on the training data and assessed the performance of ML models (Decision Tree, Random Forest Classifier, XGBoost, Catboost and LightGBM) against this data. Although the results indicated that the improvement from resampling was modest, the best performance was with the dataset that had been subject to SMOTE oversampling. Therefore, this dataset was utilised for the next step in the project. 

5.	Dimensionality reduction and feature selection: https://github.com/KarolMc/msc_dissertation/blob/main/feature_selection.ipynb  

Selection through calculation of:  
	Variance Inflation Factor  
  Feature selection methods  
  Feature importances  
  Chi2 and ANOVA F-values  
  Recursive Feature Elimination (RFE)



  Visualising the data through dimensionality reduction: https://github.com/KarolMc/msc_dissertation/blob/main/PCA_and_correlations.ipynb 
  

6. Model selection: https://github.com/KarolMc/msc_dissertation/blob/main/model_selection.ipynb 

Comparing performance with the reduced dataset against several untuned models: 
	Decision Tree  
	Random Forest  
	Support Vector Classifier (One vs One)  
	Linear Support Vector Classifier  
	Multi-layer Perceptron Classifier  
	One vs Rest (MLP) Classifier  
	XGBoost  
	Catboost  
	LightGBM  


7. Model Tuning
  
  XGBoost: https://github.com/KarolMc/msc_dissertation/blob/main/XGBoost_tuning.ipynb  
  CatBoost: https://github.com/KarolMc/msc_dissertation/blob/main/catboost.ipynb  
  Light GBM: https://github.com/KarolMc/msc_dissertation/blob/main/lgbm.ipynb  
  TabNet: https://github.com/KarolMc/msc_dissertation/blob/main/tabnet_tuning.ipynb  
    
  Tuned model comparison: https://github.com/KarolMc/msc_dissertation/blob/main/tuned_model_comparison.ipynb  
  

8. Model evaluation and interpretation

Light GBM: https://github.com/KarolMc/msc_dissertation/blob/main/explaining_lgbm.ipynb

TabNet: https://github.com/KarolMc/msc_dissertation/blob/main/explaining_tabnet.ipynb

