#!/usr/bin/python3
"""connects to a MySQL database and retrieves the names
of cities in a specific state."""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
    )
    cur = db.cursor()
    cmdsq = """ SELECT cities.name
    FROM cities
    INNER JOIN states ON states.id=cities.state_id
    WHERE states.name=%s"""
    cur.execute(
        cmdsq,
        (sys.argv[4],),
    )
    rows = cur.fetchall()
    tmp = list(row[0] for row in rows)
    print(", ".join(tmp))
    cur.close()
    db.close()
