"""
* Assignment: Sequence UnpackStar List
* Required: yes
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Separate ip address from host names
    2. Use asterisk `*` notation
    3. Run doctests - all must succeed

Polish:
    1. Odseparuj adres ip od nazwy hostów
    2. Skorzystaj z notacji z gwiazdką `*`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `str.split()` without any argument

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(ip)
    <class 'str'>
    >>> type(hosts)
    <class 'list'>
    >>> assert all(type(host) is str for host in hosts)
    >>> '' not in hosts
    True
    >>> ip
    '10.13.37.1'
    >>> hosts
    ['nasa.gov', 'esa.int', 'roscosmos.ru']
"""

DATA = ['10.13.37.1', 'nasa.gov', 'esa.int', 'roscosmos.ru']

# str: ip address: '10.13.37.1'

# list[str]: list of host names: ['nasa.gov', 'esa.int', 'roscosmos.ru']
ip = str(DATA[0])
hosts = (DATA[1:])
print(f'\tip= {ip}\n   hosts={hosts} \n')
