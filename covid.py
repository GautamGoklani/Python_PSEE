import matplotlib.pyplot as plt
import pandas as pd

x = pd.read_csv('covid.csv')

plt.figure(figsize=(100, 50))
plt.plot(x['Country'],x['Confirmed'])
plt.plot(x['Country'],x['Deaths'])
plt.xticks(rotation=90)
plt.xlabel('Country')
plt.ylabel('Confirmed')
plt.title('Confirmed Cases of Corona')
plt.show()