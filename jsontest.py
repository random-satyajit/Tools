import json
from typing import Dict, Any

import pandas as pd
import plotly.express as px
import math
import matplotlib.pyplot as plt
from numpy import mean
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
f = open(r'apex.json')
data = json.load(f)

dict1={}

for i in data['Runs']:
    c = i['CaptureData']
    for i, j in c.items():
        dict1[i] = j
#Main DataFrame
df = pd.DataFrame(dict1)

# df.plot(x='TimeInSeconds', y=(['MsBetweenPresents']))


#FPS STATS
sorted_df = df.sort_values(by='MsBetweenPresents')



sample=sorted_df.shape[0]
MIN_FPS=1000/(max(df['MsBetweenPresents']))
MAX_FPS=1000/(min(df['MsBetweenPresents']))
AVG_FPS=1000/(mean(df['MsBetweenPresents']))
# P95_FPS= 1000/sorted_df.loc[round(sample*.5), 'MsBetweenPresents']
# print(df.loc[round(sameple*0.95), 'MsBetweenPresents'])
# print(sorted_df.MsBetweenPresents)

#new Dataframe - MsBetweenPresents

Frame_time = df[["MsBetweenPresents"]].copy()
new_df_sorted = Frame_time.sort_values(by="MsBetweenPresents",ascending=True).reset_index(drop=True)

#FPS
ms_between_presents = Frame_time['MsBetweenPresents']
FPS = {
    'MsBetweenPresents': 1000/ms_between_presents
}

print(FPS)
sample1=new_df_sorted.shape[0]
# P95_FPS= 1000/new_df_sorted[round(sample*0.95), 'MsBetweenPresents']


# print(round(index))
# print(new_df_sorted.loc[38373])
# print(new_df_sorted)
# new_df_sorted.to_csv('output.csv', index=False)
# print(new_df_sorted)
# print(min(df['MsBetweenPresents']))

column_data = new_df_sorted['MsBetweenPresents']
percentile_95 = np.percentile(column_data, 5)
percentile_5=np.percentile(column_data,95)

# FPS Calculations
print('Max FPS:', round(MAX_FPS,2))
print('Min FPS:', round(MIN_FPS,2))
print('Average FPS:',  round(AVG_FPS,2))
print("95th Percentile (P95):", round(1000/percentile_95))
print("5th Percentile (P5):", round(1000/percentile_5))

#FRAME-TIME Graph
# fig = px.line(df, x='TimeInSeconds', y="MsBetweenPresents")

# df1=pd.DataFrame(Frame_time)
# df2=pd.DataFrame(FPS)
#
# fig = make_subplots(rows=1, cols=2)
#
# fig.add_trace(go.Scatter(x=df1['TimeInSeconds'], y=df1['MsBetweenPresents'], mode='lines', name='Graph 1'), row=1, col=1)
# fig.add_trace(go.Scatter(x=df2['TimeInSeconds'], y=df2['AnotherColumn'], mode='lines', name='Graph 2'), row=1, col=2)
#
# fig.update_layout(title_text="Side by Side Subplots", xaxis=dict(title='TimeInSeconds'), yaxis=dict(title='Value'))
#


# fig.show()
