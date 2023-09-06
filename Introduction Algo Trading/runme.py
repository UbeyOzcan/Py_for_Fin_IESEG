from funcs.Extractor import extract_stock_price
from funcs.Bollinger import bollinger
from funcs.RSI import rsi
from funcs.Strategy import strategy
from funcs.Graph import plot_startegy
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

pd.options.plotting.backend = "plotly"

df = extract_stock_price(ticker='SQ',
                         start='2019-01-01',
                         end='2022-08-13')

bb = bollinger(df_prices=df,
               window=14,
               delta=1.3)

rsi = rsi(df_prices=bb,
          window=14)

result_strat_1 = strategy(df_prices=rsi,
                          rsi_lower=40,
                          rsi_upper=60,
                          stop_loss=False)

result_strat_2 = strategy(
    df_prices=rsi,
    rsi_lower=40,
    rsi_upper=60,
    stop_loss=True,
    sl=0.70)

fig1_strat_1, fig2_strat_1, fig3_strat_1 = plot_startegy(result_strat_1)
fig1_strat_2, fig2_strat_2, fig3_strat_2 = plot_startegy(result_strat_2)

#fig1_strat_1.show()
#fig2_strat_1.show()
fig3_strat_1.show()
print(result_strat_1['return'])
#fig1_strat_2.show()
#fig2_strat_2.show()
fig3_strat_2.show()
print(result_strat_2['return'])