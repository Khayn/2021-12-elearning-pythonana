# 1. SQLite3 jest zainstalowany prawie wszędzie
# - SQLite3 to plikowa baza danych
# - nie wymaga instalacji serwera
# - nie bardzo obsługuje równoległe połączenia

# 2. SQLite3 jest bazą danych, która jest najczęściej wykorzystywana

# 3. W Python jest DB API, które jest takie same dla wszystkich RDBMS
# - .connect()
# - .execute()
# - .executemany()
# - .fetchone()
# - .fetchall()
# - .close()

# 4. zapytania SQL różnią się między bazami danych
# - SQLite3 jest kompatybilny z PostgreSQL
# - PostgreSQL jest kompatybilny z Oracle
# - W większości zapytania są podobne



import sqlite3



SQL_CREATE = """
    CREATE TABLE IF NOT EXISTS astronaut (
        firstname TEXT, 
        lastname TEXT);"""

SQL_INSERT = """
    INSERT INTO astronaut
    VALUES (:firstname, :lastname);"""

SQL_SELECT = """
    SELECT * 
    FROM astronaut;"""


data = [
    {'firstname': 'Mark', 'lastname': 'Watney'},
    {'firstname': 'Melissa', 'lastname': 'Lewis'},
    {'firstname': 'Rick', 'lastname': 'Martinez'},
]

with sqlite3.connect('/tmp/myfile.db') as db:
    db.execute(SQL_CREATE)
    db.executemany(SQL_INSERT, data)

    for row in db.execute(SQL_SELECT):
        print(row)



# PostgreSQL - psycodb2
# Oracle - ora
# MySQL - pymysql
# MSSQL - pyodbc, pymssql



SQL_SELECT = """
    SELECT datetime, category, event
    FROM apollo11
    WHERE
        datetime BETWEEN '1969-07-20' AND '1969-07-22'
        AND category IN ('INFO', 'CRITICAL', 'WARNING', 'ERROR')
    LIMIT 0, 30
    ORDER BY datetime ASC
"""

df = pd.read_sql(SQL_SELECT, db)
