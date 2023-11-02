import streamlit as st
import yfinance as yf
import datetime
import pandas as pd

st.set_page_config(layout="wide")
st.title('Portfolio vizualisation')

col1, col2, col3 = st.columns(3)
with col1:
    names = options = st.multiselect(
        'Compose your portfolio :',
        ['GOOG', 'AMZN', 'MCD', 'DIS'],
        ['GOOG'])
with col2:
    start_date = st.date_input("Start Date", datetime.date(2015, 1, 1))
    start_date = start_date.strftime('%Y-%m-%d')

with col3:
    end_date = st.date_input("End Date", datetime.date(2017, 12, 31))
    end_date = end_date.strftime('%Y-%m-%d')

ptf = pd.DataFrame()
for i in names:
    ptf = pd.concat([ptf, pd.DataFrame(yf.download(i, start_date, end_date)["Close"])], axis=1)
ptf.columns = names
st.markdown('### Closing price tables')
st.dataframe(ptf, use_container_width=True)
st.line_chart(ptf)
daily_return = ptf.pct_change()
st.markdown('### Evolution of daily return')
st.dataframe(daily_return, use_container_width=True)
st.line_chart(daily_return)

st.markdown('### Evolution of cumulative return')
cum_return = (1+daily_return).cumprod() - 1
st.dataframe(cum_return, use_container_width=True)
st.line_chart(cum_return)


