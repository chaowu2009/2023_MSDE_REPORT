import streamlit as st
import pandas as pd
import numpy as np
  
st.set_page_config (layout="wide", page_title = "2023 MSDE Data Summary") 

st.title("ELA summary")


ela_file = "2023_MCAP_ELA_Administrative_Data_Report_Card.xlsx"

df_ela = pd.read_excel(ela_file,  engine='openpyxl')

st.write(df_ela.head())

st.write("* will change to zero, <5 will be changed 5, >95 will be changed 95 for sorting purpose.")

columns_to_show = [ 'LEA Name',
                    'School Name',
                    'Tested Count',
                   	'Proficient Count',
                    'Proficient Pct',
                    'Level 1 Pct',
                    'Level 2 Pct',
                    'Level 3 Pct',
                    'Level 4 Pct']


lea_selection = st.multiselect("choose a county", options=df_ela['LEA Name'].unique(),  default = ['Howard'])

if lea_selection:
    f1 =  df_ela['LEA Name'].isin(lea_selection)
    school_list = df_ela[f1]['School Name'].unique()

    school_level = st.selectbox(
        "Choose a school level",
        ("Elementary", "Middle", "High"),
        index=2)
    
    if school_level:
        school_chosen = [x for x in school_list if x.endswith(school_level)]
    else:
        school_chosen = school_list

    school_selection = st.multiselect("choose a school", options=school_list,  default = school_chosen)
else:
    school_selection = st.multiselect("choose a school", options=df_ela['School Name'].unique(),  default = ['River Hill High'])

if school_selection:
    f1 =  df_ela['School Name'].isin(school_selection)
    assessment_list = df_ela[f1]['Assessment'].unique()
    assessment_group_selection = st.selectbox("choose an assessment", assessment_list)
else:
    assessment_group_selection = st.multiselect("choose an assessment", options=df_ela['Assessment'].unique())


f1 = df_ela['LEA Name'].isin(lea_selection)
f2 = df_ela['School Name'].isin(school_selection)
f3 = df_ela['Assessment']==assessment_group_selection

def clean_data(v):
   if v=="*":
      return 0
   elif v=="<= 5.0":
       return 5
   elif v==">= 95.0":
       return 95
   else:
       return round(float(v),2)

for col in [ 'Tested Count', 
                   	'Proficient Count',
                    'Proficient Pct',
                    'Level 1 Pct',
                    'Level 2 Pct',
                    'Level 3 Pct',
                    'Level 4 Pct']:
    
    df_ela[col]= df_ela[col].apply(clean_data)
    if col in ['Tested Count', 	'Proficient Count']:
        df_ela[col] = df_ela[col].astype(int)
    else:
        df_ela[col] = df_ela[col].round(2)


df_result= df_ela[f1 & f2 &f3].sort_values(by=['Proficient Pct','Tested Count'],  ascending=False)

df_result = df_result.reset_index()

df_result.index = np.arange(1, len(df_result) + 1)

st.write(df_result[columns_to_show])


