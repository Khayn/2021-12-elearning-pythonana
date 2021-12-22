# %% typy w Python

x = 1  # int
x = 1.5  # float
x = 'hello'  # str
x = True  # bool
x = None  # NoneType
x = []  # list
x = ()  # tuple
x = set()  # set
x = {}  # dict


# %%

# Alan Turing
# Turing complete

# przypisanie
x = 1

# porównanie
if x == 1:
    ...

# powtórzenie
while ...:
    ...

for ... in ...:
    ...



# %% conditionals

# funkcja input() zawsze zwraca str

x = 1  # przyrównanie, ustawia x na 1
x == 1  # porównanie, czy x jest równy 1


x = 1

if x == 1:
    print('Tak, ma wartość 1')
    print('Tak, ma wartość 1')
    print('Tak, ma wartość 1')

    if x % 2 == 0:
        print('ok')
        print('ok')
        print('ok')
        print('ok')
    else:
        print('nie ok')
        print('nie ok')
        print('nie ok')
        print('nie ok')

    print('Tak, ma wartość 1')
    print('Tak, ma wartość 1')
    print('Tak, ma wartość 1')
else:
    print('Nie ma wartości 1')
    print('Nie ma wartości 1')
    print('Nie ma wartości 1')
    print('Nie ma wartości 1')
    print('Nie ma wartości 1')




age = input('Podaj wiek')
if int(age) > 18:
    print('pełnoletni')
else:
    print('niepełnoletni')
# pełnoletni



age = int(input('Podaj wiek'))

if age >= 65:
    print('senior')
elif 30 <= age < 65:
    print('dojrzały dorosły')
elif 18 <= age < 30:
    print('młody dorosły')
elif age < 18:
    print('dziecko')


#

lang = input('Wprowadź język: ')

if lang == 'English':
    print('Hello')
elif lang == 'Polish':
    print('Witaj')
elif lang == 'German':
    print('Guten Tag')

#

lang = input('Wprowadź język: ')

match lang:
    case 'English':  print('hello')
    case 'Polish':   print('witaj')
    case 'German':   print('Guten Tag')
    case _:          print('Nie znam języka')
