import utils.sql_utils as SQL


def purge():
    SQL.DROP_TABLE(
        "reservation"
    )

    SQL.DROP_TABLE(
        "customer"
    )

    SQL.DROP_TABLE(
        "employee"
    )

    SQL.DROP_TABLE(
        "cat"
    )
