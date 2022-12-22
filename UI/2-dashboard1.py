import pandas as pd
import plotly.express as px
import streamlit as st


# load data 
def load_titanic_data():
      return pd.read_csv('UI/titanic.csv')

def clean_data(df):
      df.drop(columns=['Cabin'],inplace=True)
      df['Age'].fillna(df['Age'].mean(), inplace=True)
      return df      
# clean data 
# display
with st.spinner("Loading Dataset..."):
      titanic = load_titanic_data()
      titanic = clean_data(titanic)
st.dataframe(titanic)

selected_col = st.selectbox("select a column", titanic.columns.tolist())
st.metric(f'column: {selected_col}',str(titanic[selected_col].dtype),titanic[selected_col].nunique())

st.write(titanic[selected_col])

# visualize 


