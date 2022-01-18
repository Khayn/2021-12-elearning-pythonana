"""
* Assignment: CSV Relations Join
* Complexity: hard
* Lines of code: 11 lines
* Time: 21 min

English:
    1. Using `csv.DictWriter()` save `CREW` to `FILE`
    2. Non-functional requirements:
        a. All fields must be enclosed by double quote `"` character
        b. Use `,` to separate mission fields
        c. Use `;` to separate missions
        d. Use Unix `\n` newline
        e. Sort `fieldnames` using `sorted()`
    3. Run doctests - all must succeed

Polish:
    1. Za pomocą `csv.DictWriter()` zapisz `CREW` do `FILE`
    2. Wymagania niefunkcjonalne:
        a. Wszystkie pola muszą być otoczone znakiem cudzysłowu `"`
        b. Użyj `,` do oddzielania pól mission
        c. Użyj `;` do oddzielenia missions
        d. Użyj zakończenia linii Unix `\n`
        e. Posortuj `fieldnames` używając `sorted()`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `vars(obj)`
    * Nested `for`
    * `str.join(';', sequence)`
    * `str.join(',', sequence)`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove
    >>> result = open(FILE).read()
    >>> remove(FILE)

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> print(result)
    "firstname","lastname","missions"
    "Mark","Watney","2035,Ares 3"
    "Melissa","Lewis","2030,Ares 1;2035,Ares 3"
    "Rick","Martinez",""
    <BLANKLINE>
"""

import csv


class Astronaut:
    def __init__(self, firstname, lastname, missions=None):
        self.firstname = firstname
        self.lastname = lastname
        self.missions = list(missions) if missions else []


class Mission:
    def __init__(self, year, name):
        self.year = year
        self.name = name


CREW = [
    Astronaut('Mark', 'Watney', missions=[
        Mission(2035, 'Ares 3')]),

    Astronaut('Melissa', 'Lewis', missions=[
        Mission(2030, 'Ares 1'),
        Mission(2035, 'Ares 3')]),

    Astronaut('Rick', 'Martinez', missions=[]),
]

FILE = r'_temporary.csv'


# list[dict]: Using `csv.DictWriter()` save CREW to CSV file
result = ''


for line in CREW:
    if line.missions:
        m = []
        for mission in line.missions:
            vals = [str(x) for x in vars(mission).values()]
            m.append(','.join(vals))
        line.missions = ';'.join(m)
    else:
        line.missions = ''

headers = [str(x) for x in vars(CREW[0]).keys()]

with open(FILE, mode='wt', encoding='utf-8') as file:
    output = csv.DictWriter(
        file,
        fieldnames=headers,
        delimiter=',',
        quoting=csv.QUOTE_ALL,
        lineterminator='\n',
        quotechar='"')
    output.writeheader()
    output.writerows([vars(x) for x in CREW])

