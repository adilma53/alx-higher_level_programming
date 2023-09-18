#!/usr/bin/python3
"""filter state table by the capital letter N"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", user=argv[1], password=argv[2], database=argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    row = cur.fetchall()
    for state in row:
        print(state)
    cur.close()
    db.close()
