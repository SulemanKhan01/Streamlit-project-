import streamlit as st

def conclusion_and_insights():
    st.title("Conclusion and Insights")
    
    st.subheader("Steps Undertaken:")
    st.write("""
    - **Defining Target Variable**: The target variable, `high_math_score`, was defined successfully based on the dataset.
    - **Encoding Categorical Variables**: Categorical features were encoded to make them suitable for machine learning models.
    - **Data Splitting**: The dataset was split into training and testing sets with a selected test size of 20%.
    - **Model Selection and Training**: Logistic regression was used as the classification model.
    """)

    st.subheader("Model Performance:")
    st.write("""
    - **Accuracy**: The logistic regression model achieved a high accuracy of 91%.
    - **Confusion Matrix**:
        - Correctly predicted 73 out of 79 "Not High" cases.
        - Correctly predicted 54 out of 61 "High" cases.
    - **Precision, Recall, and F1-Score**: The model demonstrated strong performance across all evaluation metrics, with an overall F1-score of 0.9182.
    """)

    st.subheader("Insights:")
    st.write("""
    - The logistic regression model effectively distinguishes between "High" and "Not High" math scores based on the provided features.
    - The small number of misclassifications suggests that the model generalizes well to unseen data.
    """)

    st.subheader("Future Recommendations:")
    st.write("""
    - Explore additional features or interaction terms to potentially improve model performance.
    - Test alternative classification models, such as decision trees or random forests, for comparison.
    - Analyze feature importance to understand which factors contribute most to predicting high math scores.
    """)

# Call the function to display the conclusion and insights
conclusion_and_insights()

