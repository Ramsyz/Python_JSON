import pandas as pd
df = pd.read_json('all.json', orient= 'records', lines= True)
print(df)
