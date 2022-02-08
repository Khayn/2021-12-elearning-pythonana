"""
* Assignment: Function Generator Chain
* Required: yes
* Complexity: easy
* Lines of code: 9 lines
* Time: 8 min

English:
    1. Use generator expression to create `numbers`
    2. In generator use `range()` to get numbers from 1 to 33
       (inclusive) divisible by 3
    3. Use `filter()` to get odd numbers from `numbers`
    4. Use `map()` to cube all numbers in `numbers`
    5. Create `result: float` with arithmetic mean of `numbers`
    6. Do not use `lambda` expressions
    7. Run doctests - all must succeed

Polish:
    1. Użyj wyrażenia generatorowego do stworzenia `numbers`
    2. W generatorze użyj `range()` aby otrzymać liczby od 1 do 33
       (włącznie) podzielne przez 3
    3. Użyj `filter()` aby otrzymać liczby nieparzyste z `numbers`
    4. Użyj `map()` aby podnieść wszystkie liczby w `numbers` do sześcianu
    5. Stwórz `result: float` ze średnią arytmetyczną z `numbers`
    6. Nie używaj wyrażeń lambda
    7. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * type cast to `list()` to expand generator before calculating mean
    * `mean = sum(...) / len(...)`
    * TypeError: object of type 'map' has no len()
    * ZeroDivisionError: division by zero

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> isfunction(odd)
    True
    >>> isfunction(cube)
    True
    >>> type(result) is float
    True
    >>> result
    11502.0
"""
