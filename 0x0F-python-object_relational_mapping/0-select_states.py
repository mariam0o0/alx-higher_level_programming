#!/usr/bin/python3
"""Lists lists all states from the database."""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    c = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = c.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    for row in cur.fetchall():
        print(row)
    dp.close()
