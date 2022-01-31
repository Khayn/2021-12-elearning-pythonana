#%% Pandas
# DATA = 'https://python.astrotech.io/_static/iris.json'
# DATA = '/Users/matt/Developer/2021-12-elearning-pythonana/_data/json/iris.json'

import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 100)

# pandas nadaje się od 0 do 15 GB (trochę mniej niż połowa ramu)
# pandas + chunksize 15 GB do 50 GB
# dask nadaje się od 50 GB do 500 GB
# spark od 500 GB

#%% Import Export

pd.read_csv()
pd.read_json()
pd.read_sql()
pd.read_excel()
pd.read_clipboard()
pd.read_html()

df.to_*


DATA = 'https://python.astrotech.io/_static/iris.csv'
df = pd.read_csv(DATA)

#%% Series


# %% DataFrame

df['sepal_length']

# Accessor df.loc[wiersze, kolumny]
# Accessor df.at[wiersz, kolumna]

# df.loc[] -> wyszukiwania kolumn i wierszy
# df.iloc[] -> wyszukiwania kolumn i wierszy
# df.loc[] -> obsługuje nazwy kolumn
# df.iloc[] -> obsługuje numery (indeksy) kolumn

# df.at[] -> wyszukiwanie komórki
# df.iat[] -> wyszukiwanie komórki
# df.at[] -> obsługuje nazwy kolumn
# df.iat[] -> obsługuje numery (indeksy) kolumn


df.loc[:, 'sepal_length']
df.loc[:, ['sepal_length', 'sepal_width']]
df.loc[50:100:2, ['sepal_length','petal_length']]

df.iloc[1:30, ::2]

# %% Statystyka

df['species'].value_counts()

df['sepal_length'].mean()
df['sepal_length'].sum()
df['sepal_length'].median()
df['sepal_length'].std()
df['sepal_length'].kurt()
df['sepal_length'].skew()

df['sepal_length'].quantile(.25)
df['sepal_length'].quantile(.33)
df['sepal_length'].quantile(.50)
df['sepal_length'].quantile(.66)
df['sepal_length'].quantile(.75)

df['sepal_length'].min()
df['sepal_length'].max()

df['sepal_length'].rolling(window=10).median()
df['sepal_length'].rolling(window=10).mean()

#%% DataFrame Plot
# https://python.astrotech.io/pandas/dataframe/plot.html

df['sepal_length'].plot(kind='linear')

df.plot(kind='density',
        subplots=True,
        layout=(2,2),
        grid=True,
        sharey=True,
        sharex=True)



# %%

DATA = 'https://python.astrotech.io/_static/phones-pl.csv'
df = pd.read_csv(DATA, parse_dates=['datetime'])

df.info(memory_usage='deep')

df['date'] = df['datetime'].dt.date
df['time'] = df['datetime'].dt.time
df['formatted'] = df['datetime'].dt.strftime('%m %B %Y')

df[ ['year','month'] ] = df['period'].str.split('-', expand=True)

df['network'].str.findall('^[A-Z]\w{5,}')
df['network'].str.extractall('^([A-Z]\w{5,})')
df['network'].str.extractall('^([A-Z][a-zA-Z\-]{4,})')


df.set_index('datetime', inplace=True, drop=True)
df.drop(columns=['id'], inplace=True)



df.query('type == "mobile"')
df.query('type=="mobile" and network=="Orange" ')


network = 'T-Mobile'
df.query('network == @network')  # @zmienna


selected = ['T-Mobile', 'Orange', 'AT&T']
df.query('network in @selected')


df.query('index > 2000')
df.query('index > "2000-01-05"')

df.loc['1999']
df.loc['1999':'1999-11-30']
df.loc['1999-11-11':'1999-11-30']
df.loc['1999-11-11':'1999-11-30', ['item', 'duration']]

# do Pandas 1.0
# np.nan (NaN to jest float)

# od Pandas 1.0
# pd.NA



x.isnull()
x.isna()
x.all()
x.any()

x.isna().any()
x.dropna(how='any', axis='row')


~x.isnull()
~x.isna()


df.groupby(['period','item']).sum()
df.loc['1999'].groupby(['period','item']).sum().plot()


df.head(n=5)
df.tail(n=5)
df.sample(n=5)
df.sample(n=5, replace=True)
df.sample(frac=.50, replace=True)
df.sample(frac=1/2, replace=True)
df.first('2W')
df.first('Q')
df.first('3M')
df.first('5D')
df.last('5D')

df['duration'].resample('D').sum()


# %%
DATA = 'https://python.astrotech.io/_static/phones-pl.csv'


df = (
    pd
    .read_csv(DATA, parse_dates=['datetime'])
    .set_index('datetime', drop=True)
    .drop(columns=['id'])
)


df.groupby(['period','item']).agg(
    duration_count = ('duration', 'count'),
    duration_sum = ('duration', 'sum'),
    duration_median = ('duration', 'median'),
    duration_mean = ('duration', 'mean'),
    duration_std = ('duration', 'std'),
    duration_var = ('duration', 'var'),
    value = ('duration', lambda column: column.mean().astype(int))
)


# %%
DATA = 'https://python.astrotech.io/_static/phones-pl.csv'

result = (
    pd
    .read_csv(DATA, parse_dates=['datetime'])
    .set_index('datetime', drop=True)
    .drop(columns=['id'])
    .loc['2000-01-01':'2000-03-01']
    .query('item == "sms"')
    .groupby(['period','item'])
    .agg(
        duration_count = ('duration', 'count'),
        duration_sum = ('duration', 'sum'),
        duration_median = ('duration', 'median'),
        duration_mean = ('duration', 'mean'),
        duration_std = ('duration', 'std'),
        duration_var = ('duration', 'var'),
        value = ('duration', lambda column: column.mean().astype(int))
    )
)
