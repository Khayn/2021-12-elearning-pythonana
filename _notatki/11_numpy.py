# 1. typy (int, float, int8, int32, int64, uint8, uint32, uint64), atrybutów itp

# uint8 = 2 ** 8
# int8 = (2**8) / 2

# liczba 69 w  8 bit = 01000101
# liczba 69 w 32 bit = 00000000 00000000 00000000 01000101
# liczba 69 w 64 bit = 00000000 00000000 00000000 00000000 00000000 00000000 00000000 01000101

# 2. Atrybuty

# a.size
# a.shape - najważniejsze
# a.data
# a.strides
# a.itemsize
# a.ndim


# 3. axis to index w shape
# nowe wymiary przychodzą na początek

# dla jednowymiarowych
# axis=0 -> kolumny
# axis=-1 -> kolumny

# dla dwuwymiarowych
# axis=0 -> a.shape[0] - wierszy
# axis=1 -> a.shape[1] - kolumny
# axis=-2 -> wiersze
# axis=-1 -> kolumny

# dla trójwymiarowych
# axis=0 -> głębokość
# axis=1 -> wiersze
# axis=2 -> kolumny
# axis=-3 -> głębokość
# axis=-2 -> wiersze
# axis=-1 -> kolumny

# dla czterowymiarowych
# axis=0 -> czas
# axis=1 -> głębokość
# axis=2 -> wiersze
# axis=3 -> kolumny
# axis=-4 -> czas
# axis=-3 -> głębokość
# axis=-2 -> wiersze
# axis=-1 -> kolumny


import numpy as np


a = np.arange(0,50).reshape(10,5)


# 4. Indeksy numeryczne

# - int

a[0]

# list[int]

a[ [0,1,2] ]

# tuple[list[int], int]

a[ [0,1,2], 0 ]

# tuple[list[int], list[int]]

a[ [0,1,2], [3,1,2] ]

# - tuple[int,int]

a[0,1]

# - slice

a[0:5]
a[:10]
a[5:]
a[0:10:2]
a[::2]
a[:]

# - tuple[slice,int]
a[0:5, 2]

# tuple[slice, list[int]]

a[0:5, [1,2,3]]

# tuple[slice, slice]

a[0:5, 1:3]


# 5. Indeksy logiczne

# - bool

a[True]

# - list[bool]

a[ [True,False,False,True,True,False,True,False,True,True] ]

# - tuple[list[bool], list[bool]]
a[ [True,False,False,True,True,False,True,False,True,True], [False,False,True,False,True] ]


# 6. Fancy indexing

a[ a%2==0 ]

a[ (a%2==0) & (a>30) ]


# and
# True and True == True
# False and True == False
# True and False == False
# False and False == False
a[ (a%2==0) & (a>30) ]

# or
# True and True == True
# False and True == True
# True and False == True
# False and False == False
a[ (a%2==0) | (a>30) ]

# xor
# True and True == False
# False and True == True
# True and False == True
# False and False == False

a[ (a%2==0) ^ (a>30) ]

# negation
# ~True == False
# ~False == True
a[ ~(a%2==0) ]

# Złożone
a[ ~(a%2==0) & (a>30) | (a==15) ^ (a>40)]


# Dobre praktyki
q1 = (a%2==0)
q2 = (a>30)
q3 = (a==15)
q4 = (a>40)
query = ~q1 & q2 | q3 ^ q4

a[query]
array([15, 31, 33, 35, 37, 39, 41, 42, 43, 44, 45, 46, 47, 48, 49])


parzyste = (a%2==0)
duze = (a>30)
pietnascie = (a==15)
najwieksze = (a>40)

a[ ~parzyste & duze | pietnascie ^ najwieksze ]
# array([15, 31, 33, 35, 37, 39, 41, 42, 43, 44, 45, 46, 47, 48, 49])





index = np.array([
    '1999-12-30',
    '1999-12-31',
    '2000-01-01',
    '2000-01-02'])

columns = np.array(['Morning', 'Noon', 'Evening'])

data = np.array([[ 1.76405235,  0.40015721,  0.97873798],
                 [ 2.2408932 ,  1.86755799, -0.97727788],
                 [ 0.95008842, -0.15135721, -0.10321885],
                 [ 0.4105985 ,  0.14404357,  1.45427351]])

