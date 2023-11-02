import streamlit as st
import yfinance as yf
import datetime
import pandas as pd
from io import StringIO

st.set_page_config(layout="wide")
st.title('Import external data')

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    with st.spinner('Please Wait'):
        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file)
        st.dataframe(dataframe)
