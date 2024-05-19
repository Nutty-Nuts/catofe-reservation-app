import utils.sql_utils as SQL


def init_tables():
    SQL.CREATE_TABLE(
        "customer",
        """
        customer_id int NOT NULL AUTO_INCREMENT,
        customer_first_name varchar(255),
        customer_last_name varchar(255),
        customer_contact_no varchar(255),

        PRIMARY KEY (customer_id)
        """
    )

    SQL.CREATE_TABLE(
        "employee",
        """
        employee_id int NOT NULL AUTO_INCREMENT,
        employee_first_name varchar(255),
        employee_last_name varchar(255),
        employee_contact_no varchar(255),

        PRIMARY KEY (employee_id)
        """
    )

    SQL.CREATE_TABLE(
        "cat",
        """
        cat_id int NOT NULL AUTO_INCREMENT,
        cat_name varchar(255),
        cat_breed varchar(255),
        cat_birthdate date default NULL,

        PRIMARY KEY (cat_id)
        """
    )

    SQL.CREATE_TABLE(
        "reservation",
        """
        reservation_id int NOT NULL AUTO_INCREMENT,
        customer_id int default 0,
        employee_id int default 0,
        cat_id int default 0,
        reservation_date varchar(255),
        reservation_time_start varchar(255),
        reservation_time_end varchar(255),

        PRIMARY KEY (reservation_id),
        FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
        FOREIGN KEY (employee_id) REFERENCES employee(employee_id),
        FOREIGN KEY (cat_id) REFERENCES cat(cat_id)
        """
    )


def init_cats():
    SQL.INSERT_ENTITY_INSTANCES(
        "cat",
        "cat_name, cat_breed, cat_birthdate",
        [
            ('Maxell', 'Tuxedo Cat', '2020-01-01'),
            ('Arthur', 'British Shorthair', '2021-06-21'),
            ('Anis', 'Orange Cat', '2018-07-11'),
            ('Andrea', 'American Curl', '207-12-25'),
        ]
    )


def init_employee():
    SQL.INSERT_ENTITY_INSTANCES(
        "employee",
        "employee_first_name, employee_last_name, employee_contact_no",
        [
            ("John", "Smith", "0912876123"),
            ("Wilhelm", "Helmsman", "0988172980")
        ]
    )


def init_customer():
    SQL.INSERT_ENTITY_INSTANCES(
        "customer",
        "customer_first_name, customer_last_name, customer_contact_no",
        [
            ("Gerard Angelo", "Vega", "09350354447"),
            ("Dave Christian", "Baran", "09979920287"),
            ("Lorenz Roal", "Abonitalla", "09067379136"),
        ]
    )


def init_reservation():
    SQL.INSERT_ENTITY_INSTANCES(
        "reservation",
        "customer_id, employee_id, cat_id, reservation_date, reservation_time_start, reservation_time_end",
        [
            (1, 1, 2, "2024-05-11", "07:30:00", "11:00:00",),
            (2, 1, 4, "2024-05-11", "09:30:00", "13:00:00",),
            (3, 1, 1, "2024-05-11", "11:30:00", "14:00:00",),
        ]
    )


def test_customer_select():
    data = SQL.GET_TABLE_DATA_CONDITIONAL(
        "customer_id",
        "customer",
        """
        customer_first_name = 'Gerard Angelo' AND 
        customer_last_name = 'Vega' 
        """
    )
    print(data[0][0])
