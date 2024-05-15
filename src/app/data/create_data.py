import utils.sql_utils as SQL


class CreateData():
    def __init__(self):
        print("initializing create data")
        self.information = {
            "first_name": "",
            "last_name": "",
            "contact_number": "",
            "preferred_cat": "",
            "employee_in_charge": "",
            "date": "",
            "time_start": "",
            "time_end": ""
        }

    def clear(self):
        self.information = {
            "first_name": "",
            "last_name": "",
            "contact_number": "",
            "preferred_cat": "",
            "employee_in_charge": "",
            "date": "",
            "time_start": "",
            "time_end": ""
        }

    def upload(self):
        if self.validate():
            print("incomplete data")
            return

        conditions = "customer_first_name = '{}' AND customer_last_name = '{}' AND customer_contact_no = '{}'"
        conditions = conditions.format(
            self.information["first_name"], self.information["last_name"], self.information["contact_number"]
        )

        if SQL.IS_ENTITY_INSTANCE_EXISTING("customer_id", "customer", conditions):
            print("Customer already exists")
        else:
            print("Creating customer")

            SQL.INSERT_ENTITY_INSTANCE(
                "customer",
                "customer_first_name, customer_last_name, customer_contact_no",
                (self.information["first_name"], self.information["last_name"],
                 self.information["contact_number"])
            )

        data = SQL.GET_TABLE_DATA_CONDITIONAL(
            "customer_id",
            "customer",
            conditions
        )

        customer_id = data[0][0]

        SQL.INSERT_ENTITY_INSTANCE(
            "reservation",
            "customer_id, employee_id, cat_id,  reservation_date, reservation_time_start, reservation_time_end",
            (customer_id, self.information["employee_in_charge"], self.information["preferred_cat"],
             self.information["date"], self.information["time_start"], self.information["time_end"])
        )

        self.clear()

    def validate(self):
        validate_first_name = self.information["first_name"] == ""
        validate_last_name = self.information["last_name"] == ""
        validate_contact_number = self.information["contact_number"] == ""
        validate_preferred_cat = self.information["preferred_cat"] == ""
        validate_employee_in_charge = self.information["employee_in_charge"] == ""
        validate_date = self.information["date"] == ""
        validate_time_start = self.information["time_start"] == ""
        validate_time_end = self.information["time_end"] == ""

        validate = validate_first_name or validate_last_name or validate_contact_number or validate_preferred_cat or validate_employee_in_charge or validate_date or validate_time_start or validate_time_end

        return validate


create_data = CreateData()
