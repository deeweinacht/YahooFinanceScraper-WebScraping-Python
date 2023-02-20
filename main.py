"""

"""

import web_scraping
import database_access
import constants

# TODO: format date string so DB recognizes as date
# TODO: include logic to prevent duplicate entries attempted
# TODO: finish documentation
# TODO: check scheduler host and setup

if __name__ == '__main__':
    url = web_scraping.generate_nasdaq_url()
    source_code = web_scraping.scrape(url)
    table = web_scraping.extract_table_data(source_code)

    connection = database_access.database_connect(constants.DATABASE_NAME)
    for row in table[1:-1]:
        database_access.database_insert(connection, constants.TABLE_NAME, row)




