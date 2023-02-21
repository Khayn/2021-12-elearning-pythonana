"""
* Assignment: Function Definition Print
* Required: yes
* Complexity: easy
* Lines of code: 5 lines
* Time: 3 min

English:
    1. Define function `call` without parameters
    2. Function appends `Beetlejuice` to `results`
    3. Call function three times
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `call` bez parametrów
    2. Funkcja dodaje `Beetlejuice` do `result`
    3. Wywołaj funkcję trzy razy
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> isfunction(call)
    True
    >>> result
    ['Beetlejuice', 'Beetlejuice', 'Beetlejuice']
"""

result = []

def call():
    result.append('Beetlejuice')
    return result


call()
call()
call()
print(result)