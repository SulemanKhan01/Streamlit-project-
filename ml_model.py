# Importing necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.preprocessing import LabelEncoder
import streamlit as st
import joblib

def ml_model():
    # Streamlit app title
    st.title("Logistic Regression: High Math Score Classification")

    # File uploader for the dataset
    uploaded_file = st.file_uploader("Upload your CSV dataset", type="csv")

    if uploaded_file is not None:
        # Load the dataset
        try:
            data = pd.read_csv(uploaded_file)
            st.write("### Dataset Overview")
            st.write("Preview of the dataset:")
            st.write(data.head())
        except Exception as e:
            st.error(f"Error loading the file: {e}")
            st.stop()

        # Check if the required column exists
        if 'math score' not in data.columns:
            st.error("The dataset must contain a 'math score' column!")
            st.stop()

        # Define the target column: High performance in math (binary classification)
        st.write("### Defining Target Variable")
        data['high_math_score'] = (data['math score'] >= 70).astype(int)
        st.write("Target column `high_math_score` added successfully.")

        # Encode categorical variables (if any)
        st.write("### Encoding Categorical Variables")
        categorical_columns = data.select_dtypes(include=['object']).columns
        label_encoders = {}
        if len(categorical_columns) > 0:
            for column in categorical_columns:
                le = LabelEncoder()
                data[column] = le.fit_transform(data[column])
                label_encoders[column] = le
            st.success("Categorical variables encoded successfully!")
        else:
            st.info("No categorical variables found. Skipping encoding step.")

        # Split the dataset into features and target
        st.write("### Splitting the Dataset")
        X = data.drop(columns=['math score', 'high_math_score'])
        y = data['high_math_score']

        # Interactive test size selection
        test_size = st.slider("Select Test Size (Percentage)", min_value=10, max_value=50, value=20, step=5) / 100
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
        st.write(f"Training Set: {X_train.shape[0]} samples")
        st.write(f"Testing Set: {X_test.shape[0]} samples")

        # Train Logistic Regression Model
        st.write("### Training Logistic Regression Model")
        model = LogisticRegression()
        try:
            model.fit(X_train, y_train)
            st.success("Model trained successfully!")
        except Exception as e:
            st.error(f"Error training the model: {e}")
            st.stop()

        # Make predictions
        y_pred = model.predict(X_test)

        # Evaluate the model
        st.write("### Model Evaluation")
        accuracy = accuracy_score(y_test, y_pred)
        st.metric("Model Accuracy", f"{accuracy:.2f}")

        # Display confusion matrix
        conf_matrix = confusion_matrix(y_test, y_pred)
        conf_matrix_df = pd.DataFrame(conf_matrix, 
                                    index=["Not High (0)", "High (1)"], 
                                    columns=["Predicted 0", "Predicted 1"])
        st.write("**Confusion Matrix:**")
        st.dataframe(conf_matrix_df)

        # Display classification report
        class_report = classification_report(y_test, y_pred, output_dict=True)
        class_report_df = pd.DataFrame(class_report).transpose()
        st.write("**Classification Report:**")
        st.dataframe(class_report_df)

        # Option to save the trained model
        if st.button("Save Model"):
            joblib.dump(model, 'logistic_regression_model.pkl')
            st.success("Model saved as `logistic_regression_model.pkl`!")

        # Interactive prediction
        st.write("### Make Predictions with New Data")
        with st.form("prediction_form"):
            st.write("Enter values for the features:")
            user_input = {}
            for col in X.columns:
                if col in categorical_columns:
                    # Provide dropdown options for categorical variables
                    options = {i: label for i, label in enumerate(label_encoders[col].classes_)}
                    user_input[col] = st.selectbox(f"{col} (categorical)", options.keys(), format_func=lambda x: options[x])
                else:
                    # Provide numeric input for other variables
                    user_input[col] = st.number_input(f"{col} (numeric)", min_value=float(X[col].min()), max_value=float(X[col].max()), step=1.0)
            
            submit = st.form_submit_button("Predict")
            if submit:
                try:
                    user_df = pd.DataFrame([user_input])  # Convert input into a DataFrame
                    prediction = model.predict(user_df)[0]
                    prediction_label = "High Math Score (1)" if prediction == 1 else "Not High Math Score (0)"
                    st.success(f"Prediction: {prediction_label}")
                except Exception as e:
                    st.error(f"Error making prediction: {e}")

    else:
        st.warning("Please upload a CSV file to proceed.")