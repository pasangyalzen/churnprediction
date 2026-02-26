# 📊 Customer Churn Prediction & Deployment

This project provides a complete end-to-end machine learning solution to predict customer attrition. It includes a detailed data analysis pipeline and a **Streamlit** web application for real-time predictions.

## 🧠 Model Insights
Based on the Random Forest model analysis, the top factors contributing to churn are:
1. **Satisfaction Score**: The most critical indicator; customers with scores of 1-2 are at high risk.
2. **Tenure (Months)**: Early-stage customers (less than 9 months) show significantly higher churn rates.
3. **Contract Type**: Customers on Month-to-Month contracts are more likely to leave compared to those on Two-Year plans.
4. **Internet Type**: Fiber Optic users show a higher churn rate (40.7%) compared to DSL or Cable users.

## 🛠️ Tech Stack
* **Analysis**: Python, Pandas, NumPy
* **Visualization**: Matplotlib, Seaborn
* **Machine Learning**: Scikit-Learn (Random Forest Classifier with `class_weight='balanced'`)
* **Deployment**: Streamlit & Joblib

## 📈 Model Performance
The final optimized model achieved:
* **ROC-AUC**: ~0.93 (High predictive power)
* **Balanced Handling**: Used `class_weight='balanced'` to account for the fact that only ~26.5% of the data represents churned customers.

## 🚀 How to Use the App
1. Install requirements: `pip install streamlit pandas joblib scikit-learn`
2. Run the app: `streamlit run churnprediction.py`
3. Input customer metrics (Satisfaction, Tenure, Charges) to see a real-time Risk Score.

## 📁 Files in this Repo
* `churnprediction.ipynb`: Full EDA, Feature Engineering, and Model Tuning.
* `churn_model.pkl`: The serialized Random Forest model.
* `churndata.csv`: The raw customer dataset.
