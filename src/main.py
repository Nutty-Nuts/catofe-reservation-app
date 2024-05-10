from PySide6.QtWidgets import QApplication
from app.ui.window import Window
from utils.sql import INSERT_ENTITY_INSTANCE, CREATE_TABLE
from app.logic.createReservationLogic import reservationInformation
import sys

app = QApplication(sys.argv)

window = Window()
window.show()

app.exec()

print(reservationInformation)
