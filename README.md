# 🚗 Car Price Prediction using Machine Learning

## 📌 Overview

This project is a Machine Learning model that predicts the selling price of used cars based on various features such as present price, kilometers driven, fuel type, transmission, and ownership.

The goal is to understand how regression models can be applied to real-world pricing problems.

## 🎯 Objectives

* Perform data preprocessing and cleaning
* Apply feature engineering techniques
* Train a regression model using Linear Regression
* Evaluate model performance using metrics
* Visualize actual vs predicted prices

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Joblib


## 📂 Project Structure

Car-Price-Prediction/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── EDA.ipynb
│
├── src/
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   └── evaluate_model.py
│
├── models/
│   └── car_price_model.pkl
│
├── outputs/
│   └── plots/
│
├── main.py
├── requirements.txt
└── README.md




## 📊 Workflow

1. Load the dataset
2. Clean the data (handle missing values, remove irrelevant columns)
3. Encode categorical features
4. Split data into training and testing sets
5. Train the Linear Regression model
6. Evaluate model performance
7. Visualize results


## 📈 Model Evaluation

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* R² Score

## 📉 Output Visualization

The model performance is visualized using an **Actual vs Predicted Prices** scatter plot.

## 🚀 How to Run the Project

1. Clone the repository:
git clone https://github.com/tanzeeha1504-cyber/CodeAlpha_CarPricePrediction


2. Navigate to the project folder:
cd Car-Price-Prediction

3. Install dependencies:
pip install -r requirements.txt

4. Run the project:
python main.py

## 📌 Results

The model achieved a good R² score, indicating strong predictive performance on the dataset.

## 💡 Future Improvements

* Use advanced models like Random Forest or XGBoost
* Hyperparameter tuning
* Deploy as a web application (Streamlit)

## 🙌 Acknowledgement

This project was completed as part of the **CodeAlpha Machine Learning Internship**.


## 👩‍💻 Author

Tanzeeha Suman H