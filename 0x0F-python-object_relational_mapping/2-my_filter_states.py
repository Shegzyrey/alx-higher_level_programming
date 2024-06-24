#!/usr/bin/python3
"""List all states in ascending order of ID"""


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
    state = sys.argv[4]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=mysql_username,
                         passwd=mysql_password,
                         db=db_name)

    cursor = db.cursor()
    sql_query = "SELECT * FROM states WHERE states.name = '{}'\
            ORDER BY states.id ASC".format(state)
    cursor.execute(sql_query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
