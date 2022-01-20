"""
* Assignment: SQLite3 Join Relations
* Complexity: medium
* Lines of code: 15 lines
* Time: 21 min

English:
    1. Connect to database:
        a. Set returned result type to `sqlite3.Row`
        b. Get cursor and next things execute on it
        c. Execute `SQL_CREATE_TABLE_ASTRONAUT` to create table `astronauts`
        d. Execute `SQL_CREATE_TABLE_ADDRESS` to create table `addresses`
        e. Execute `SQL_CREATE_INDEX_ASTRONAUT_LASTNAME` to create index
    2. Iterate over `DATA`:
        a. Seprate `addresses` from other values
        b. Execute `SQL_INSERT_ASTRONAUT` to insert astroanut to database
        c. Get `id` of the last inserted row (`cursor.lastrowid`)
        d. Add `id` to each address
        e. Executing `SQL_INSERT_ADDRESS` insert `addresses` to database
    3. Executing `SQL_SELECT` select data from database:
        a. Join data from both tables
        b. Append each row to `result: list[dict]`
    4. Run doctests - all must succeed

Polish:
    1. Połącz się do bazy danych:
        a. Ustaw typ zwracanych wyników na `sqlite3.Row`
        b. Pobierz kursor i następne polecenia wykonuj na nim
        c. Wykonując `SQL_CREATE_TABLE_ASTRONAUT` stwórz tabelę `astronauts`
        d. Wykonując `SQL_CREATE_TABLE_ADDRESS` stwórz tabelę `addresses`
        e. Wykonując `SQL_CREATE_INDEX_ASTRONAUT_LASTNAME` stwórz indeks
    2. Iteruj po `DATA`:
        a. Oddziel `addresses` od pozostałych wartości
        b. Wykonując `SQL_INSERT_ASTRONAUT` wstaw astronautę do bazy
        c. Pobierz `id` ostatniego wstawianego wiersza (`cursor.lastrowid`)
        d. Dodaj to `id` do każdego adresu
        e. Wykonując `SQL_INSERT_ADDRESS` wstaw adresy do bazy danych
    3. Wykonując `SQL_SELECT` wybierz dane z bazy:
        a. Połącz dane z obu tabel
        b. Dodaj każdy rekord do `result: list[dict]`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `cursor = db.cursor()`
    * `astronaut_id = cursor.lastrowid`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result)
    <class 'list'>
    >>> len(result) > 0
    True
    >>> all(type(row) is dict
    ...     for row in result)
    True

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [{'id': 1, 'firstname': 'José', 'lastname': 'Jiménez', 'astronaut_id': 1, 'street': '2101 E NASA Pkwy', 'city': 'Houston', 'state': 'Texas', 'code': 77058, 'country': 'USA'},
     {'id': 1, 'firstname': 'José', 'lastname': 'Jiménez', 'astronaut_id': 1, 'street': None, 'city': 'Kennedy Space Center', 'state': 'Florida', 'code': 32899, 'country': 'USA'},
     {'id': 2, 'firstname': 'Mark', 'lastname': 'Watney', 'astronaut_id': 2, 'street': '4800 Oak Grove Dr', 'city': 'Pasadena', 'state': 'California', 'code': 91109, 'country': 'USA'},
     {'id': 2, 'firstname': 'Mark', 'lastname': 'Watney', 'astronaut_id': 2, 'street': '2825 E Ave P', 'city': 'Palmdale', 'state': 'California', 'code': 93550, 'country': 'USA'},
     {'id': 3, 'firstname': 'Иван', 'lastname': 'Иванович', 'astronaut_id': 3, 'street': '', 'city': 'Космодро́м Байкону́р', 'state': 'Кызылординская область', 'code': None, 'country': 'Қазақстан'},
     {'id': 5, 'firstname': 'Alex', 'lastname': 'Vogel', 'astronaut_id': 5, 'street': 'Linder Hoehe', 'city': 'Köln', 'state': None, 'code': 51147, 'country': 'Germany'}]
"""

import sqlite3

DATABASE = ':memory:'

DATA = [
    {"firstname": "José", "lastname": "Jiménez", "addresses": [
        {"street": "2101 E NASA Pkwy", "code": 77058, "city": "Houston", "state": "Texas", "country": "USA"},
        {"street": None, "code": 32899, "city": "Kennedy Space Center", "state": "Florida", "country": "USA"}]},

    {"firstname": "Mark", "lastname": "Watney", "addresses": [
        {"street": "4800 Oak Grove Dr", "code": 91109, "city": "Pasadena", "state": "California", "country": "USA"},
        {"street": "2825 E Ave P", "code": 93550, "city": "Palmdale", "state": "California", "country": "USA"}]},

    {"firstname": "Иван", "lastname": "Иванович", "addresses": [
        {"street": "", "code": None, "city": "Космодро́м Байкону́р", "state": "Кызылординская область", "country": "Қазақстан"}]},

    {"firstname": "Melissa", "lastname": "Lewis", "addresses": []},

    {"firstname": "Alex", "lastname": "Vogel", "addresses": [
        {"street": "Linder Hoehe", "city": "Köln", "code": 51147, "state": None, "country": "Germany"}]}
]

SQL_CREATE_TABLE_ASTRONAUT = """
    CREATE TABLE IF NOT EXISTS astronaut (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        firstname TEXT,
        lastname TEXT);"""

SQL_CREATE_TABLE_ADDRESS = """
    CREATE TABLE IF NOT EXISTS address (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        astronaut_id INTEGER,
        street TEXT,
        city TEXT,
        state TEXT,
        code INTEGER,
        country TEXT);"""

SQL_CREATE_INDEX_ASTRONAUT_LASTNAME = """
    CREATE INDEX IF NOT EXISTS lastname_index ON astronaut (lastname);"""

SQL_INSERT_ASTRONAUT = """
    INSERT INTO astronaut VALUES (
        NULL,
        :firstname,
        :lastname);"""

SQL_INSERT_ADDRESS = """
    INSERT INTO address VALUES (
        NULL,
        :astronaut_id,
        :street,
        :city,
        :state,
        :code,
        :country);"""

SQL_SELECT = """
    SELECT *
    FROM astronaut
    JOIN address
    ON astronaut.id=address.astronaut_id;"""


# list[tuple]: select all results from database in list[dict] format, example:
#              [{'id': 1, 'firstname': 'José', 'lastname': 'Jiménez',
#                'astronaut_id': 1, 'street': '2101 E NASA Pkwy', 'city':
#                'Houston', 'state': 'Texas', 'code': 77058, 'country': 'USA'},
#               ...]
result = ...
