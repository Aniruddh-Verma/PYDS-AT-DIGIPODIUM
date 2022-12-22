import pandas as pd
import plotly.express as px
import streamlit as st

 
def load_titanic_data():
      return pd.read_csv('UI/titanic.csv')

def clean_data(df):
      df.drop(columns=['Cabin'],inplace=True)
      df['Age'].fillna(df['Age'].mean(), inplace=True)
      df['Survived'] = df['Survived'].apply(lambda x: 'Yes' if x == 1 else 'No')
      return df      

with st.spinner("Loading Dataset..."):
      titanic = load_titanic_data()
      titanic = clean_data(titanic)

if st.sidebar.checkbox("Click On check box To See the dataset"):
      st.header("Titanic Dataset")
      st.dataframe(titanic)

if st.sidebar.checkbox("view Datatypes for each Columns"):
      st.header("Datatype for Each Column")
      c1,c2,c3 = st.columns(3)
      total_cols = len(titanic.columns)
      for idx,col in enumerate(titanic):
            if idx< total_cols/3:
                  c1.metric(f'Column:{col}',
                  f'Type: {titanic[col].dtype}',
                  f'Unique: {titanic[col].nunique()}')
            elif idx< 2*total_cols/3:
                  c2.metric(f'Column:{col}',
                  f'Type: {titanic[col].dtype}',
                  f'Unique: {titanic[col].nunique()}')
            else:
                  c3.metric(f'Column:{col}',
                  f'Type: {titanic[col].dtype}',
                  f'Unique: {titanic[col].nunique()}')
if st.sidebar.checkbox("View Summary statistics for Each Columns"):
      st.header("Summary statistics for each columns")
      st.dataframe(titanic.describe(include='all'),use_container_width=True)

goptions = ['bar','histogram','box','violin','scatter']
c1,c2 = st.columns(2)
selected_col = c1.selectbox("select a Column" , titanic.columns.tolist())
graph_type = c2.selectbox("Select a Graph Type", goptions)

if graph_type == goptions[0]:
      fig = px.bar(titanic, x=selected_col)
elif graph_type == goptions[1]:
      fig = px.histogram(titanic, x=selected_col)
elif graph_type == goptions[2]:
      fig = px.box(titanic, x=selected_col)
elif graph_type == goptions[3]:
      fig = px.violin(titanic, x=selected_col)
elif graph_type == goptions[4]:
      fig = px.scatter(titanic, x= selected_col, y='Age')
st.plotly_chart(fig)

st.header("Bivariate Column Analysis")
goptions = ['Scatter','Box','Violin']
c1,c2,c3 = st.columns(3)
sc1 = c1.selectbox("select a Column for X", titanic.columns.tolist())
sc2 = c2.selectbox("Seelct a Columns for Y", titanic.columns.tolist())
graph_type = c3.selectbox("select Graph Type", goptions)
try:
      if graph_type == goptions[0]:
            fig = px.scatter(titanic, x= sc1, y=sc2)
      elif graph_type == goptions[1]:
            fig = px.box(titanic, x=sc1, y= sc2)
      elif graph_type == goptions[2]:
            fig = px.violin(titanic, x=sc1, y=sc2)
      st.plotly_chart(fig)
except Exception as e:
      st.error(f'Error:{e}')
      st.error("please select a different Columns for X and Y")

st.header("Important Visualization")

# Survival Rate wtih respect to genders
fig = px.bar(titanic, y='Pclass', x='Survived', facet_col='Sex',color='Survived',
             title='Survival of gender with respect to passenger',
             color_discrete_sequence=px.colors.qualitative.D3)
st.plotly_chart(fig)