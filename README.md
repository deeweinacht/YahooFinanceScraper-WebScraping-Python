# YahooFinanceScraper-WebScraping-Python

**This script scrapes data from yahoo finance and saves it to an SQLite 
database**

    Copyright (C) 2023  Dee Weinacht

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

**Description:**  
This script scrapes data from the yahoo finance page summarizing daily data for 
the nasdaq composite for the previous 90-day period. The data is parsed and
saved into an SQLite database for future use or analysis. Each time the script 
runs it will add any additional data read since the last time the script was 
run.

**User's Guide:**  
To load the most recent 90 days of financial data for the nasdaq composite
index run the main.py file. The data will be stored in the SQLite database
'FinancialData.db'. If the file does not already exist, it will be created.

**Dependencies:**
- html_table_parser used under the GNU AGPL v3.0 License
- requests used under the Apache 2.0 License