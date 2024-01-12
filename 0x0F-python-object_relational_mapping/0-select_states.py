#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa."""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], port=3306, db=argv[3])

    # Create a MySQL cursor
    cursor = db.cursor()

    # Execute the MySQL query
    cursor.execute("SELECT * FROM states ORDER BY id")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
