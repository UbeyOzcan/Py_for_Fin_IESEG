import numpy as np
from scipy.stats import norm
import streamlit as st
import pandas as pd
import plotly.express as px

N = norm.cdf

S0 = st.sidebar.number_input('Current Stock Value : ', value=100)
K_call = st.sidebar.number_input('Strike long call : ', value=105)
K_put = st.sidebar.number_input('Strike long put : ', value=95)
T = st.sidebar.number_input('Time Horizon : ', value=1)
r = st.sidebar.number_input('Risk-Free rate : ', value=0)
sig = st.sidebar.number_input('Volatility : ', value=0.2)

st.title('Black and Scholes models calculator')


def BS_CALL(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return round(S * N(d1) - K * np.exp(-r * T) * N(d2), 2)


def BS_PUT(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return round(K * np.exp(-r * T) * N(-d2) - S * N(-d1), 2)


sT = np.arange(0.7 * S0, 1.3 * S0, 1)


def call_payoff(sT, strike_price, premium):
    return pd.DataFrame({'St': sT,
                         'payoff_call': np.where(sT > strike_price, sT - strike_price, 0) - premium})


Call = BS_CALL(S0, K_call, T, r, sig)
payoff_long_call = call_payoff(sT, K_call, Call)

fig = px.line(payoff_long_call, x="St", y="payoff_call", title='Payoff Long Call')
st.plotly_chart(fig)
st.markdown(f'### The Call price calculated using B-S Model is : ***{Call}*** ')


def put_payoff(sT, strike_price, premium):
    return pd.DataFrame({'St': sT,
                         'payoff_put': np.where(sT < strike_price, strike_price - sT, 0) - premium})


Put = BS_PUT(S0, K_put, T, r, sig)
payoff_long_put = put_payoff(sT, K_put, Put)
fig2 = px.line(payoff_long_put, x="St", y="payoff_put", title='Payoff Long Put')
st.plotly_chart(fig2)
st.markdown(f'### The Put price calculated using B-S Model is : ***{Put}*** ')
