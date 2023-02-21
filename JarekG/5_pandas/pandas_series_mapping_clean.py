"""

* Assignment: Series Mapping Clean
* Complexity: medium
* Lines of code: 15 lines
* Time: 21 min

English:
    1. Convert `DATA` to `pd.Series`
    2. Write function to clean up data
    3. Function takes one `str` argument
    4. Function returns cleaned text
    5. Apply function to all elements of `pd.Series`
    6. Run doctests - all must succeed

Polish:
    1. Przekonwertuj `DATA` do `pd.Series`
    2. Napisz funkcję czyszczącą dane
    3. Funkcja przyjmuje jeden argument typu `str`
    4. Funkcja zwraca oczyszczony tekst
    5. Zaaplikuj funkcję na wszystkich elementach `pd.Series`
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> pd.set_option('display.width', 500)
    >>> pd.set_option('display.max_columns', 10)
    >>> pd.set_option('display.max_rows', 10)

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is pd.Series, \
    'Variable `result` has invalid type, should be `pd.Series`'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    0               Mieszka II
    1        Zygmunta III Wazy
    2      Bolesława Chrobrego
    3     Jana III Sobieskiego
    4     Jana III Sobieskiego
                  ...
    6     Jana III Sobieskiego
    7     Jana III Sobieskiego
    8     Jana III Sobieskiego
    9     Jana III Sobieskiego
    10    Jana III Sobieskiego
    Length: 11, dtype: object

TODO: Translate input data to English
"""

import pandas as pd



DATA = ['ul.Mieszka II',
        'UL. Zygmunta III WaZY',
        '  bolesława chrobrego ',
        'ul Jana III SobIESkiego',
        '\tul. Jana trzeciego Sobieskiego',
        'ulicaJana III Sobieskiego',
        'UL. JA    NA 3 SOBIES  KIEGO',
        'ULICA JANA III SOBIESKIEGO  ',
        'ULICA. JANA III SOBIeskieGO',
        ' Jana 3 Sobieskiego  ',
        'Jana III Sobi  eskiego ']

def clean(text: str) -> str:
    text = text.strip().upper()
    text = text.replace('3', 'III').replace('.', '')
    text = text.replace('    ', '').replace('  ', '')
    text = text.replace('ULICA', '').replace('UL', '')
    text = text.replace('TRZECIEGO', 'III')
    text = text.strip().title()
    text = text.replace('Iii', 'III').replace('Ii', 'II')
    return text


result = pd.Series(DATA)
result = result.map(clean)
