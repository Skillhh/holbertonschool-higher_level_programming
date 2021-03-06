#!/usr/bin/python3
""" Lists all elements from the database """
import MySQLdb
from sys import argv


def connect():
    """ Connection Data Base """
    if len(argv) == 4:
        conn = MySQLdb.connect(host='localhost', user=argv[1],
                               passwd=argv[2], db=argv[3], port=3306)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM states ORDER BY states.id ASC;')
        # Print tuple
        for row in cursor.fetchall():
            print(row)
        # Close connection
        conn.close()


if __name__ == '__main__':
    connect()
