from app.logic.createReservationLogic import reservationInformation


def clicked_discard_reservation():
    print("discared customer reservation")


def clicked_create_reservation():
    print("created customer reservation")


def textEdited_firstName(new_text):
    reservationInformation["firstName"] = new_text
    print(reservationInformation["firstName"])


def textEdited_lastName(new_text):
    reservationInformation["lastName"] = new_text
    print(reservationInformation["lastName"])


def textEdited_birthdate(new_text):
    reservationInformation["birthdate"] = new_text
    print(reservationInformation["birthdate"])


def textEdited_contactNumber(new_text):
    reservationInformation["contactNumber"] = new_text
    print(reservationInformation["contactNumber"])


def textEdited_preferredCat(new_text):
    reservationInformation["preferredCat"] = new_text
    print(reservationInformation["preferredCat"])


def textEdited_employeeInCharge(new_text):
    reservationInformation["employeeInCharge"] = new_text
    print(reservationInformation["employeeInCharge"])


def textEdited_date(new_text):
    reservationInformation["date"] = new_text
    print(reservationInformation["date"])


def textEdited_time(new_text):
    reservationInformation["time"] = new_text
    print(reservationInformation["time"])


def textEdited_duration(new_text):
    reservationInformation["duration"] = new_text
    print(reservationInformation["duration"])
