import csv
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
df = pd.read_csv('data2.csv')
studentdf = df.loc[df['student_id'] == 'TRL_xsl']
print(studentdf.groupby('level')['attempt'].mean())
fig = go.Figure(go.Bar(
    x = studentdf.groupby('level')['attempt'].mean(),
    y = ['Level 1', 'Level 2', 'Level 3', 'Level 4'],
    orientation = 'h'
))
fig.show()