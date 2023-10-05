import pandas as pd

df = pd.read_csv('cars.csv', sep=';')
pd.set_option('display.max_rows', 100000)
pd.set_option('display.max_columns', 9)
df['MPG'] = df['MPG'].iloc[1:].astype(float)
df = df.sort_values(by='MPG', ascending=False)
df = df.dropna()
NON_ZERO_FILTER = df['MPG'] != 0  # Filtered MPG
MPG = df[NON_ZERO_FILTER]
HIGHEST = MPG.iloc[0]
LOWEST = MPG.iloc[-1]
MEAN = MPG['MPG'].mean()
MEDIAN = MPG['MPG'].median()

print(HIGHEST)
print(LOWEST)
print(f'mean is {MEAN}')
print(f'median is {MEDIAN}')