import utils.sql as sql


def purge():
    sql.DROP_TABLE(
        "reservation"
    )

    sql.DROP_TABLE(
        "customer"
    )

    sql.DROP_TABLE(
        "employee"
    )

    sql.DROP_TABLE(
        "cat"
    )
