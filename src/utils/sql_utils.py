from database.config import db, cursor
import mysql.connector


def CREATE_TABLE(table_name, table_contents):
    query = "CREATE TABLE IF NOT EXISTS {} ({});"
    query = query.format(table_name, table_contents)

    try:
        cursor.execute(query)
    except mysql.connector.Error as err:
        print("Something went wrong at CREATE_TABLE({}, {}): {}".format(
            table_name, table_contents, err)
        )
        print()


def DROP_TABLE(table_name):
    query = "DROP TABLE IF EXISTS {}"
    query = query.format(table_name)

    try:
        cursor.execute(query)
    except mysql.connector.Error as err:
        print("Something went wrong at DROP_TABLE({}): {}".format(table_name, err))
        print()


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
        print("Something went wrong at INSERT_ENTITY_INSTANCE({}, {}, {}): {}".format(
            table, table_columns, values, err)
        )
        print()


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
        print("Something went wrong at INSERT_ENTITY_INSTANCES({}, {}, {}): {}".format(
            table, table_columns, values, err)
        )
        print()


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
        print("Something went wrong at UPDATE_ENTITY_INSTANCE({}, {}, {}): {}".format(
            table, columns, err)
        )
        print()


def GET_TABLE_DATA(columns, table):
    query = "SELECT {} FROM {}"
    query = query.format(columns, table)

    try:
        cursor.execute(query)
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print("Something went wrong at GET_TABLE_DATA({}, {}): {}".format(
            columns, table, err)
        )
        print("Failed to fetch data, returning []")
        print()
        return []


def GET_TABLE_DATA_CONDITIONAL(columns, table, conditions):
    query = "SELECT {} FROM {} WHERE {}"
    query = query.format(columns, table, conditions)

    try:
        cursor.execute(query)
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print("Something went wrong at GET_TABLE_DATA_CONDITIONAL({}, {}, {}): {}".format(
            columns, table, err)
        )
        print("Failed to fetch data, returning []")
        print()
        return []


def IS_ENTITY_INSTANCE_EXISTING(columns, table, conditions):
    data = GET_TABLE_DATA_CONDITIONAL(columns, table, conditions)

    if len(data) == 0:
        return False
    else:
        return True
