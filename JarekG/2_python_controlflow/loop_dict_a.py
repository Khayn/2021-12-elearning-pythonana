"""
* Assignment: Loop Dict To Dict
* Required: yes
* Complexity: easy
* Lines of code: 3 lines
* Time: 8 min

English:
    1. Convert to `result: dict[str, str]`
    2. Run doctests - all must succeed

Polish:
    1. Przekonwertuj do `result: dict[str, str]`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result)
    <class 'dict'>

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'Doctorate': '6',
     'Prof-school': '6',
     'Masters': '5',
     'Bachelor': '5',
     'Engineer': '5',
     'HS-grad': '4',
     'Junior High': '3',
     'Primary School': '2',
     'Kindergarten': '1'}
"""

DATA = {
    6: ['Doctorate', 'Prof-school'],
    5: ['Masters', 'Bachelor', 'Engineer'],
    4: ['HS-grad'],
    3: ['Junior High'],
    2: ['Primary School'],
    1: ['Kindergarten'],
}

# dict[str,str]: converted DATA. Note values are str not int!
result = {
    k: str(v)
    for v, v_list in DATA.items()
    for k in v_list
}
