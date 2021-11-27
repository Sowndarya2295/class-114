import pandas as pd
import plotly.express as px

df = pd.read_csv('test.csv')
fig = px.scatter(df, x="GRE Score", y="Chance of Admit ")
fig.show()