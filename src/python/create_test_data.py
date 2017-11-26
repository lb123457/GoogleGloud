import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(0,100,size=(30000, 4)), columns=list('ABCD'))

print(df)

df.to_csv('~/Development/Data/dummy.csv', index=False, encoding='utf-8')

print('Done writing file')

