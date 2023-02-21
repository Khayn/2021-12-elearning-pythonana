"""
* Assignment: Sequence Slice Text
* Required: yes
* Complexity: easy
* Lines of code: 8 lines
* Time: 8 min

English:
    1. Remove title and military rank in each variable
    2. Remove also whitespaces at the beginning and end of a text
    3. Use only `slice` to clean text
    4. Run doctests - all must succeed

Polish:
    1. Usuń tytuł naukowy i stopień wojskowy z każdej zmiennej
    2. Usuń również białe znaki na początku i końcu tekstu
    3. Użyj tylko `slice` do oczyszczenia tekstu
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert a is not Ellipsis, \
    'Assign result to variable: `a`'
    >>> assert b is not Ellipsis, \
    'Assign result to variable: `b`'
    >>> assert c is not Ellipsis, \
    'Assign result to variable: `c`'
    >>> assert d is not Ellipsis, \
    'Assign result to variable: `d`'
    >>> assert e is not Ellipsis, \
    'Assign result to variable: `e`'
    >>> assert f is not Ellipsis, \
    'Assign result to variable: `f`'
    >>> assert g is not Ellipsis, \
    'Assign result to variable: `g`'
    >>> assert type(a) is str, \
    'Variable `a` has invalid type, should be str'
    >>> assert type(b) is str, \
    'Variable `b` has invalid type, should be str'
    >>> assert type(c) is str, \
    'Variable `c` has invalid type, should be str'
    >>> assert type(d) is str, \
    'Variable `d` has invalid type, should be str'
    >>> assert type(e) is str, \
    'Variable `e` has invalid type, should be str'
    >>> assert type(f) is str, \
    'Variable `f` has invalid type, should be str'
    >>> assert type(g) is str, \
    'Variable `g` has invalid type, should be str'

    >>> example
    'Mark Watney'
    >>> a
    'Jan Twardowski'
    >>> b
    'Jan Twardowski'
    >>> c
    'Mark Watney'
    >>> d
    'Melissa Lewis'
    >>> e
    'Ryan Stone'
    >>> f
    'Ryan Stone'
    >>> g
    'Jan Twardowski'
"""

EXAMPLE = 'lt. Mark Watney, PhD'
A = 'dr hab. inż. Jan Twardowski, prof. AATC'
B = 'gen. pil. Jan Twardowski'
C = 'Mark Watney, PhD'
D = 'lt. col. ret. Melissa Lewis'
E = 'dr n. med. Ryan Stone'
F = 'Ryan Stone, MD-PhD'
G = 'lt. col. Jan Twardowski\t'

example = EXAMPLE[4:-5]

# str: expected result: 'Jan Twardowski'
a = A[13:27]
print(a)
# str: expected result: 'Jan Twardowski'
b = B[10:]
print(b)

# str: expected result: 'Mark Watney'
c = C[:11]
print(c)

# str: expected result: 'Melissa Lewis'
d = D[14:]
print(d)
# str: expected result: 'Ryan Stone'
e = E[11:]
print(e)
# str: expected result: 'Ryan Stone'
f = F[:10]
print(f)
# str: expected result: 'Jan Twardowski'
g = G[9:23]
print(g)