# Inventory Leakage Restock Prediction
Detect silent stock losses · Forecast demand · Prevent stockouts for small businesses

## Problem Statement

A small business realized it was experiencing some inventory trouble it couldn't quite explain. Shelves that should have been full were running empty at unpredictable times, while stock counts at the end of the month never quite matched what should have been there. This pattern wasn't unique to one shop. Across small and medium sized enterprises (SMEs), particularly in the agrovet, retail, pharmacy, and electronics segments, businesses were routinely losing revenue to two interlinked problems: unexplained stock shrinkage and unpredictable stockouts.

The root cause became clear on closer inspection. These businesses typically lack the tooling that larger retailers use, such as demand forecasting or automated reorder triggers, and instead rely on manual stock counts and fixed reorder levels that don't adapt to product specific demand patterns or supplier lead times. Without a way to see patterns across products, categories, and time, owners were left reacting to problems after they happened rather than preventing them.

To explore how data analysis and machine learning could address this gap, I built a synthetic dataset engineered to reflect realistic SME operating conditions, including common real world data quality issues (missing values, inconsistent formatting, mixed date types), seasonal demand patterns, and category specific shrinkage behavior. The dataset was designed based on domain research rather than drawn from live business records, so the specific figures are illustrative, but the data cleaning challenges, feature engineering choices, and modeling approach reflect what a real analysis would require.

The analysis set out to answer three questions:

Where in the business do shrinkage and stockout risk concentrate?
Which measurable signals most reliably predict stockout risk?
Can a predictive model flag at risk products early enough to inform reorder decisions?

### Scope

The project covers the full analytical pipeline:

Data cleaning and standardization
Exploratory analysis using a structured 5W1H framework (who, what, when, where, why, how)
Feature engineering (rolling demand averages, shrinkage rates, days of stock remaining)
Model development, four classification models (Logistic Regression, Random Forest, XGBoost, LightGBM) trained and compared, with XGBoost selected as the best performer based on ROC-AUC (0.9993 on the held out test set)


### Project Structure
```
inventory-stock-analysis/
│
├── README.md                          # Problem statement, scope, key findings
├── requirements.txt                   # pandas, numpy, scikit-learn, xgboost, lightgbm, etc.
│
├── data/
│   ├── raw/
│   │   └── inventory_data.csv         # Original synthetic dataset (5,526 records)
│   ├── processed/
│   │   └── cleaned_inventory_data.csv # Post-cleaning, standardized dataset
│   └── data_dictionary.md             # Column definitions and units
│
├── notebooks/
│   └── inventory_stock_analysis.ipynb # Main analysis notebook (full pipeline)
│
├── src/
│   ├── data_cleaning.py               # Standardization, missing value handling
│   ├── feature_engineering.py         # Rolling averages, shrinkage rate, days-of-stock
│   ├── eda.py                         # 5W1H exploratory analysis functions
│   ├── model_training.py              # Logistic Regression, RF, XGBoost, LightGBM
│   ├── model_evaluation.py            # ROC-AUC, precision/recall, confusion matrix
│   └── reorder_engine.py              # Economic reorder quantity & safety stock logic
│
├── models/
│   ├── stockout_model.json            # Saved best model (XGBoost)
│   ├── model_bundle.joblib            # Model + scaler + test set bundle
│   └── model_metadata.json            # Model parameters and performance metrics
│
├── outputs/
│   ├── figures/                       # Saved charts (shrinkage, stockout risk, trends)
│   ├── reports/
│   │   └── inventory_stock_analysis.pdf
│   └── stockout_model_output/
│       └── model_evaluation.png
│
├── presentation/
│   └── Inventory_Analysis_Presentation.pptx
│
└── deployment
    └── app.py                # 5W1H framework, reorder formula, model selection rationale
    ├── render and GitHub

```




