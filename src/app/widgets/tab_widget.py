from PySide6.QtWidgets import QTabWidget, QVBoxLayout, QWidget
from shiboken6 import createdByPython
from app.widgets.create_page import CreatePage
from app.widgets.reserve_page import ReservationPage

from app.data.reservation_data import reservation_data
from app.data.create_data import create_data


class Tab(QWidget):
    def __init__(self):
        super().__init__()

        self.create_page = CreatePage()
        self.reservation_page = ReservationPage()
        widget_tab = QTabWidget()

        widget_tab.addTab(self.create_page, "Create")
        widget_tab.addTab(self.reservation_page, "Reservations")

        layout_main = QVBoxLayout()
        layout_main.addWidget(widget_tab)

        self.setLayout(layout_main)

        self.create_page.widget_discard_button.clicked.connect(
            self.discard_create_reservation
        )

        self.create_page.widget_create_button.clicked.connect(
            self.clicked_create_reservation
        )

        self.refresh()

    def refresh(self):
        reservation_data.refresh()
        self.reservation_page.refresh(reservation_data.processed_data)

    def clicked_create_reservation(self):
        if self.validate() == False:
            return

        create_data.upload()
        self.refresh()
        self.clear_line_edits()

    def discard_create_reservation(self):
        self.clear_line_edits()

    def clear_line_edits(self):
        create = self.create_page
        line_edits = [create.widget_first_name, create.widget_last_name, create.widget_contact_no, create.widget_preferred_cat,
                      create.widget_employee_in_charge, create.widget_date, create.widget_time_start, create.widget_time_end]

        for line_edit in line_edits:
            line_edit.clear()

    def validate(self):
        create = self.create_page
        line_edits = [create.widget_first_name, create.widget_last_name, create.widget_contact_no, create.widget_preferred_cat,
                      create.widget_employee_in_charge, create.widget_date, create.widget_time_start, create.widget_time_end]

        for line_edit in line_edits:
            if line_edit.text() == "":
                return False

        return True
