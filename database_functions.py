import sqlite3
from datetime import datetime


def database_connect(database_name: str):
    """
    Forms a connection to an SQLite database with the given name.
    :param database_name: name of the SQLite database
    :return: <Connection> connection object for the database
    """
    connection = sqlite3.Connection(database_name)
    return connection


def database_load_table(connection: sqlite3.Connection, table_name: str):
    """
    Loads an entire table from a database
    :param connection: SQLite Connection object formed with the database
    :param table_name: table to load from the database
    :return: <list> a list of rows forming the table
    """
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM {table_name}')
    rows = cursor.fetchall()
    cursor.close()
    table = [list(row) for row in rows]
    return table


def database_load_row(connection: sqlite3.Connection,
                      table_name: str,
                      row_date: str):
    """
    Loads a specific row from a table from a database
    :param connection: SQLite Connection object formed with the database
    :param table_name: table to load from in the database
    :param row_date: identifying date for the row
    :return: the row from the table
    """
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table_name} WHERE Date='{row_date}'")
    row = cursor.fetchone()
    cursor.close()
    return row


def database_insert_row(connection: sqlite3.Connection,
                        table_name: str,
                        row: list):
    """
    Inserts a row into a table in the database
    :param connection: SQLite Connection object formed with the database
    :param table_name: table to insert into in the database
    :param row: row to insert into the database
    :return:
    """
    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO {table_name} VALUES(?,?,?,?,?,?,?)', row)
    connection.commit()
    cursor.close()


def format_date_sqlite(date_orig: str):
    """
    Format a date for SQLite in the format YYYY-MM-DD
    :param date_orig: date in the format (Abr-Month dd, yyyy)
    :return: <str> date in the formatted string
    """
    date_formatted = datetime.strptime(date_orig, '%b %d, %Y')
    return date_formatted.strftime('%Y-%m-%d')
