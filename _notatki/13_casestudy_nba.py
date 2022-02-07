import pandas as pd
import requests

DATA = 'https://stats.nba.com/stats/leaguestandingsv3?LeagueID=00&Season=2021-22&SeasonType=Regular%20Season'
HEADERS = {
    'User-Agent': 'hahaha',
    'Referer': 'https://www.nba.com',
    'Origin': 'https://www.nba.com',
}

data = requests.get(DATA, headers=HEADERS).json()
header = data['resultSets'][0]['headers']
rows = data['resultSets'][0]['rowSet']

result = pd.DataFrame(
    data=rows,
    columns=header,
)
