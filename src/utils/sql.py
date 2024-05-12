from data.config import db, cursor
import mysql.connector


def CREATE_TABLE(table_name, table_contents):
    query = "CREATE TABLE IF NOT EXISTS {} ({});"
    query = query.format(table_name, table_contents)

    try:
        cursor.execute(query)
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))


def DROP_TABLE(table_name):
    query = "DROP TABLE IF EXISTS {}"
    query = query.format(table_name)

    try:
        cursor.execute(query)
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))


def INSERT_ENTITY_INSTANCE(table, table_columns, values):
    number_of_columns = len(table_columns.split(", "))
    format = ""

    for i in range(number_of_columns):
        if i >= number_of_columns - 1:
            format = format + "%s"
        else:
            format = format + "%s, "

    query = "INSERT INTO {} ({}) VALUES ({})"
    query = query.format(table, table_columns, format)

    try:
        cursor.execute(query, values)
        db.commit()
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))


def INSERT_ENTITY_INSTANCES(table, table_columns, values):
    number_of_columns = len(table_columns.split(", "))
    format = ""

    for i in range(number_of_columns):
        if i >= number_of_columns - 1:
            format = format + "%s"
        else:
            format = format + "%s, "

    query = "INSERT INTO {} ({}) VALUES ({})"
    query = query.format(table, table_columns, format)

    try:
        cursor.executemany(query, values)
        db.commit()
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))


def UPDATE_ENTITY_INSTANCE(table, columns, identifier):
    query = """
    UPDATE {}
    SET {}
    WHERE {}
    """
    query = query.format(table, columns, identifier)

    try:
        cursor.execute(query)
        db.commit()
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))


def GET_TABLE_DATA(columns, table):
    query = "SELECT {} FROM {}"
    query = query.format(columns, table)

    try:
        cursor.execute(query)
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        return None


def GET_TABLE_DATA_CONDITIONAL(columns, table, conditions):
    query = "SELECT {} FROM {} WHERE {}"
    query = query.format(columns, table, conditions)

    try:
        cursor.execute(query)
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        return cursor.fetchall()
        # return None
