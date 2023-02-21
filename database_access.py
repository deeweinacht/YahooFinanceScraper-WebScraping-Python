import sqlite3


def database_connect(database_name: str):
    connection = sqlite3.Connection(database_name)
    return connection


def database_close(connection: sqlite3.Connection):
    connection.close()


def database_load_table(connection: sqlite3.Connection, table_name: str):
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM {table_name}')
    rows = cursor.fetchall()
    cursor.close()
    table = [list(row) for row in rows]
    return table


def database_load_row(connection: sqlite3.Connection,
                      table_name: str,
                      row_date: str):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table_name} WHERE Date='{row_date}'")
    row = cursor.fetchone()
    cursor.close()
    return row


def database_insert_row(connection: sqlite3.Connection,
                        table_name: str,
                        row: list):
    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO {table_name} VALUES(?,?,?,?,?,?,?)', row)
    connection.commit()
    cursor.close()
