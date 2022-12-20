import streamlit as st 
from random import choice 

st.title("Random Name generator")

fname = ['Alex','Bob','charlie','David','Eve','Fraank','George','Hannah','Ivan','Jenny','Karl','Linda','Mike','Naancy','Oscar','Pam','Quinn','Ralph','Sarah','Tom','Ursala','Victor','Wendy','Xavier','yvonne','Zach']
lname = ['Anderson','Baker','CLark','Davis','Evans','Foster','Garcia']

btn = st.button("Generate Name")
if btn:
      fn = choice(fname)
      ln = choice(lname)
      fullname = f"{fn} {ln}"
      st.success(fullname)

### streamlit run UI/app1.py ###