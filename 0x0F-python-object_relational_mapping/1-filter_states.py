#!/usr/bin/python3
"""Lists all states starting with N"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    [print(state) for state in cur.fetchall() if state[1][0] == "N"]
    cur.close()
    conn.close()
