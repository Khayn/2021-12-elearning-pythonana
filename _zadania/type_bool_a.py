"""
* Assignment: Type Bool True or False
* Required: yes
* Complexity: easy
* Lines of code: 16 lines
* Time: 5 min

English:
    1. Which variables are `True`?
    2. Which variables are `False`?
    3. Run doctests - all must succeed

Polish:
    1. Które zmienne są `True`?
    2. Które zmienne są `False`?
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
    >>> assert j is not Ellipsis, 'Assign result to variable: `j`'
    >>> assert k is not Ellipsis, 'Assign result to variable: `k`'
    >>> assert l is not Ellipsis, 'Assign result to variable: `l`'
    >>> assert m is not Ellipsis, 'Assign result to variable: `m`'
    >>> assert n is not Ellipsis, 'Assign result to variable: `n`'
    >>> assert o is not Ellipsis, 'Assign result to variable: `o`'
    >>> assert n is not Ellipsis, 'Assign result to variable: `n`'
    >>> assert p is not Ellipsis, 'Assign result to variable: `p`'
    >>> assert q is not Ellipsis, 'Assign result to variable: `q`'
    >>> assert type(a) is bool, 'Variable `a` has invalid type, should be bool'
    >>> assert type(b) is bool, 'Variable `b` has invalid type, should be bool'
    >>> assert type(c) is bool, 'Variable `c` has invalid type, should be bool'
    >>> assert type(d) is bool, 'Variable `d` has invalid type, should be bool'
    >>> assert type(e) is bool, 'Variable `e` has invalid type, should be bool'
    >>> assert type(f) is bool, 'Variable `f` has invalid type, should be bool'
    >>> assert type(g) is bool, 'Variable `g` has invalid type, should be bool'
    >>> assert type(h) is bool, 'Variable `h` has invalid type, should be bool'
    >>> assert type(i) is bool, 'Variable `i` has invalid type, should be bool'
    >>> assert type(j) is bool, 'Variable `j` has invalid type, should be bool'
    >>> assert type(k) is bool, 'Variable `k` has invalid type, should be bool'
    >>> assert type(l) is bool, 'Variable `l` has invalid type, should be bool'
    >>> assert type(m) is bool, 'Variable `m` has invalid type, should be bool'
    >>> assert type(n) is bool, 'Variable `n` has invalid type, should be bool'
    >>> assert type(o) is bool, 'Variable `o` has invalid type, should be bool'
    >>> assert type(p) is bool, 'Variable `p` has invalid type, should be bool'
    >>> assert type(q) is bool, 'Variable `q` has invalid type, should be bool'

    >>> a
    False
    >>> b
    True
    >>> c
    False
    >>> d
    False
    >>> e
    False
    >>> f
    False
    >>> g
    True
    >>> h
    True
    >>> i
    True
    >>> j
    True
    >>> k
    False
    >>> l
    True
    >>> m
    False
    >>> n
    False
    >>> o
    False
    >>> p
    True
    >>> q
    False
"""

a = bool(False)
b = bool(True)

c = bool(0)
d = bool(0.0)
e = bool(-0)
f = bool(-0.0)

g = bool('a')
h = bool('.')
i = bool('0')
j = bool('0.0')
k = bool('')
l = bool(' ')

m = bool(int('0'))
n = bool(float(str(-0)))

o = bool(-0.0 + 0.0j)
p = bool('-0.0+0.0j')
q = bool(complex('-0.0+0.0j'))
