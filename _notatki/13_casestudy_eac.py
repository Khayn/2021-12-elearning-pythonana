import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.width', 150)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 100)

DAY = 1
YEAR = 365 * DAY

DATA = 'https://en.wikipedia.org/wiki/European_Astronaut_Corps'
tables = pd.read_html(DATA)

active = tables[0]
retired = tables[1]

r = retired['Time in space'].apply(pd.to_timedelta).sum()
a = active['Time in space'].apply(pd.to_timedelta, errors='coerce').sum()

result = (a+r).days / YEAR
