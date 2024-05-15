from PySide6.QtWidgets import QApplication, QMainWindow
import sys

from app.widgets.tab_widget import Tab

app = QApplication(sys.argv)

main_widget = Tab()

main_window = QMainWindow()
main_window.show()
main_window.setCentralWidget(main_widget)

main_window.resize(480, 560)
main_window.setMinimumWidth(480)
main_window.setMinimumHeight(560)

app.exec()
