import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select(conn, sql):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param sql:
    :return: sql result
    """
    cur = conn.cursor()
    cur.execute(sql)

    rows = cur.fetchall()

    for row in rows:
        print(row)


def insert(conn, sql):
    """
    Insert into table
    :param conn:
    :param sql:
    :return: project id
    """
    # sql = ''' INSERT INTO projects(name,begin_date,end_date)
    #           VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(conn, sql)
    return cur.lastrowid


def update(conn, sql):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param sql:
    :return: project id
    """
    # sql = ''' UPDATE tasks
    #           SET priority = ? ,
    #               begin_date = ? ,
    #               end_date = ?
    #           WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(conn, sql)
    conn.commit()


def main():
    database = r"../db.sqlite3"

    # create a database connection
    conn = create_connection(database)
    with conn:

        print(insert(conn, ''))
        print(select(conn, 'SELECT * FROM usuarios_usuariosmodel'))


if __name__ == '__main__':
    main()