from PySide6.QtWidgets import QGroupBox, QHBoxLayout, QPushButton, QVBoxLayout, QWidget
import utils.pyqt_utils as QtUtil
from app.slots.input_slots import slots


class CreatePage(QWidget):
    def __init__(self):
        super().__init__()
        layout_page_header = QtUtil.Label.create_centered_label(
            "CREATE RESERVATION", QtUtil.Fonts.header_text
        )

        # <-- SUB-SECTION START:
        # --- CUSTOMER INFORMATION
        self.widget_first_name = QtUtil.LineEdit.create_line_edit(
            "customer first name"
        )
        self.widget_last_name = QtUtil.LineEdit.create_line_edit(
            "customer last name"
        )
        self.widget_contact_no = QtUtil.LineEdit.create_line_edit(
            "customer contact number"
        )

        wid_layout_first_name = QtUtil.LineEdit.add_label_to_line_edit(
            self.widget_first_name, "First Name",  QtUtil.LineEdit.Vertical
        )
        wid_layout_last_name = QtUtil.LineEdit.add_label_to_line_edit(
            self.widget_last_name, "Last Name",  QtUtil.LineEdit.Vertical
        )
        wid_layout_contact_no = QtUtil.LineEdit.add_label_to_line_edit(
            self.widget_contact_no, "Contact No.",  QtUtil.LineEdit.Vertical
        )

        layout_customer_info_group = QtUtil.Layout.create_layout_from_many_layouts(
            [wid_layout_first_name, wid_layout_last_name,
                wid_layout_contact_no], QtUtil.Layout.VBox
        )

        widget_customer_info_group = QGroupBox("Customer Information")
        widget_customer_info_group.setLayout(layout_customer_info_group)
        # SUB-SECTION END:     ---
        # CUSTOMER INFORMATION -->

        # <-- SUB-SECTION START:
        # --- RESERVATION INFORMATION
        self.widget_preferred_cat = QtUtil.LineEdit.create_line_edit(
            "preferred cat"
        )
        self.widget_employee_in_charge = QtUtil.LineEdit.create_line_edit(
            "employee in charge"
        )
        self.widget_date = QtUtil.LineEdit.create_line_edit(
            "YYYY-MM-DD"
        )
        self.widget_time_start = QtUtil.LineEdit.create_line_edit(
            "HH:MM"
        )
        self.widget_time_end = QtUtil.LineEdit.create_line_edit(
            "HH:MM"
        )

        wid_layout_preferred_cat = QtUtil.LineEdit.add_label_to_line_edit(
            self.widget_preferred_cat, "Preferred Cat", QtUtil.LineEdit.Vertical
        )
        wid_layout_employee_in_charge = QtUtil.LineEdit.add_label_to_line_edit(
            self.widget_employee_in_charge, "Employee In Charge", QtUtil.LineEdit.Vertical
        )
        wid_layout_date = QtUtil.LineEdit.add_label_to_line_edit(
            self.widget_date, "Date", QtUtil.LineEdit.Vertical
        )
        wid_layout_time_start = QtUtil.LineEdit.add_label_to_line_edit(
            self.widget_time_start, "Time Start", QtUtil.LineEdit.Vertical
        )
        wid_layout_time_end = QtUtil.LineEdit.add_label_to_line_edit(
            self.widget_time_end, "Time End", QtUtil.LineEdit.Vertical
        )

        layout_date_time = QtUtil.Layout.create_layout_from_many_layouts(
            [wid_layout_date, wid_layout_time_start,
                wid_layout_time_end], QtUtil.Layout.HBox
        )
        layout_reservation_info_group = QtUtil.Layout.create_layout_from_many_layouts(
            [wid_layout_preferred_cat, wid_layout_employee_in_charge,
                layout_date_time], QtUtil.Layout.VBox
        )

        widget_reservation_info_group = QGroupBox("Reservation Information")
        widget_reservation_info_group.setLayout(layout_reservation_info_group)
        # SUB-SECTION END:        ---
        # RESERVATION INFORMATION -->

        # <-- SUB-SECTION START:
        # --- ACTION BUTTONS
        self.widget_discard_button = QPushButton("Discard")
        self.widget_create_button = QPushButton("Create")

        layout_action_buttons = QtUtil.Layout.create_layout_from_many_widgets(
            [self.widget_discard_button, self.widget_create_button],
            QtUtil.Layout.HBox
        )
        # SUB-SECTION END:  ---
        # ACTION BUTTONS    -->

        # <-- SUB-SECTION START:
        # --- WIDGET MAIN LAYOUT
        layout_main = QVBoxLayout()

        QtUtil.Layout.add_many_layouts_to_layout(
            [layout_page_header], layout_main
        )
        QtUtil.Layout.add_many_widgets_to_layout(
            [widget_customer_info_group, widget_reservation_info_group], layout_main
        )
        QtUtil.Layout.add_many_layouts_to_layout(
            [layout_action_buttons], layout_main
        )
        # SUB-SECTION END:   ---
        # WIDGET MAIN LAYOUT --n>

        self.setLayout(layout_main)

        self.widget_first_name.textEdited.connect(slots.text_edited_first_name)
        self.widget_last_name.textEdited.connect(slots.text_edited_last_name)
        self.widget_contact_no.textEdited.connect(
            slots.text_edited_contact_number)
        self.widget_preferred_cat.textEdited.connect(
            slots.text_edited_preferred_cat)
        self.widget_employee_in_charge.textEdited.connect(
            slots.text_edited_employee_in_charge)
        self.widget_date.textEdited.connect(slots.text_edited_date)
        self.widget_time_start.textEdited.connect(slots.text_edited_time_start)
        self.widget_time_end.textEdited.connect(slots.text_edited_time_end)
