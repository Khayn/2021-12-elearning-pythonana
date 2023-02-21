"""
* Assignment: JSON Object Factory
* Complexity: medium
* Lines of code: 15 lines
* Time: 13 min

English:
    1. Convert from JSON format to Python
    2. Create instances of `Setosa`, `Virginica`, `Versicolor`
       classes based on value in field "species"
    3. Add instances to `result: list[Setosa|Virginica|Versicolor]`
    4. Run doctests - all must succeed

Polish:
    1. Przekonwertuj dane z JSON do Python
    2. Twórz obiekty klas `Setosa`, `Virginica`, `Versicolor`
       w zależności od wartości pola "species"
    3. Dodawaj instancje do `result: list[Setosa|Virginica|Versicolor]`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * `dict.pop()`
    * `globals()`
    * Assignment Expression

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result)
    <class 'list'>
    >>> len(result) > 0
    True
    >>> all(type(row) in (Setosa, Virginica, Versicolor)
    ...     for row in result)
    True
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [Virginica(sepalLength=5.8, sepalWidth=2.7, petalLength=5.1, petalWidth=1.9),
     Setosa(sepalLength=5.1, sepalWidth=3.5, petalLength=1.4, petalWidth=0.2),
     Versicolor(sepalLength=5.7, sepalWidth=2.8, petalLength=4.1, petalWidth=1.3),
     Virginica(sepalLength=6.3, sepalWidth=2.9, petalLength=5.6, petalWidth=1.8),
     Versicolor(sepalLength=6.4, sepalWidth=3.2, petalLength=4.5, petalWidth=1.5),
     Setosa(sepalLength=4.7, sepalWidth=3.2, petalLength=1.3, petalWidth=0.2),
     Versicolor(sepalLength=7.0, sepalWidth=3.2, petalLength=4.7, petalWidth=1.4),
     Virginica(sepalLength=7.6, sepalWidth=3.0, petalLength=6.6, petalWidth=2.1),
     Setosa(sepalLength=4.9, sepalWidth=3.0, petalLength=1.4, petalWidth=0.2)]
"""

import json
from dataclasses import dataclass

FILE = r'_temporary.json'

DATA = """
    [{"sepalLength": 5.8, "sepalWidth": 2.7, "petalLength": 5.1, "petalWidth": 1.9, "species": "virginica"},
     {"sepalLength": 5.1, "sepalWidth": 3.5, "petalLength": 1.4, "petalWidth": 0.2, "species": "setosa"},
     {"sepalLength": 5.7, "sepalWidth": 2.8, "petalLength": 4.1, "petalWidth": 1.3, "species": "versicolor"},
     {"sepalLength": 6.3, "sepalWidth": 2.9, "petalLength": 5.6, "petalWidth": 1.8, "species": "virginica"},
     {"sepalLength": 6.4, "sepalWidth": 3.2, "petalLength": 4.5, "petalWidth": 1.5, "species": "versicolor"},
     {"sepalLength": 4.7, "sepalWidth": 3.2, "petalLength": 1.3, "petalWidth": 0.2, "species": "setosa"},
     {"sepalLength": 7.0, "sepalWidth": 3.2, "petalLength": 4.7, "petalWidth": 1.4, "species": "versicolor"},
     {"sepalLength": 7.6, "sepalWidth": 3.0, "petalLength": 6.6, "petalWidth": 2.1, "species": "virginica"},
     {"sepalLength": 4.9, "sepalWidth": 3.0, "petalLength": 1.4, "petalWidth": 0.2, "species": "setosa"}]"""


@dataclass
class Iris:
    sepalLength: float
    sepalWidth: float
    petalLength: float
    petalWidth: float


class Setosa(Iris):
    pass


class Virginica(Iris):
    pass


class Versicolor(Iris):
    pass


result: list = []
