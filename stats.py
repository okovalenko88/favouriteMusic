#!python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.tbl', sep='\t', header=None, names=['name', 'author', 'year', 'sales'], index_col = False)
plt.scatter(data['year'], sorted(list(map(lambda x: float(x.replace(' Millionen', '').replace(',', '')), data['sales']))), alpha = 0.5, s = 50);
plt.xlabel('Year')
plt.ylabel('Sales, millions')
plt.show()
