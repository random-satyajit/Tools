import json
import pandas as pd
import matplotlib.pyplot as plt

f = open(r'file path')
data = json.load(f)

dict = {}

for i in data['Runs']:
    c = i['CaptureData']
    for i, j in c.items():
        dict[i] = j

df = pd.DataFrame(dict)
df.plot(x='TimeInSeconds', y=(['MsBetweenPresents']))

#Ploting the frame-time graph 
plt.show()
