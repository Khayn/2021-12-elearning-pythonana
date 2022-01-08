"""
* Assignment: Type Bool Simple
* Required: yes
* Complexity: easy
* Lines of code: 9 lines
* Time: 5 min

English:
    1. What you need to put in expressions to get the expected outcome?
    2. In place of ellipsis (`...`) insert only `True` or `False`
    3. Run doctests - all must succeed

Polish:
    1. Co należy podstawić w wyrażeniach aby otrzymać wartość oczekiwaną?
    2. W miejsce trzech kropek (`...`) wstawiaj tylko `True` lub `False`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert a is not Ellipsis, 'Assign result to variable: `a`'
    >>> assert b is not Ellipsis, 'Assign result to variable: `b`'
    >>> assert c is not Ellipsis, 'Assign result to variable: `c`'
    >>> assert d is not Ellipsis, 'Assign result to variable: `d`'
    >>> assert e is not Ellipsis, 'Assign result to variable: `e`'
    >>> assert f is not Ellipsis, 'Assign result to variable: `f`'
    >>> assert g is not Ellipsis, 'Assign result to variable: `g`'
    >>> assert h is not Ellipsis, 'Assign result to variable: `h`'
    >>> assert i is not Ellipsis, 'Assign result to variable: `i`'
    >>> assert type(a) is bool, 'Variable `a` has invalid type, should be bool'
    >>> assert type(b) is bool, 'Variable `b` has invalid type, should be bool'
    >>> assert type(c) is bool, 'Variable `c` has invalid type, should be bool'
    >>> assert type(d) is bool, 'Variable `d` has invalid type, should be bool'
    >>> assert type(e) is bool, 'Variable `e` has invalid type, should be bool'
    >>> assert type(f) is bool, 'Variable `f` has invalid type, should be bool'
    >>> assert type(g) is bool, 'Variable `g` has invalid type, should be bool'
    >>> assert type(h) is bool, 'Variable `h` has invalid type, should be bool'
    >>> assert type(i) is bool, 'Variable `i` has invalid type, should be bool'

    >>> bool(a)
    True
    >>> bool(b)
    True
    >>> bool(c)
    False
    >>> bool(d)
    True
    >>> bool(e)
    True
    >>> bool(f)
    False
    >>> bool(g)
    True
    >>> bool(h)
    True
    >>> bool(i)
    False
"""

# bool: the expression result must be True
a = True == True

# bool: the expression result must be True
b = True != False

# bool: the expression result must be False
c = not True

# bool: the expression result must be True
d = bool(True) == True

# bool: the expression result must be True
e = bool(False) == False

# bool: the expression result must be False
f = False or False

# bool: the expression result must be True
g = True and True

# bool: the expression result must be True
h = bool(bool(True) == True) or False

# bool: the expression result must be False
i = bool(False) is not bool(False)

# Solution
a = True == True
b = True != False
c = not True
d = bool(True) == True
e = bool(False) == False
f = False or False
g = True and True
h = bool(bool(False) == False) or False
i = bool(False) is not bool(False)
