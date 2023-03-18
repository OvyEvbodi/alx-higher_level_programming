#!/usr/bin/python3

"""This module lists all states from a database,
where name starts with 'N'
It takes the following arguments:
    mysql username
    mysql password
    database name
"""

import MySQLdb
from sys import argv


def db_connect(username, password, database, host="localhost", port=3306):
    """Establishes a connection to a database

    Args:
        username: the username of the MySQL to connect to
        password: the password of the server
        database: the database to use
        host: the host
        port: the port

    Returns:
        a connection object
    """
    connection = None
    connection = MySQLdb.connect(user=username, passwd=password, db=database)
    return connection


def db_cursor(connection):
    """Gets a cursor from a connection object

    Args:
        connection: the connection object

    Return:
        the cursor
    """
    cursor = None
    cursor = connection.cursor()
    return cursor


def db_execute(cursor, command, param):
    """Executes a MySQL query

    Args:
        cursor: the cursor
        command: the query to execute

    Returns:
        the number of records returned by the query

    """
    rows = None
    rows = cursor.execute(command, param)
    return rows


def db_print_data(cursor):
    """Prints the query (if printable)

    Args:
        cursor: the cursor

    Returns:
        The data returned by the query
    """
    data = None
    data = cursor.fetchall()
    for cursor in data:
        print(f"{cursor}")
    return data


def db_clean_up(cursor, connection):
    """Cleans up after executing a mySQL query

    Args:
        cursor: the cursor
        connection: the MySQLdb connection
    """
    cursor.close()
    connection.close()


if __name__ == '__main__':
    if len(argv) < 5:
        print('Usage: argv[0] <username> <password> <database> <state name>')
        exit()
    state = argv[4]
    command = 'SELECT * FROM states WHERE name = %s \
    ORDER BY id'
    connection = db_connect(argv[1], argv[2], argv[3])
    cursor = db_cursor(connection)
    rows = db_execute(cursor, command, (state,))
    data = db_print_data(cursor)
    db_clean_up(cursor, connection)
