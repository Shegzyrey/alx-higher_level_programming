#!/usr/bin/python3
"""List all states in ascending order of ID"""


if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    mysql_username = argv[1]
    mysql_password = argv[2]
    db_name = argv[3]
    claus = argv[4]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=mysql_username,
                         passwd=mysql_password,
                         db=db_name)

    cursor = db.cursor()
    sql_query = "SELECT * FROM states WHERE states.name LIKE\
            BINARY '{}' ORDER BY states.id ASC".format(claus)
    cursor.execute(sql_query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
