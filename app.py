import streamlit as st
import pandas as pd

st.set_page_config (layout="wide", page_title = "2023 MSDE Data Summary") 


st.title("2023 MSDE Report Summary")

st.header("data source: https://support.mdassessments.com/reporting/")

st.header("Math")

math_file = "2023_MCAP_MATH_Administrative_Data_Report_Card.xlsx"
df_math = pd.read_excel(math_file,  engine='openpyxl')
st.write(df_math)

st.header("ELA")
ela_file = "2023_MCAP_ELA_Administrative_Data_Report_Card.xlsx"

df_ela = pd.read_excel(ela_file,  engine='openpyxl')

st.write(df_ela)