#!/usr/bin/python3
"""List all states in ascending order of ID starting with N"""


if __name__ == "__main__":

    import MySQLdb
    import sys

    if len(sys.argv) != 4:
        res = "Usage: ./0-states.py <mysql_username>"
        res += "<mysql_password> <db_name>"
        print(res)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=mysql_username,
                         passwd=mysql_password,
                         db=db_name)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name like\
            'N%' ORDER BY states.id ASC;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
