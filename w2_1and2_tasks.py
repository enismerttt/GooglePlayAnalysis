#1- print (table) the unique names of all categories
import pandas as pd
df=pd.read_csv('cleaned_playstore.csv')
table=df['Category'].unique()
table=pd.DataFrame(table,columns=['Unique Category Names'])
print(table)


#2- plot a bar chart for categories with the total number of installing numbers in each category
import matplotlib.pyplot as plt
df_grouped = df.groupby('Category')['Installs'].apply(lambda x: x.sum())
df_grouped.plot.bar(color='b', width=0.5, title='Total Number of Installing Numbers in Each Category')
plt.xlabel("Categories")
plt.ylabel("Install Amount")
plt.subplots_adjust(top=0.92, bottom=0.3, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)
plt.show()



