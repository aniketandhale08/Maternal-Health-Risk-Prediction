
# Maternal Health Risk Prediction

## Overview

This project aims to predict the maternal health risk level of pregnant women based on various health indicators. The dataset contains information on features like age, blood pressure, blood sugar levels, heart rate, and more. The primary goal is to classify the risk level as `Low Risk`, `Mid Risk`, or `High Risk`.

## Dataset Description

The dataset used in this project is the **Maternal Health Risk Data Set**. It contains 1014 entries and 7 features. The dataset is used to predict the health risk level for pregnant women.

### Features:
- **Age**: Age of the woman
- **SystolicBP**: Systolic Blood Pressure (mmHg)
- **DiastolicBP**: Diastolic Blood Pressure (mmHg)
- **BS**: Blood Sugar levels (mmol/L)
- **BodyTemp**: Body Temperature (°C)
- **HeartRate**: Heart rate (bpm)
- **RiskLevel**: Target variable (Low Risk, Mid Risk, High Risk)

## Project Workflow

1. **Data Preprocessing**: Loaded the dataset, cleaned the data, and handled missing values.
2. **Exploratory Data Analysis (EDA)**: Analyzed the dataset to understand the distribution of features and their relation to the target variable.
3. **Feature Engineering**: Dealt with outliers and selected important features for modeling.
4. **Modeling**: Trained multiple classification models to predict the risk level and evaluated their performance.
5. **Model Deployment**: Tuned the best model and saved it for future use.

## Exploratory Data Analysis

- **Univariate Analysis**: Explored the distribution of individual features like Age, Blood Pressure, and Heart Rate.
- **Bivariate Analysis**: Investigated the relationships between features and the target variable.
- **Correlation Plot**: Created a heatmap to analyze multicollinearity between features.

## Feature Engineering

1. **Outlier Detection**: Removed extreme outliers, specifically from the Heart Rate column.
2. **Feature Selection**: Dropped less useful features (e.g., HeartRate) after analysis.

## Modeling

Multiple models were tested using **train_test_split** and cross-validation. The classifiers used include:
- Random Forest
- AdaBoost
- Decision Tree
- K-Nearest Neighbors
- XGBoost
- Naive Bayes
- Support Vector Classifier (SVC)

**Random Forest** with hyperparameter tuning was chosen as the best-performing model.

### Hyperparameter Tuning

- Grid search was used to find the optimal hyperparameters for the RandomForestClassifier.
- Best parameters found:
  - `n_estimators`: 50
  - `criterion`: gini

### Final Model Accuracy
- **Base Model Accuracy**: 0.93
- **Tuned Model Accuracy**: 0.95


## Usage

1. Clone the repository:

```bash
git clone <repository-link>
```

2. Install the required libraries:

```bash
pip install -r requirements.txt
```

3. Run the model:

```python
streamlit run app.py
```

## Conclusion

This project demonstrates the prediction of maternal health risks using machine learning techniques. The RandomForestClassifier showed the best performance after hyperparameter tuning, and the model was saved for deployment.
