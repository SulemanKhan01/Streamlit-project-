# Student Math Score Prediction Using Streamlit

This project predicts whether a student's math score is categorized as "High" or "Not High" using a logistic regression model. The project focuses on creating an interactive Streamlit application that showcases data analysis, model performance, and insights.

---

## Table of Contents
- [Overview](#overview)
- [Features of the Application](#features-of-the-application)
- [Technologies Used](#technologies-used)
- [Steps Undertaken](#steps-undertaken)
- [Model Performance](#model-performance)
- [How to Run the Application](#how-to-run-the-application)
- [Future Recommendations](#future-recommendations)
- [Acknowledgments](#acknowledgments)

---

## Overview
This project is designed to:
- Predict student math scores as "High" or "Not High" using logistic regression.
- Provide a user-friendly interface for exploratory data analysis (EDA), model insights, and performance metrics.
- Help understand key factors influencing math scores.

The interactive Streamlit application allows users to explore the dataset, view analysis results, and assess the logistic regression model's performance.

---

## Features of the Application
- **Introduction**: Overview of the dataset and project goals.
- **EDA Section**: Visualizations, statistics, and key insights from the dataset.
- **Model Performance**: Results of the logistic regression model, including accuracy and confusion matrix.
- **Conclusions and Recommendations**: Highlights from the analysis and future work suggestions.

---

## Technologies Used
- **Streamlit**: For building the interactive web application.
- **Python Libraries**:
  - Pandas: Data manipulation and analysis.
  - Matplotlib/Seaborn: Data visualization.
  - Scikit-learn: Machine learning model implementation.

---

## Steps Undertaken
1. **Target Variable Definition**: Created the target variable `high_math_score` from the dataset.
2. **Encoding Categorical Variables**: Transformed categorical data into machine-learning-friendly formats.
3. **Data Splitting**: Divided the dataset into 80% training and 20% testing subsets.
4. **Model Selection and Training**: Applied logistic regression to classify math scores.
5. **Application Development**: Built a Streamlit application to present the entire workflow interactively.

---

## Model Performance
- **Accuracy**: Achieved 91% accuracy with logistic regression.
- **Confusion Matrix**:
  - Predicted 73 out of 79 "Not High" cases correctly.
  - Predicted 54 out of 61 "High" cases correctly.
- **Precision, Recall, F1-Score**: Demonstrated strong performance with an overall F1-score of 0.9182.
- **Insights**:
  - The model effectively classifies math scores.
  - Misclassifications were minimal, showing good generalization on unseen data.

---

## How to Run the Application
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/student-math-score-prediction.git
