import pandas as pd
from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday, EasterMonday, Easter
from pandas.tseries.offsets import Day
import matplotlib.pyplot as plt
from doctest import testmod as run_tests

pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 100)


CONFIRMED = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
DEATHS = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
RECOVERED = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'

confirmed = pd.read_csv(CONFIRMED)
deaths = pd.read_csv(DEATHS)
recovered = pd.read_csv(RECOVERED)


class PLHolidayCalendar(AbstractHolidayCalendar):
    """
    Custom Holiday calendar for Poland based on
    https://en.wikipedia.org/wiki/Public_holidays_in_Poland
    """
    rules = [
        Holiday('New Years Day', month=1, day=1),
        Holiday('Epiphany', month=1, day=6),
        Holiday('Easter', month=1, day=1, offset=[Easter()]),
        EasterMonday,
        Holiday('May Day', month=5, day=1),
        Holiday('Constitution Day', month=5, day=3),
        Holiday('Pentecost Sunday', month=1, day=1, offset=[Easter(), Day(49)]),
        Holiday('Corpus Christi', month=1, day=1, offset=[Easter(), Day(60)]),
        Holiday('Assumption of the Blessed Virgin Mary', month=8, day=15),
        Holiday('All Saints Day', month=11, day=1),
        Holiday('Independence Day', month=11, day=11),
        Holiday('Christmas Day', month=12, day=25),
        Holiday('Second Day of Christmastide', month=12, day=26),
    ]

def _get(country, data, column_name):
    """
    >>> _get('Poland', confirmed, 'Confirmed').loc['2022-01-01']
    Confirmed    4120248
    Name: 2022-01-01 00:00:00, dtype: int64

    >>> _get('Poland', deaths, 'Deaths').loc['2022-01-01']
    Deaths    97559
    Name: 2022-01-01 00:00:00, dtype: int64

    >>> _get('Poland', recovered, 'Recovered').loc['2022-01-01']
    Recovered    0
    Name: 2022-01-01 00:00:00, dtype: int64
    """
    if country is not None:
        query = data['Country/Region'] == country
        data = data[query]
    data = data.transpose()[4:].sum(axis='columns').astype('int64')
    df = pd.DataFrame(data)
    df.columns = [column_name]
    df.index = df.index.map(pd.to_datetime)
    return df

def covid19(country=None):
    """
    >>> covid19('Poland').loc['2022-01-01']
    Confirmed    4120248
    Deaths         97559
    Recovered          0
    Name: 2022-01-01 00:00:00, dtype: int64

    >>> covid19('US').loc['2022-01-01']
    Confirmed    54963778
    Deaths         828124
    Recovered           0
    Name: 2022-01-01 00:00:00, dtype: int64

    >>> covid19('France').loc['2022-01-01']
    Confirmed    10296909
    Deaths         124839
    Recovered           0
    Name: 2022-01-01 00:00:00, dtype: int64

    >>> covid19().loc['2022-01-01']
    Confirmed    289514753
    Deaths         5444013
    Recovered            0
    Name: 2022-01-01 00:00:00, dtype: int64
    """
    return pd.concat((
        _get(country, confirmed, 'Confirmed'),
        _get(country, deaths, 'Deaths'),
        _get(country, recovered, 'Recovered'),
    ), axis='columns')

poland = covid19('Poland')
usa = covid19('US')
france = covid19('France')
china = covid19('China')
world = covid19()




data = poland.loc['2022-01-01':, ['Confirmed','Deaths']]

data.plot(kind='line', subplots=True, layout=(2,1), figsize=(10,10))
plt.show()


# śmiertelność
ratio = data['Deaths'] / data['Confirmed']
percent = ratio * 100
percent.plot(
    kind='line',
    title='Percent of deaths vs new cases in last two weeks',
    xlabel='Day',
    ylabel='Percent',
    ylim=(2.1, 2.5),
    figsize=(10,10),
    grid=True)
plt.show()


# przyrost zakażeń dzień po dniu
data['Confirmed'].diff().plot()


# liczba dziennych zakażeń w okresie ostatnich 2 tygodni
data['Confirmed'].last('2W').diff().plot()
plt.show()

# przyrost nowych zakażeń w okresach miesięcznych
poland['Confirmed'].resample('M').sum().plot()
plt.show()


# fale zakażeń covid
poland['Confirmed'].diff().resample('W').median().plot()
plt.show()


# jak wyglądały zakażenia w dwa tygodnie po świętach
# czy święta (spotkania rodzin) odbijają się na wzroście zakażeń
pl_holidays = PLHolidayCalendar().holidays(start='2021-01-01', end='2022-02-07')

DAYS = 14
result = {}

for holiday in pl_holidays:
    column = poland['Confirmed']
    start = holiday
    column_name = holiday.date().isoformat()
    result[column_name] = []

    for i in range(DAYS):
        day = holiday + pd.Timedelta(days=i)
        value = column.loc[day]
        result[column_name].append(value)

trend = pd.DataFrame(result).diff()
trend.plot(
    kind='line',
    subplots=True,
    layout=(15,1),
    sharex=True,
    figsize=(5,15),
    grid=True)


# matt@sages.io
