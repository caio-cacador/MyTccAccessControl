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


def select_task_by_priority(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuarios_usuariosmodel")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def create_task(conn):
    """
    Create a new task
    :param conn:
    :return:
    """

    sql = ''' SELECT * FROM usuarios_usuariosmodel '''
    cur = conn.cursor()
    cur.execute(sql)
    return cur.lastrowid


def main():
    database = r"../db.sqlite3"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        # project = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30');
        # project_id = create_project(conn, project)

        # tasks
        # task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
        # task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')

        # create tasks
        print(select_all_tasks(conn))
        # create_task(conn, task_2)


if __name__ == '__main__':
    main()