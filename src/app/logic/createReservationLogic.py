import utils.sql as sql

information = {
    "firstName": "",
    "lastName": "",
    "birthdate": "",
    "contactNumber": "",
    "preferredCat": "",
    "employeeInCharge": "",
    "date": "",
    "time": "",
    "duration": ""
}


def uploadToDatabase():
    sql.INSERT_ENTITY_INSTANCE(
        "customer",
        "customer_first_name, customer_last_name, customer_contact_no",
        (information["firstName"], information["lastName"],
         information["contactNumber"])
    )

    conditions = "customer_first_name = '{}' AND customer_last_name = '{}' AND customer_contact_no = '{}'"
    conditions = conditions.format(
        information["firstName"], information["lastName"], information["contactNumber"]
    )

    data = sql.GET_TABLE_DATA_CONDITIONAL(
        "customer_id",
        "customer",
        conditions
    )

    if data == None:
        return

    customer_id = data[0][0]

    sql.INSERT_ENTITY_INSTANCE(
        "reservation",
        "customer_id, employee_id, cat_id,  reservation_date, reservation_time_start, reservation_time_end, reservation_status",
        (customer_id, information["employeeInCharge"], information["preferredCat"],
         information["date"], information["time"], information["duration"], "Queued")
    )
