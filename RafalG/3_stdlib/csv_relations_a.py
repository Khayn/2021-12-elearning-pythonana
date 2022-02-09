"""
* Assignment: CSV Relations Nested
* Complexity: medium
* Lines of code: 14 lines
* Time: 13 min

English:
    1. Convert `DATA` to format with one column per each attrbute for example:
       a. `mission1_year`, `mission2_year`,
       b. `mission1_name`, `mission2_name`
    2. Note, that enumeration starts with one
    3. Sort `fieldnames`
    4. Save data to `FILE`
    5. Run doctests - all must succeed

Polish:
    1. Przekonweruj `DATA` do formatu z jedną kolumną dla każdego atrybutu, np:
       a. `mission1_year`, `mission2_year`,
       b. `mission1_name`, `mission2_name`
    2. Zwróć uwagę, że enumeracja zaczyna się od jeden
    3. Posortuj `fieldnames`
    4. Zapisz dane do `FILE`
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove
    >>> result = open(FILE).read()
    >>> remove(FILE)

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> print(result)
    "firstname","lastname","mission1_name","mission1_year","mission2_name","mission2_year"
    "Mark","Watney","Ares3","2035","",""
    "Melissa","Lewis","Ares1","2030","Ares3","2035"
    "Rick","Martinez","","","",""
    <BLANKLINE>
"""

import csv

FILE = r'_temporary.csv'

DATA = [
    {"firstname": "Mark", "lastname": "Watney", "missions": [
        {"year": "2035", "name": "Ares3"}]},

    {"firstname": "Melissa", "lastname": "Lewis", "missions": [
         {"year": "2030", "name": "Ares1"},
         {"year": "2035", "name": "Ares3"}]},

    {"firstname": "Rick", "lastname": "Martinez", "missions": []}
]

# list[dict]: flatten data, each mission field prefixed with mission and number
# result = ...

header = set()
data = []

for astronaut in DATA:
    mission_number = 0
    missions = astronaut.pop("missions")
    header.update(astronaut.keys())

    for mission in missions:
        mission_number += 1
        a = f"mission{mission_number}_name"
        b = f"mission{mission_number}_year"
        # header.update((f"mission{mission_number}_name", f"mission{mission_number}_year"))
        header.update((a, b))

        astronaut.update({f"mission{mission_number}_name": mission.get("name"),
                          f"mission{mission_number}_year": mission.get("year")})

    # print(astronaut)
    data.append(astronaut)


with open(FILE, mode='w', encoding='utf-8') as file:
    f = csv.DictWriter(file, fieldnames=sorted(header), delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL,
                       lineterminator='\n')
    f.writeheader()
    f.writerows(data)