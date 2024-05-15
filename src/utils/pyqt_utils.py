from PySide6 import QtCore
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QHBoxLayout, QHeaderView, QLabel, QLineEdit, QSizePolicy, QSpacerItem, QTableWidgetItem, QVBoxLayout, QTableWidget
from PySide6.QtCore import Qt


class FontsHelperClass():
    def __init__(self):
        print("initializing font helper")
        # configs here

        self.body_text = QFont()
        self.sub_header_text = QFont()
        self.header_text = QFont()

        self.body_text.setBold(False)
        self.body_text.setPointSize(12)

        self.sub_header_text.setBold(True)
        self.sub_header_text.setPointSize(12)

        self.header_text.setBold(True)
        self.header_text.setPointSize(16)


class LineEditHelperClass():
    def __init__(self):
        print("initializing line edit helper")
        # configs here

        self.Vertical = 0
        self.Horizontal = 1

    def create_label_line_edit(self, label_text, line_edit_text, variant):
        label = QLabel(label_text)
        label.setFont(Fonts.body_text)

        line_edit = QLineEdit()
        line_edit.setPlaceholderText(line_edit_text)
        line_edit.setFont(Fonts.body_text)

        if variant == 1:
            h_layout = QHBoxLayout()
            h_layout.addWidget(label)
            h_layout.addWidget(line_edit)

            return h_layout
        else:
            v_layout = QVBoxLayout()
            v_layout.addWidget(label)
            v_layout.addWidget(line_edit)

            return v_layout

    def create_line_edit(self, placeholderText):
        line_edit = QLineEdit()
        line_edit.setPlaceholderText(placeholderText)

        return line_edit

    def add_label_to_line_edit(self, line_edit, label_text, variant):
        label = QLabel(label_text)
        label.setFont(Fonts.body_text)

        if variant == 1:
            h_layout = QHBoxLayout()
            h_layout.addWidget(label)
            h_layout.addWidget(line_edit)

            return h_layout
        else:
            v_layout = QVBoxLayout()
            v_layout.addWidget(label)
            v_layout.addWidget(line_edit)

            return v_layout


class LabelHelperClass():
    def __init__(self):
        print("initializing label helper class")

    def create_label(self, label_text, font):
        label = QLabel(label_text)
        label.setFont(font)

        return label

    def create_centered_label(self, label_text, font):
        label = QLabel(label_text)
        label.setFont(font)

        l_spacer = QSpacerItem(
            20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )
        r_spacer = QSpacerItem(
            20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        h_layout = QHBoxLayout()
        h_layout.addItem(l_spacer)
        h_layout.addWidget(label)
        h_layout.addItem(r_spacer)

        return h_layout


class LayoutHelperClass():
    def __init__(self):
        print("initializing layout helper")
        # configs here

        self.VBox = 0
        self.HBox = 1

    def add_widget_to_layout(self, widget, layout):
        layout.addWidget(widget)

    def add_layout_to_layout(self, child_layout, parent_layout):
        parent_layout.addLayout(child_layout)

    def add_many_widgets_to_layout(self, widgets, layout):
        for widget in widgets:
            layout.addWidget(widget)

    def add_many_layouts_to_layout(self, child_layouts, parent_layout):
        for child_layout in child_layouts:
            parent_layout.addLayout(child_layout)

    def create_layout_from_many_layouts(self, layouts, variant):
        if variant == 1:
            layout = QHBoxLayout()

            for l in layouts:
                layout.addLayout(l)

            return layout
        else:
            layout = QVBoxLayout()

            for l in layouts:
                layout.addLayout(l)

            return layout

    def create_layout_from_many_widgets(self, widgets, variant):
        if variant == 1:
            layout = QHBoxLayout()

            for widget in widgets:
                layout.addWidget(widget)

            return layout
        else:
            layout = QVBoxLayout()

            for widget in widgets:
                layout.addWidget(widget)

            return layout

    def extract_widgets(self, layout, index):
        return layout.itemAt(index).widget()


class TableHelperClass():
    def __init__(self):
        print("initializing table helper")

        self.Normal = 0
        self.Reversed = 1

    def add_column_headers(self, header_titles, table):
        table.setColumnCount(len(header_titles))
        table.setHorizontalHeaderLabels(header_titles)
        header = table.horizontalHeader()
        for i in range(len(header_titles)):
            header.setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)

    def insert_row(self, data, table):
        row_position = table.rowCount()
        table.insertRow(row_position)

        for i in range(len(data)):
            table.setItem(row_position, i, QTableWidgetItem(str(data[i])))

    def insert_rows(self, data, table, order):
        if order == 1:
            for i in reversed(range(len(data))):
                self.insert_row(data[i], table)
        else:
            for i in range(len(data)):
                self.insert_row(data[i], table)

    def clear_table(self, table):
        table.clearContents()
        table.setRowCount(0)


Fonts = FontsHelperClass()
LineEdit = LineEditHelperClass()
Layout = LayoutHelperClass()
Label = LabelHelperClass()
Table = TableHelperClass()
