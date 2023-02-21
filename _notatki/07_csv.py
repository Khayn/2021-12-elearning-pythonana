#%% CSV

import csv


# %% Podsumowanie

# Pandas ma to wbudowane i generalnie nie będziemy korzystali samodzielnie z CSV w Python
# chyba, że... CSV będzie nieprawidłowy i Pandas nie da rady
# Używamy context managera "with"
# używamy encoding do funkcji open(), bo standardowo Excel zapisuje jako cp1250
# a Python i wszystkie systemy operacyjne doniemują, utf-8
# nie obsługuje relacji


# reader        # list[tuple]
# writer        # list[tuple]
# DictReader    # list[dict]
# DictWriter    # list[dict]


# csv.reader()

# Dla Excel w Polsce
# delimiter=';'
# decimal=','
# quotechar='"'
# quoting=csv.QUOTE_MINIMAL
# lineseparator='\r\n'

# Dla Excel in English
# delimiter=','
# decimal='.'
# quotechar='"'
# quoting=csv.QUOTE_MINIMAL
# lineseparator='\r\n'

with open(FILE, mode='r', encoding='cp1250') as file:
    reader = csv.reader(...)

    for line in reader:
        print(line)



file = open(...)
content = file.read()
file.close()


with open(...) as file:
    content = file.read()
