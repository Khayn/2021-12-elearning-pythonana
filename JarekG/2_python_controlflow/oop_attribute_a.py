"""
* Assignment: OOP Attribute Model
* Required: yes
* Complexity: easy
* Lines of code: 12 lines
* Time: 8 min

English:
    1. Modify code below
    2. Add attibutes to model the data:
       a. Watney, USA, 1969-07-21
       b. NASA, USA, 1958-07-29
    3. Create instances (watney, nasa) filling it with data
    4. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj kod poniżej
    2. Dodaj atrybuty by zamodelować dane:
       a. Watney, USA, 1969-07-21
       b. NASA, USA, 1958-07-29
    3. Stwórz instancje (watney, nasa) wypełniając je danymi
    4. Uruchom doctesty - wszystkie muszą się powieść

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


class Astronaut:
    def __init__(self):
        # self.Watney = 'Watney, USA, 1969-07-21'
        self.name = 'Watney'
        self.country = 'USA'
        self.date = '1969-07-21'


class SpaceAgency:
    def __init__(self):
        self.name = 'NASA'
        self.country = 'USA'
        self.date = '1958-07-29'


watney = Astronaut()
nasa = SpaceAgency()
