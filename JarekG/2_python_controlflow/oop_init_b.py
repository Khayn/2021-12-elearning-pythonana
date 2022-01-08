"""
* Assignment: OOP Init Model
* Required: yes
* Complexity: easy
* Lines of code: 12 lines
* Time: 8 min

English:
    1. Modify code below
    2. Values must be passed at the initialization
    3. Create instances of a first class using positional arguments
    4. Create instances of a second class using keyword arguments
    5. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj kod poniżej
    2. Wartości mają być podawane przy inicjalizacji
    3. Twórz instancje pierwszej klasy używając argumentów pozycyjnych
    4. Twórz instancje drugiej klasy używając argumentów nazwanych
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert isinstance(watney, Astronaut)
    >>> assert isinstance(nasa, SpaceAgency)
    >>> assert 'Watney' in vars(watney).values()
    >>> assert 'USA' in vars(watney).values()
    >>> assert '1969-07-21' in vars(watney).values()
    >>> assert 'NASA' in vars(nasa).values()
    >>> assert 'USA' in vars(nasa).values()
    >>> assert '1958-07-29' in vars(nasa).values()
"""


# Watney, USA, 1969-07-21
# NASA, USA, 1958-07-29
from files_to_name import names


class Astronaut:
    def __init__(self, name, country, date, *args, **kwargs):
        self.name = name
        self.country = country
        self.date = date


class SpaceAgency:
    def __init__(self, name=None, country=None, date=None, *args, **kwargs):
        self.name = name
        self.country = country
        self.date = date


watney = Astronaut('Watney', 'USA', '1969-07-21')
watney.name = 'Watney'
watney.country = 'USA'
watney.date = '1969-07-21'

nasa = SpaceAgency()
nasa.name = 'NASA'
nasa.country = 'USA'
nasa.date = '1958-07-29'
