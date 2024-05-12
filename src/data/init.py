import utils.sql as sql


def init_tables():
    sql.CREATE_TABLE(
        "customer",
        """
        customer_id int NOT NULL AUTO_INCREMENT,
        customer_first_name varchar(255),
        customer_last_name varchar(255),
        customer_contact_no varchar(255),

        PRIMARY KEY (customer_id)
        """
    )

    sql.CREATE_TABLE(
        "employee",
        """
        employee_id int NOT NULL AUTO_INCREMENT,
        employee_first_name varchar(255),
        employee_last_name varchar(255),
        employee_contact_no varchar(255),
        employee_birthdate date default NULL,

        PRIMARY KEY (employee_id)
        """
    )

    sql.CREATE_TABLE(
        "cat",
        """
        cat_id int NOT NULL AUTO_INCREMENT,
        cat_name varchar(255),
        cat_birthdate date default NULL,

        PRIMARY KEY (cat_id)
        """
    )

    sql.CREATE_TABLE(
        "reservation",
        """
        reservation_id int NOT NULL AUTO_INCREMENT,
        customer_id int default 0,
        employee_id int default 0,
        cat_id int default 0,
        reservation_date date default NULL,
        reservation_time_start time default NULL,
        reservation_time_end time default NULL,
        reservation_status varchar(255),

        PRIMARY KEY (reservation_id),
        FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
        FOREIGN KEY (employee_id) REFERENCES employee(employee_id),
        FOREIGN KEY (cat_id) REFERENCES cat(cat_id)
        """
    )


def init_cats():
    sql.INSERT_ENTITY_INSTANCES(
        "cat",
        "cat_name, cat_birthdate",
        [
            ('Maxell', '2020-01-01'),
            ('Arthur', '2021-06-21'),
            ('Anis', '2018-07-11'),
            ('Andrea', '207-12-25'),
        ]
    )


def init_employee():
    sql.INSERT_ENTITY_INSTANCES(
        "employee",
        "employee_first_name, employee_last_name, employee_contact_no, employee_birthdate",
        [
            ("John", "Smith", "0912876123", "2000-01-01"),
            ("Wilhelm", "Helmsman", "0988172980", "2002-03-11")
        ]
    )


def init_customer():
    sql.INSERT_ENTITY_INSTANCES(
        "customer",
        "customer_first_name, customer_last_name, customer_contact_no",
        [
            ("Gerard Angelo", "Vega", "09350354447")
        ]
    )


def init_reservation():
    sql.INSERT_ENTITY_INSTANCES(
        "reservation",
        "customer_id, employee_id, cat_id, reservation_date, reservation_time_start, reservation_time_end, reservation_status",
        [
            (1, 1, 2, "2024-05-11", "07:30:00", "11:00:00", "Queued")
        ]
    )


def test_customer_select():
    data = sql.GET_TABLE_DATA_CONDITIONAL(
        "customer_id",
        "customer",
        """
        customer_first_name = 'Gerard Angelo' AND 
        customer_last_name = 'Vega' 
        """
    )
    print(data[0][0])
