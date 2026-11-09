# Medical Insurance Cost Prediction

## Problem
Predict the yearly medical insurance charge of a person from their age, BMI, number of children, smoking status, gender and region.

## Dataset
1,338 records, 7 columns (age, sex, bmi, children, smoker, region, charges). No missing values. One duplicate row was removed, leaving 1,337.

## Preprocessing
- Removed duplicates
- Encoded sex and smoker as 0/1
- One-hot encoded region
- 80/20 train-test split (random_state=42)

## Model
Multiple Linear Regression (scikit-learn).

## Evaluation (test set)
| Metric | Value |
|--------|-------|
| MAE | 4177.05 |
| MSE | 35478020.68 |
| RMSE | 5956.34 |
| R2 | 0.8069 |

## Key Findings
- Smoking is the biggest cost driver (correlation 0.79 with charges)
- Charges rise with age (0.30)
- BMI has a moderate effect (0.20)
- Gender and number of children have little impact

## Screenshots
Add your images from the screenshots folder here.

## Live App
PASTE YOUR DEPLOYED LINK HERE

## How to Run
pip install -r requirements.txt
streamlit run app.py

## Limitations
- A linear model cannot capture interactions (e.g. high BMI matters more for smokers)
- Trained on one public dataset, so it is an educational estimate, not a real insurance quote
- Predictions can be unrealistic at extreme inputs
