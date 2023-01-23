
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cleaned_playstore.csv')
top5 = df.sort_values(by=['Installs','Size'],ascending=[False,True]).head(5)

plt.figure(figsize=(10,5))
plt.xticks(rotation= 75)
plt.bar(top5['App'],top5['Installs'],width=0.3)
plt.show
