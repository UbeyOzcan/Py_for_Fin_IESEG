import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

pd.options.plotting.backend = "plotly"
st.set_page_config(layout="wide")
st.title('Simulation of Geometric Brownian Motion')
# Parameters
# drift coefficent
mu = st.sidebar.number_input('Select the mu parameter : ', value=0.1)
# number of steps
n = st.sidebar.number_input('Select the steps of dicretization : ', value=100)
# time in years
T = st.sidebar.number_input('Select the time horizon in year : ', value=1)
# number of sims
M = st.sidebar.number_input('Select the number of simulation :', value=500)
# initial stock price
S0 = st.sidebar.number_input('Select the initial stock price', value=1)
# volatility
sigma = st.sidebar.number_input('Select the volatility factor : ', value=0.5)
run = st.button('Simulate ! ')
if run:
    # calc each time step
    dt = T / n
    # simulation using numpy arrays
    St = np.exp(
        (mu - sigma ** 2 / 2) * dt
        + sigma * np.random.normal(0, np.sqrt(dt), size=(M, n)).T
    )
    # include array of 1's
    St = np.vstack([np.ones(M), St])
    # multiply through by S0 and return the cumulative product of elements along a given simulation path (axis=0).
    St = S0 * St.cumprod(axis=0)

    # Define time interval correctly
    time = np.linspace(0, T, n + 1)
    # Require numpy array that is the same shape as St
    tt = np.full(shape=(M, n + 1), fill_value=time).T
    St = pd.DataFrame(St)
    fig = px.line(St)
    fig.update_layout(showlegend=False)

    st.plotly_chart(fig, use_container_width=True)
