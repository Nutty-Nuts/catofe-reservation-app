from app.logic.createReservationLogic import information, uploadToDatabase


def clicked_discard_reservation():
    print("discared customer reservation")


def clicked_create_reservation():
    uploadToDatabase()
    print("created customer reservation")


def textEdited_firstName(new_text):
    information["firstName"] = new_text
    print(information["firstName"])


def textEdited_lastName(new_text):
    information["lastName"] = new_text
    print(information["lastName"])


def textEdited_birthdate(new_text):
    information["birthdate"] = new_text
    print(information["birthdate"])


def textEdited_contactNumber(new_text):
    information["contactNumber"] = new_text
    print(information["contactNumber"])


def textEdited_preferredCat(new_text):
    information["preferredCat"] = new_text
    print(information["preferredCat"])


def textEdited_employeeInCharge(new_text):
    information["employeeInCharge"] = new_text
    print(information["employeeInCharge"])


def textEdited_date(new_text):
    information["date"] = new_text
    print(information["date"])


def textEdited_time(new_text):
    information["time"] = new_text
    print(information["time"])


def textEdited_duration(new_text):
    information["duration"] = new_text
    print(information["duration"])
