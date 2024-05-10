from PySide6.QtWidgets import QTabWidget, QWidget, QVBoxLayout
from app.ui.createReservation import CreateReservation
from app.ui.manageReservation import ManageReservations
from app.ui.reservationHistory import ReservationHistory
from utils.qt import Layout


class Window(QWidget):  # application window
    def __init__(self):
        super().__init__()

        tabWidget = QTabWidget()
        tabWidget.addTab(CreateReservation(), "Create")
        tabWidget.addTab(ManageReservations(), "Manage")
        tabWidget.addTab(ReservationHistory(), "History")

        windowLayout = QVBoxLayout()
        Layout.addMultipleWidgetsToLayout([tabWidget], windowLayout)

        self.setLayout(windowLayout)
