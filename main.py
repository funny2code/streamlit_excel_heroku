import streamlit as st
import pandas as pd
import math # Import the math module
import openpyxl



# Load the Excel file "Universe_new_Moumita" into a DataFrame
st.title('Uber pickups in NYC')
st.text('Loaded an example Excel file...')
df = pd.read_excel('1203_Tokenomics_Lacentral.xlsx')
# data_load_state.text('Loading data...done')
st.subheader('Raw data')
st.write(df)