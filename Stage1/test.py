import pandas as pd
import os

print(os.getcwd())
path = os.getcwd() + '\Stage1\data.csv'
print(path)
data = pd.read_csv(path, low_memory = False)
print('finished')