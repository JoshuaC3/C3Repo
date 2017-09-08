import pandas as pd

df = pd.DataFrame({'col1': [1, 4, 3, 5], 
                   'col2': [5, 6, 3, 5]})
print(df.mean())