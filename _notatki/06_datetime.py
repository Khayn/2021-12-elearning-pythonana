#%% Datetime

# https://python.astrotech.io/intermediate/_index.html#datetime-and-timezones
# https://www.youtube.com/watch?v=2dbjCuq2bEU&list=PLv4THqSPE6meFeo_jNLgUVKkP40UstIQv&index=13

# %% Podsumowanie

# tworzenie dat
# pobieranie elementów składowych dat
# wyciąganie daty i czasu z datetime
# formatowanie i rozczytywanie iso format
# formatowanie i rozczytywanie dowolnego formatu
# timestamp
# timedelta (odejmowanie i dodawanie czasu)
# strefy czasowe


# %%

from datetime import date, time, datetime, timezone, timedelta


date.today()
datetime.now().date()
datetime.now().time()
x.date()
x.time()
x.hour
x.year
x.month
x.day
x.minute
x.second
datetime().now()
datetime.now()
datetime.now() - timedelta(days=5)
datetime.now() - datetime(1969,7,21)
td = datetime.now() - datetime(1969,7,21)
td.days
td.days / 365
x = datetime.now()

# %% ISO Format - 8601

'2022-01-10'
'2022-01-10T18:15:35.564314'

x.isoformat()
'2022-01-10T18:15:35.564314'

x.isoformat(' ')
'2022-01-10 18:15:35.564314'


text = '2022-01-10 18:15:35.564314'
datetime.fromisoformat(text)
# datetime.datetime(2022, 1, 10, 18, 15, 35, 564314)


# %% Formatowanie

# datetime.strftime()

x.strftime('%Y-%m-%d')
'2022-01-10'

x.strftime('%d.%m.%Y')
'10.01.2022'

x.strftime('%m/%d/%y')
'01/10/22'

x.strftime('%Y-%m-%d %H:%M:%S.%f')
'2022-01-10 18:15:35.564314'

x.strftime('%A')
'Monday'

x.strftime('%a')
'Mon'

x.strftime('%B')
'January'

x.strftime('%b')
'Jan'

# %% Parsowanie

# datetime.strptime()
x
datetime.datetime(2022, 1, 10, 18, 15, 35, 564314)
x.isoformat()
'2022-01-10T18:15:35.564314'
x.isoformat(' ')
'2022-01-10 18:15:35.564314'
text = '2022-01-10 18:15:35.564314'
datetime.fromisoformat(text)
datetime.datetime(2022, 1, 10, 18, 15, 35, 564314)
text = '10.01.2022'
datetime.strptime(text, '%d.%m.%Y')
datetime.datetime(2022, 1, 10, 0, 0)
datetime.strptime(text, '%m.%d.%Y')
datetime.datetime(2022, 10, 1, 0, 0)


# %% timestamp

# timestamp
# ts
# epoch
# unix ts
# unix timestamp
# unix epoch

x
datetime.datetime(2022, 1, 10, 18, 15, 35, 564314)
x.timestamp()
1641834935.564314
(2 ** 32) / 2
2147483648.0
datetime.fromtimestamp(2147483648)
datetime.datetime(2038, 1, 19, 4, 14, 8)
datetime.fromtimestamp(-2147483648)
datetime.datetime(1901, 12, 13, 22, 9, 52)

# liczba sekund od 1970-01-01 00:00:00.000000 UTC
