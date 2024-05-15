from PySide6.QtWidgets import QTableWidget, QVBoxLayout, QWidget
import utils.pyqt_utils as QtUtil


class ReservationPage(QWidget):
    def __init__(self):
        super().__init__()

        layout_page_header = QtUtil.Label.create_centered_label(
            "RESERVATIONS", QtUtil.Fonts.header_text
        )

        self.widget_reservation_table = QTableWidget()
        self.widget_reservation_table.verticalHeader().setVisible(False)
        QtUtil.Table.add_column_headers(
            ["id", "name", "contact_no", "cat", "date", "start", "end"],
            self.widget_reservation_table
        )

        layout_main = QVBoxLayout()

        QtUtil.Layout.add_layout_to_layout(
            layout_page_header, layout_main
        )
        QtUtil.Layout.add_widget_to_layout(
            self.widget_reservation_table, layout_main
        )

        self.setLayout(layout_main)

    def refresh(self, new_data):
        QtUtil.Table.clear_table(self.widget_reservation_table)
        QtUtil.Table.insert_rows(
            new_data, self.widget_reservation_table, QtUtil.Table.Reversed
        )
