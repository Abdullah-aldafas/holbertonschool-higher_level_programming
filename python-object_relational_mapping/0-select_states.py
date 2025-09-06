#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost ",
        port=3306,
        user=user,
        password=password,
        DATABASE="hbtn_0e_0_usa",
    )
    cur = conn.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()
