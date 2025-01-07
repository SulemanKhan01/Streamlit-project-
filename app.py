import streamlit as st
from introduction import introduction
from datasetView import dataset_overview
from EDA2 import eda2
from ml_model import ml_model
from preprocessing import preprocessing
from conclusion_and_insights import conclusion_and_insights

# Dictionary to map page names to functions
pages = {
    "Introduction": introduction,
    "Dataset Overview": dataset_overview,
    "EDA": eda2,
    "Machine Learning Model": ml_model,
    "Data Preprocessing": preprocessing,
    "Conclusion and Insights": conclusion_and_insights
}

# Sidebar for navigation
st.sidebar.title("Heart Disease Dataset")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Display the selected page
pages[selection]()
