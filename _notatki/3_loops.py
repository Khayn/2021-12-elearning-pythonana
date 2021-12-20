# while - while, for
# for - forEach

# %% while

data = ['a', 'b', 'c']

data[0].upper()
'A'
data[1].upper()
'B'
data[2].upper()
'C'


i = 0

if i < len(data):
    data[i].upper()
    i += 1

if i < len(data):
    data[i].upper()
    i += 1

if i < len(data):
    data[i].upper()
    i += 1

if i < len(data):
    data[i].upper()
    i += 1

i = 0
while i < len(data):
    x = data[i].upper()
    print(x)
    i += 1


# 12 - maks ludzkiego oka
# 24 fps - filmy
# 60 fps - gry lub filmy 4k
# 120 fps - nowe gry

# while True:
#     try:
#         ...
#     except KeyboardInterrupt:
#         ...

# %% for

data = ['a', 'b', 'c']

for letter in data:
    print(letter.upper())


#

*features, label = (5.1, 3.5, 1.4, 0.2, 'setosa')

features
[5.1, 3.5, 1.4, 0.2]

label
'setosa'

#

DATA = [
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]

for *features, label in DATA[1:]:
    avg = sum(features) / len(features)
    print(f'{avg=}, {label=}')

avg=3.88, label='virginica'
avg=2.55, label='setosa'
avg=3.48, label='versicolor'
avg=4.15, label='virginica'
avg=3.90, label='versicolor'
avg=2.35, label='setosa'

#

DATA = [
    {'Sepal length': 5.1, 'Sepal width': 3.5, 'Species': 'setosa'},
    {'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
    {'Sepal length': 6.3, 'Petal width': 1.8, 'Species': 'virginica'},
    {'Sepal length': 5.0, 'Petal width': 0.2, 'Species': 'setosa'},
    {'Sepal width': 2.8, 'Petal length': 4.1, 'Species': 'versicolor'},
    {'Sepal width': 2.9, 'Petal width': 1.8, 'Species': 'virginica'},
]

for row in DATA:
    for key, value in row.items():
        print(f'{key=: >15}, {value=}')



# %% comprehension

# w Python jest konwencja
# dolny element jest włącznie
# górny element jest rozłącznie
# np. range(0,3) -> 0, 1, 2


# bardzo ważne w analizie danych
# to jest nadużywane w analizie danych
# częściej wykorzystywane niż zwykłe pętle w Python

# nie tylko generują listy, ale również inne


result = [x for x in range(0,5)]
# x
# NameError: name 'x' is not defined


[x**2 for x in range(0,5)]
[0, 1, 4, 9, 16]
result = []
for x in range(0,5):
    result.append(x**2)

result
[0, 1, 4, 9, 16]
result = [x**2 for x in range(0,5)]
result = [float(x) for x in range(0,5)]
result
[0.0, 1.0, 2.0, 3.0, 4.0]







DATA = [
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]


[sum(X)/len(X) for *X,y in DATA[1:] if y=='setosa']
[2.55, 2.35]


result = [(species, avg)
          for *values, species in DATA[1:]
          if species == 'setosa'
          and (avg := sum(values) / len(values))]




DATA = [
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]


all(observation > 1.0
    for *values, species in DATA[1:]
    for observation in values
    if type(observation) is float)
False


any(observation > 1.0
    for *values, species in DATA[1:]
    for observation in values
    if type(observation) is float)
True

# cognitive complexity
