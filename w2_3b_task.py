import pandas as pd
import matplotlib.pyplot as plt

df_apps = pd.read_csv("cleaned_playstore.csv")

df_apps['Total Profit'] = df_apps['Price']*df_apps['Installs']
barchart = df_apps.groupby('Category')['Total Profit'].sum().sort_values(ascending=0).head(10)

plt.figure(figsize=(15,5))
plt.xticks(rotation=90)
plt.bar(barchart.index, barchart.values, width=0.3)
plt.xlabel('Categories')
plt.ylabel('Total Profit')
plt.title('Top Categories With Highest Profit')
plt.show()