"""
* Assignment: Loop Dict Label Encoder
* Required: no
* Complexity: hard
* Lines of code: 9 lines
* Time: 13 min

English:
    1. Define:
        a. `features: list[tuple]` - measurements
        b. `labels: list[int]` - species
        c. `label_encoder: dict[int, str]`
            dictionary with encoded (as numbers) species names
    2. Separate header from data
    3. To encode and decode `labels` (species) we need:
        a. Define `label_encoder: dict[int, str]`
        b. key - id (incremented integer value)
        c. value - species name
    4. `label_encoder` must be generated from `DATA`
    5. For each row append to `features`, `labels` and `label_encoder`
    6. Run doctests - all must succeed

Polish:
    1. Zdefiniuj:
        a. `features: list[tuple]` - pomiary
        b. `labels: list[int]` - gatunki
        c. `label_encoder: dict[int, str]`
            słownik zakodowanych (jako cyfry) nazw gatunków
    2. Odseparuj nagłówek od danych
    3. Aby móc zakodować i odkodować `labels` (gatunki) potrzebujesz:
        a. Zdefiniuj `label_encoder: dict[int, str]`:
        b. key - identyfikator (kolejna liczba rzeczywista)
        c. value - nazwa gatunku
    4. `label_encoder` musi być wygenerowany z `DATA`
    5. Dla każdego wiersza dodawaj do `feature`, `labels` i `label_encoder`
    6. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * Reversed lookup dict

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(features) is list
    >>> assert type(labels) is list
    >>> assert type(label_encoder) is dict
    >>> assert all(type(x) is tuple for x in features)
    >>> assert all(type(x) is int for x in labels)
    >>> assert all(type(x) is int for x in label_encoder.keys())
    >>> assert all(type(x) is str for x in label_encoder.values())

    >>> features  # doctest: +NORMALIZE_WHITESPACE
    [(5.8, 2.7, 5.1, 1.9),
     (5.1, 3.5, 1.4, 0.2),
     (5.7, 2.8, 4.1, 1.3),
     (6.3, 2.9, 5.6, 1.8),
     (6.4, 3.2, 4.5, 1.5),
     (4.7, 3.2, 1.3, 0.2)]
    >>> labels
    [0, 1, 2, 0, 2, 1]
    >>> label_encoder  # doctest: +NORMALIZE_WHITESPACE
    {0: 'virginica',
     1: 'setosa',
     2: 'versicolor'}
"""

DATA = [
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]

# list[tuple]: values from column 0-3 from DATA without header
features = [
    tuple(feat for feat in line[:-1])
    for line in DATA[1:]
]

# list[str]: species name from column 4 from DATA without header
labels = [label for line in DATA[1:] for label in line[-1:]]


# dict[int,str]: lookup dict generated from species names
label_encoder = {label for label in labels}
label_encoder = {k: v for k, v in enumerate(label_encoder)}

labels = [k for label in labels for k, v in label_encoder.items() if label == v]

# ======== Matt solution =============


headers, *data = DATA

features = []
labels = []
label_encoder = {}

for *X, y in data:
    if y not in label_encoder:
        label_encoder[y] = len(label_encoder)
        
    labels.append(label_encoder[y])
    features.append(tuple(X))
    
label_encoder = {val: key for key, val in label_encoder.items()}

