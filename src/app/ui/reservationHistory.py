from PySide6.QtWidgets import QGroupBox, QHBoxLayout, QHeaderView, QPushButton, QSpacerItem, QTableView, QTableWidget, QVBoxLayout, QWidget
from utils.qt import Fonts, Layout, LineEdit, Label


class ReservationHistory(QWidget):
    def __init__(self):
        super().__init__()

        # ## SECTION: UI
        # ## THIS SECTION OF THE CLASS WILL HANDLE THE CREATE OF THE
        # ## USER INTERFACE

        lt_pageHeader = Label.createCenteredLabel("RESERVATION HISTORY")
        Layout.extractWidget(lt_pageHeader, 1).setFont(Fonts.heroText)

        wt_resTable = QTableWidget()
        wt_resTable.setColumnCount(5)
        wt_resTable.setHorizontalHeaderLabels(
            ["Customer", "Cat", "Date", "Start", "End"])
        header = wt_resTable.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)

        widgetLayout = QVBoxLayout()
        Layout.addLayoutToLayout(lt_pageHeader, widgetLayout)
        Layout.addWidgetToLayout(wt_resTable, widgetLayout)

        self.setLayout(widgetLayout)

        # ## SECTION: LOGIC
        # ## THIS SECTION WILL HANDLE THE USER INTERFACE LOGIC
        # ## , SLOTS, SIGNALS, AND ETC.