dec30 = (index == '1999-12-30')
dec31 = (index == '1999-12-31')
jan01 = (index == '2000-01-01')
jan02 = (index == '2000-01-02')

morning = (columns == 'Morning')
noon = (columns == 'Noon')
evening = (columns == 'Evening')


data[jan01, noon]
# array([-0.15135721])

data[ jan01|jan02, noon]
# array([-0.15135721,  0.14404357])

data[ dec31|jan01|jan02, noon]
# array([ 1.86755799, -0.15135721,  0.14404357])


# https://python.astrotech.io/numpy/indexing/advancedindexing.html#diagonal-problem

data[ np.ix_(dec31|jan01|jan02, noon|evening)]
# array([[ 1.86755799, -0.97727788],
#        [-0.15135721, -0.10321885],
#        [ 0.14404357,  1.45427351]])

# 7. Universal Functions (ufunc)
# - działają dla skalarów (wartości)
# - działają dla arrayów (n-wymiarowych)

np.sin(1)
# 0.8414709848078965

np.sin(data)
# array([[ 0.9813841 ,  0.38956314,  0.82979374],
#        [ 0.78376151,  0.95628847, -0.82897801],
#        [ 0.81346693, -0.15077996, -0.10303566],
#        [ 0.39915815,  0.14354597,  0.99321889]])

# 8. Vectorized Operations
# - operacje matematyczne, które są aplikowane do każdego elementu (elementwise)
# - normalnie w Python trzeba użyć pętli aby to osiągnąć

data = [1,2,3]
data * 10
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
[x*10 for x in data]
[10, 20, 30]


data = np.array([1,2,3])
data * 10
array([10, 20, 30])

# 9. Reduction operations
# - operacje nieredukujące - na wyjściu mają taką samą liczbę elementów (+, -, *, **, /)
# - operacje redukujące - na wyjściu mają mniejszą liczbę elementów (.sum(), .prod(), .var(), .std(), .mean(), .median())

# 10. NaN

data = np.array([1,2,3,4,np.nan,6,7,8,9])

# Operacje nieredukujące wykonywane są elementwise, dlatego nan jest tylko
# przy elemencie, przy którym był
data * 10
array([10., 20., 30., 40., nan, 60., 70., 80., 90.])

# Operacje redukujące przenoszą NaN (Not-a-Number)

# jeżeli w danych jest choćby jeden NaN, to wynik zawsze będzie nan
data.sum()
nan
data.mean()
nan
data.std()
nan

# wyjątkiem są funkcje np.nan*()
np.nanmean(data)
5.0
np.mean(data)
nan
np.std(data)
nan
np.nanstd(data)
2.7386127875258306
np.sum(data)
nan
np.nansum(data)
40.0

# 11. Broadcasting
# - to operacje między dwoma arraymi

a * a
array([1, 4, 9])

a + a
array([2, 4, 6])

a - a
array([0, 0, 0])

# - najpierw numpy sprawdza czy kształt pozwala na wykonanie operacji

a - b
array([[ 0,  0,  0],
       [-3, -3, -3]])

b - a
array([[0, 0, 0],
       [3, 3, 3]])

a * b
array([[ 1,  4,  9],
       [ 4, 10, 18]])

b * a
array([[ 1,  4,  9],
       [ 4, 10, 18]])

# - nie wszystkie operacje da się wykonać
# - np. @ - mnożenie macierzowe
# mnożenie macirzowe wymaga aby drugi miał tyle kolumn co pierwszy wierszy,
# i tyle wierszy co pierwszy kolumn
# - nie wszystkie shape mogą wykonać daną operację

a @ b
ValueError: matmul: Input operand 1 has a mismatch in its core dimension 0, with gufunc signature (n?,k),(k,m?)->(n?,m?) (size 2 is different from 3)

b @ a
array([14, 32])

# NaN
# Operacje nieredukujące wykonywane są elementwise, więc jak jeden ma np.nan
# To zarazi nim, korespondujący element w drugim (tylko jeden element)

# W operacjach redukujących NaN jest zaraźliwe, chyba że użyjemy np.nan*()
