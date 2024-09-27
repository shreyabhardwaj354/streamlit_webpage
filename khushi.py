import streamlit as st
import plotly.express as px
import pandas as pd

# Create a sample dataset for experimental results
data = {
    'Experiment': ['Experiment 1', 'Experiment 1', 'Experiment 2', 'Experiment 2'],
    'Result': [10, 20, 30, 40],
    'Category': ['A', 'B', 'A', 'B']
}

df = pd.DataFrame(data)

# Create a Streamlit app
st.title("Experimental Results")

# Create a dropdown menu to select experiments
experiments = ['Experiment 1', 'Experiment 2']
selected_experiment = st.selectbox("Select Experiment", experiments)

# Filter the data based on the selected experiment
filtered_df = df[df['Experiment'] == selected_experiment]

# Create a Plotly graph
fig = px.bar(filtered_df, x='Category', y='Result')

# Display the graph
st.plotly_chart(fig)