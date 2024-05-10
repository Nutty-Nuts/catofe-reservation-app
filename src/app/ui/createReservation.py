from PySide6.QtWidgets import QGroupBox, QHBoxLayout, QHeaderView, QLineEdit, QPushButton, QSpacerItem, QTableView, QTableWidget, QVBoxLayout, QWidget
from utils.qt import Fonts, Layout, LineEdit, Label
import app.slots.createReservationSlots as slots


class CreateReservation(QWidget):
    def __init__(self):
        super().__init__()

        # ## SECTION: UI
        # ## THIS SECTION OF THE CLASS WILL HANDLE THE CREATE OF THE
        # ## USER INTERFACE

        lt_pageHeader = Label.createCenteredLabel("CREATE RESERVATION")
        Layout.extractWidget(lt_pageHeader, 1).setFont(Fonts.heroText)

        # customer information widgets and widget-layouts
        wt_firstName = LineEdit.createLineEdit("customer first name")
        lt_firstName = LineEdit.createVLabelLineEdit(
            "First Name", wt_firstName
        )
        wt_lastName = LineEdit.createLineEdit("customer last name")
        lt_lastName = LineEdit.createVLabelLineEdit(
            "Last Name", wt_lastName
        )
        wt_age = LineEdit.createLineEdit("customer birthdate")
        lt_age = LineEdit.createVLabelLineEdit(
            "Birthdate", wt_age
        )
        wt_contactNumber = LineEdit.createLineEdit("customer contact number")
        lt_contact = LineEdit.createVLabelLineEdit(
            "Contact No.", wt_contactNumber
        )

        lt_ageContact = QHBoxLayout()
        Layout.addMultipleLayoutsToLayout(
            [lt_age, lt_contact], lt_ageContact
        )

        # reservation information widgets and widget-layouts
        wt_preferredCat = LineEdit.createLineEdit("reservation preferred cat")
        lt_preferredCat = LineEdit.createVLabelLineEdit(
            "Preferred Cat", wt_preferredCat
        )
        wt_employeeInCharge = LineEdit.createLineEdit(
            "employee in charge of reservation")
        lt_employeeInCharge = LineEdit.createVLabelLineEdit(
            "Employee In Charge", wt_employeeInCharge
        )
        wt_date = LineEdit.createLineEdit("YYYY-MM-DD")
        lt_date = LineEdit.createVLabelLineEdit(
            "Date", wt_date
        )
        wt_time = LineEdit.createLineEdit("hh:mm")
        lt_time = LineEdit.createVLabelLineEdit(
            "Time", wt_time
        )
        wt_duration = LineEdit.createLineEdit("hh:mm")
        lt_duration = LineEdit.createVLabelLineEdit(
            "Duration", wt_duration
        )

        lt_dateTimeDuration = QHBoxLayout()
        Layout.addMultipleLayoutsToLayout(
            [lt_date, lt_time, lt_duration],
            lt_dateTimeDuration
        )

        # actions for creating reservations
        wt_discardButton = QPushButton("Discard")
        wt_createButton = QPushButton("Create")

        discard_create_layout = QHBoxLayout()
        Layout.addMultipleWidgetsToLayout(
            [wt_discardButton, wt_createButton], discard_create_layout
        )

        # customer information group box and group box layout
        wt_custInfoGroupBox = QGroupBox("Customer Information")
        lt_custInfoGoupBoxLayout = QVBoxLayout()

        # reservation information group box and group box layout
        wt_resInfoGroupBox = QGroupBox("Reservation Information")
        lt_resInfoGoupBoxLayout = QVBoxLayout()

        widgetLayout = QVBoxLayout()
        Layout.addLayoutToLayout(lt_pageHeader, widgetLayout)

        Layout.addMultipleLayoutsToLayout(
            [lt_firstName, lt_lastName, lt_ageContact],
            lt_custInfoGoupBoxLayout
        )
        wt_custInfoGroupBox.setLayout(lt_custInfoGoupBoxLayout)
        Layout.addWidgetToLayout(wt_custInfoGroupBox, widgetLayout)

        Layout.addMultipleLayoutsToLayout(
            [lt_preferredCat, lt_employeeInCharge, lt_dateTimeDuration],
            lt_resInfoGoupBoxLayout
        )
        wt_resInfoGroupBox.setLayout(lt_resInfoGoupBoxLayout)
        Layout.addWidgetToLayout(wt_resInfoGroupBox, widgetLayout)

        Layout.addLayoutToLayout(discard_create_layout, widgetLayout)

        self.setLayout(widgetLayout)

        # ## SECTION: LOGIC
        # ## THIS SECTION WILL HANDLE THE USER INTERFACE LOGIC
        # ## , SLOTS, SIGNALS, AND ETC.

        wt_discardButton.clicked.connect(slots.clicked_discard_reservation)
        wt_createButton.clicked.connect(slots.clicked_create_reservation)
        wt_firstName.textEdited.connect(slots.textEdited_firstName)
        wt_lastName.textEdited.connect(slots.textEdited_lastName)
        wt_age.textEdited.connect(slots.textEdited_birthdate)
        wt_contactNumber.textEdited.connect(slots.textEdited_contactNumber)
        wt_preferredCat.textEdited.connect(slots.textEdited_preferredCat)
        wt_employeeInCharge.textEdited.connect(
            slots.textEdited_employeeInCharge)
        wt_date.textEdited.connect(slots.textEdited_date)
        wt_time.textEdited.connect(slots.textEdited_time)
        wt_duration.textEdited.connect(slots.textEdited_duration)
