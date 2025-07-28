
# Life Expectancy Prediction using Machine Learning

This project builds machine learning models to predict life expectancy of countries using health, demographic, and economic indicators. It includes exploratory data analysis, model development, evaluation, and deployment using Streamlit.

## Project Overview

The objective is to understand the influence of various features such as BMI, schooling, GDP, and immunization on life expectancy and build predictive models.

## Dataset

- Source: WHO data (processed)
- Target variable: Life Expectancy
- Features include:
  - Adult Mortality
  - Infant Deaths
  - Alcohol Consumption
  - BMI
  - GDP
  - Schooling
  - HIV/AIDS prevalence
  - Immunization Coverage

## Workflow

1. Data Loading and Cleaning
2. Exploratory Data Analysis (EDA)
3. Feature Engineering and Preprocessing
4. Model Building (Linear, Polynomial, Tree-based, SVR)
5. Hyperparameter Tuning with GridSearchCV
6. Cross-Validation and Evaluation
7. Model Saving using Pickle
8. Web App Interface with Streamlit

## Model Performance Summary

| Model                   | R² (Train) | R² (Test) | MAE (Train) | MAE (Test) |
|------------------------|------------|-----------|-------------|------------|
| Linear Regression       | 0.802      | 0.771     | 4.10        | 4.23       |
| Lasso Regression        | 0.802      | 0.771     | 4.10        | 4.24       |
| Polynomial Regression   | 0.899      | 0.862     | 3.02        | 3.53       |
| Decision Tree Regressor| 0.969      | 0.931     | 2.86        | 5.42       |
| SVR (RBF Kernel)        | 0.970      | 0.916     | 2.78        | 6.64       |
| Random Forest Regressor| 0.972      | 0.952     | 2.61        | 3.82       |

Best Model: **Random Forest Regressor** with highest R² and lowest test MAE.

## Saving Model

The final model is saved using Pickle:
```python
import pickle
with open("best_model.pkl", "wb") as f:
    pickle.dump(model, f)
```

## Streamlit App

A simple Streamlit interface is created to load the model and take user input.

To run the app, execute this in the terminal:
```
streamlit run streamlit_app.py
```

## Folder Structure

```
Life_Expectancy_Project/
├── Life expectancy project.ipynb
├── streamlit_app.py
├── best_model.pkl
├── README.md
└── dataset.csv
```

## Future Scope

- Incorporate XGBoost or LightGBM
- Add explainability with SHAP
- REST API deployment with Flask or FastAPI

## Author

Aman Singh Parihar
MSc Statistics  
Email: amanparihar.bhu.stats26@gmail.com
GitHub: https://github.com/amanparihar27
