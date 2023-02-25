"""
This script scrapes data from yahoo finance and saves it to an SQLite database
"""
import sqlite3

import web_scraping
import database_functions as db_func
import constants


# TODO: finish documentation
# TODO: check scheduler host and setup

if __name__ == '__main__':

    url = web_scraping.generate_nasdaq_url()
    source_code = web_scraping.scrape(url)
    table = web_scraping.extract_table_data(source_code)

    try:
        connection = db_func.database_connect(constants.DATABASE_NAME)
        for row in table[1:-1]:
            row[0] = db_func.format_date_sqlite(row[0])
            existing_row = db_func.database_load_row(connection,
                                                     constants.TABLE_NAME,
                                                     row[0])
            if not existing_row:
                db_func.database_insert_row(connection,
                                            constants.TABLE_NAME,
                                            row)
        connection.close()
    except sqlite3.OperationalError:
        print ('Error communicating with database')




