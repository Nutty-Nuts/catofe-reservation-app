import utils.sql_utils as SQL


class ReservationData():
    def __init__(self):
        print("reservation_data.py: Initializing reservation data class")

        self.database_data = []
        self.processed_data = []

    def refresh(self):
        self.fetch()
        self.process()

    def fetch(self):
        fetch_columns = "reservation_id, customer_id, cat_id, reservation_date, reservation_time_start, reservation_time_end"
        fetch_table = "reservation"
        fetched_data = SQL.GET_TABLE_DATA(fetch_columns, fetch_table)

        if len(fetched_data) == 0:
            return
        else:
            self.database_data = []
            self.database_data = fetched_data

    def process(self):
        processed_data = []
        for row_number, row_data in enumerate(self.database_data):
            customer_conditions = "customer_id = {}"
            customer_conditions = customer_conditions.format(row_data[1])
            customer = SQL.GET_TABLE_DATA_CONDITIONAL(
                "customer_first_name, customer_last_name, customer_contact_no",
                "customer",
                customer_conditions
            )

            customer_name = str(customer[0][0]) + " " + str(customer[0][1])
            processed_datum = (row_data[0], customer_name, customer[0][2], row_data[2],
                               row_data[3], row_data[4], row_data[5])

            processed_data.append(processed_datum)

        if len(processed_data) == 0:
            return 0
        else:
            self.processed_data = []
            self.processed_data = processed_data


reservation_data = ReservationData()
