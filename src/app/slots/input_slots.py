from app.data.create_data import create_data


class InputSlots():
    def __init__(self):
        print("create_page_slots.py: Initializing InputSlots")

    def text_edited_first_name(self, text):
        create_data.information["first_name"] = text

    def text_edited_last_name(self, text):
        create_data.information["last_name"] = text

    def text_edited_contact_number(self, text):
        create_data.information["contact_number"] = text

    def text_edited_preferred_cat(self, text):
        create_data.information["preferred_cat"] = text

    def text_edited_employee_in_charge(self, text):
        create_data.information["employee_in_charge"] = text

    def text_edited_date(self, text):
        create_data.information["date"] = text

    def text_edited_time_start(self, text):
        create_data.information["time_start"] = text

    def text_edited_time_end(self, text):
        create_data.information["time_end"] = text


slots = InputSlots()
