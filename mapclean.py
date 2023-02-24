import pandas as pd

df = pd.read_csv('liste-des-gares.csv', sep=';', usecols=['commune', 'departement', 'geo_point_2d'])
df = df.dropna(subset=['commune', 'departement', 'geo_point_2d'])

df[['latitude', 'longitude']] = df['geo_point_2d'].str.split(',', expand=True)
df = df.drop('geo_point_2d', axis=1)

# print(df.head(10))

df.to_csv('output.csv', index=False)