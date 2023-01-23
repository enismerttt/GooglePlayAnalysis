import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('cleaned_playstore.csv')

top_3_app = df.sort_values(by=['Installs','Rating','Reviews'], ascending=False).head(n=3)
top_3_app_values = pd.DataFrame(columns=['col1', 'col2'])
top_3_app_values['col1'] = top_3_app['App']
top_3_app_values['col2'] = top_3_app['Installs']
print(top_3_app_values)

plt.bar(top_3_app_values['col1'], top_3_app_values['col2'])
plt.xlabel('Apps')
plt.ylabel('Installs')
plt.title('Top 3 Most Installed Apps')
plt.show()