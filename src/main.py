from os import initgroups
from PySide6.QtWidgets import QApplication
from app.ui.window import Window
from app.logic.createReservationLogic import information
import sys
import data.purge as purge
import data.init as init

purge.purge()
init.init_tables()
init.init_cats()
init.init_employee()
init.init_customer()
init.init_reservation()
init.test_customer_select()


app = QApplication(sys.argv)
window = Window()
window.show()

app.exec()
