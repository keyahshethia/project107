import pandas as ps
import plotly.graph_objects as go
import csv

df=ps.read_csv("data.csv")
print(df.groupby("level")["attempt"].mean())

fig=go.Figure(go.Bar(x=df.groupby("level")["attempt"].mean(),y=['Level1','Level2','Level3','Level4'],orientation='h'))
fig.show()