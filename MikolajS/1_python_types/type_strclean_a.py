"""
* Assignment: String Clean Strings
* Required: yes
* Complexity: easy
* Lines of code: 8 lines
* Time: 13 min

English:
    1. Expected value is `Pana Twardowskiego III`
    2. Use only `str` methods to clean each variable
    3. Discuss how to create generic solution which fit all cases
    4. Implementation of such generic function will be in
       `Function Arguments Clean` chapter
    5. Run doctests - all must succeed

Polish:
    1. Oczekiwana wartość `Pana Twardowskiego III`
    2. Wykorzystaj tylko metody `str` do oczyszczenia każdej zmiennej
    3. Przeprowadź dyskusję jak zrobić rozwiązanie generyczne pasujące
       do wszystkich przypadków
    4. Implementacja takiej generycznej funkcji będzie w rozdziale
       `Function Arguments Clean`
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert example is not Ellipsis, \
    'Assign result to variable: `example`'
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
    >>> assert h is not Ellipsis, \
    'Assign result to variable: `h`'
    >>> assert i is not Ellipsis, \
    'Assign result to variable: `i`'
    >>> assert type(example) is str, \
    'Variable `example` has invalid type, should be str'
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
    >>> assert type(h) is str, \
    'Variable `h` has invalid type, should be str'
    >>> assert type(i) is str, \
    'Variable `i` has invalid type, should be str'

    >>> example
    'Pana Twardowskiego III'
    >>> a
    'Pana Twardowskiego III'
    >>> b
    'Pana Twardowskiego III'
    >>> c
    'Pana Twardowskiego III'
    >>> d
    'Pana Twardowskiego III'
    >>> e
    'Pana Twardowskiego III'
    >>> f
    'Pana Twardowskiego III'
    >>> g
    'Pana Twardowskiego III'
    >>> h
    'Pana Twardowskiego III'
    >>> i
    'Pana Twardowskiego III'
"""

EXAMPLE = 'UL. Pana \tTWArdoWskIEGO 3'
A = 'ul Pana TwaRDOWSkiego III'
B = '\tul. Pana Twardowskiego trzeciego'
C = 'ulicaPana Twardowskiego III'
D = 'Pana \nTWARDOWSKIEGO 3'
E = 'UL. Pana TWARDowsKIEGO III'
F = 'ULICA Pana TWARDOWSKIEGO III '
G = 'ULICA. Pana TWARDowsKIEGO III'
H = ' Pana Twardowskiego 3 '
I = 'Pana\tTwardowskiego III '

example = EXAMPLE.upper().replace('UL. ', '').replace('\t', '') \
    .strip().title().replace('3', 'III')

def char_cleaning_fun(str_input):
    ul_rep = ['ulica', 'ul.', 'ul', 'UL.', 'ULICA.', 'ULICA']
    three_rep = ['3', 'Trzeciego', 'Trzeci', 'Iii', 'lll']

    str_input = str_input.strip().replace('\t', ' ').replace('\n', '')

    for ch in ul_rep:
        str_input = str_input.replace(ch, '')

    str_input = str_input.title()

    for number in three_rep:
        str_input = str_input.replace(number, 'III')

    return str_input.strip()

# str: expected string is 'Pana Twardowskiego III'
a = char_cleaning_fun(A)

# str: expected string is 'Pana Twardowskiego III'
b = char_cleaning_fun(B)

# str: expected string is 'Pana Twardowskiego III'
c = char_cleaning_fun(C)

# str: expected string is 'Pana Twardowskiego III'
d = char_cleaning_fun(D)

# str: expected string is 'Pana Twardowskiego III'
e = char_cleaning_fun(E)

# str: expected string is 'Pana Twardowskiego III'
f = char_cleaning_fun(F)

# str: expected string is 'Pana Twardowskiego III'
g = char_cleaning_fun(G)

# str: expected string is 'Pana Twardowskiego III'
h = char_cleaning_fun(H)

# str: expected string is 'Pana Twardowskiego III'
i = char_cleaning_fun(I)
