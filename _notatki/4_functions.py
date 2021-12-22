def say_hello():
    print('hello')
    print('hello')
    print('hello')
    print('hello')


#

def add(a, b):  # parametry
    return a + b


add(1, 2)  # argumenty


# parametry - to z czym definiujesz funkcję
# - wymagane
# - opcjonalne - mają wartość domyślną
# opcjonalne parametry są zawsze maksymalnie po prawej stronie
# po jakimkolwiek parametrze z wartością domyślną,
# wszystkie kolejne muszą mieć wartość domyślną

def add(a, b):  # oba parametry są wymagane
    return a + b


def add(a=1, b=2):  # oba parametry są opcjonalne
    return a + b


def add(a, b=2):  # a jest wymagane, b jest opcjonalne
    return a + b


def add(a=1, b):  # nie działa
    return a + b


def add(a, b=1, c):  # nie działa
    return a + b


def add(a, b=1, c=2):  # a jest wymagany, b i c opcjonalny
    return a + b


# argumenty - to z czym wywołujesz funkcję
# - pozycyjne - parametrom przypisywane są wartości po kolei
# - nazwane (keyword) - przypisywane po nazwach, a nie kolejności
# - nazwane muszą być maksymalnie po prawej stronie
# - po jakimkolwiek nazwanym, wszystkie kolejne muszą być keyword


def add(a, b):  # oba parametry są wymagane
    return a + b


add(1, 2)
add(a=1, b=2)
add(b=2, a=1)
add(1, b=2)
add(a=1, 2)  # nie działa


def add(a, b=1, c=2):  # a jest wymagany, b i c opcjonalny
    return a + b


add(1, b=2, 3)  # nie działa


def login(username, password):
    ...


login('root', 'admin')
login('admin', 'root')

login(username='root',
      password='admin')

login(
    password='admin',
    username='root', )


#


def read_csv(filepath_or_buffer, sep=NoDefault.no_default, delimiter=None,
             header='infer', names=NoDefault.no_default, index_col=None,
             usecols=None, squeeze=False, prefix=NoDefault.no_default,
             mangle_dupe_cols=True, dtype=None, engine=None, converters=None,
             true_values=None, false_values=None, skipinitialspace=False,
             skiprows=None, skipfooter=0, nrows=None, na_values=None,
             keep_default_na=True, na_filter=True, verbose=False,
             skip_blank_lines=True, parse_dates=False,
             infer_datetime_format=False,
             keep_date_col=False, date_parser=None, dayfirst=False,
             cache_dates=True, iterator=False, chunksize=None,
             compression='infer',
             thousands=None, decimal='.', lineterminator=None, quotechar='"',
             quoting=0, doublequote=True, escapechar=None, comment=None,
             encoding=None, encoding_errors='strict', dialect=None,
             error_bad_lines=None, warn_bad_lines=None, on_bad_lines=None,
             delim_whitespace=False, low_memory=True, memory_map=False,
             float_precision=None, storage_options=None): ...


read_csv('myfile.csv',
         usecols=(1, 2, 3, 4),
         delimiter=',',
         encoding='utf-8',
         skiprows=2)



# datetime
# json
# csv
# database
# regex
