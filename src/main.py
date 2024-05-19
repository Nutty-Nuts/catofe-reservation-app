from PySide6.QtWidgets import QApplication, QMainWindow
from app.widgets.tab_widget import Tab

import sys
import database.purge as purge
import database.init as init

has_args = len(sys.argv) > 1

if has_args:
    if sys.argv[1] == "--purge":
        purge.purge()
    if sys.argv[1] == "--init":
        init.init_tables()
        init.init_customer()
        init.init_employee()
        init.init_cats()
        init.init_reservation()
    if sys.argv[1] == "--reset":
        purge.purge()
        init.init_tables()
        init.init_customer()
        init.init_employee()
        init.init_cats()
        init.init_reservation()

app = QApplication()

main_widget = Tab()

main_window = QMainWindow()
main_window.show()
main_window.setCentralWidget(main_widget)

main_window.resize(480, 560)
main_window.setMinimumWidth(480)
main_window.setMinimumHeight(560)

app.exec()
