from PySide6 import QtCore
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QSizePolicy, QSpacerItem, QVBoxLayout


class FontsHelperClass():
    def __init__(self):
        print("initializing font helper")
        # configs here

        self.bodyText = QFont()
        self.subHeroText = QFont()
        self.heroText = QFont()

        self.bodyText.setBold(False)
        self.bodyText.setPointSize(12)

        self.subHeroText.setBold(True)
        self.subHeroText.setPointSize(12)

        self.heroText.setBold(True)
        self.heroText.setPointSize(16)


class LineEditHelperClass():
    def __init__(self):
        print("initializing line edit helper")
        # configs here

    def createVLabelLineEdit(self, labelText, lineEdit):
        label = QLabel(labelText)
        label.setFont(Fonts.bodyText)

        v_layout = QVBoxLayout()
        v_layout.addWidget(label)
        v_layout.addWidget(lineEdit)
        v_layout.setAlignment(QtCore.Qt.AlignTop)

        return v_layout

    def createHLabelLineEdit(self, labelText, placeholderText):
        label = QLabel(labelText)

        line_edit = QLineEdit()
        line_edit.setPlaceholderText(placeholderText)

        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(line_edit)

        return h_layout

    def createLineEdit(self, placeholderText):
        line_edit = QLineEdit()
        line_edit.setPlaceholderText(placeholderText)

        return line_edit


class LabelHelperClass():
    def __init__(self):
        print("initializing label helper class")

    def createLabel(self, labelText):
        label = QLabel(labelText)

        return label

    def createCenteredLabel(self, labelText):
        label = QLabel(labelText)
        l_spacer = QSpacerItem(
            20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)
        r_spacer = QSpacerItem(
            20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        h_layout = QHBoxLayout()
        h_layout.addItem(l_spacer)
        h_layout.addWidget(label)
        h_layout.addItem(r_spacer)

        return h_layout


class LayoutHelperClass():
    def __init__(self):
        print("initializing layout helper")
        # configs here

    def addWidgetToLayout(self, widget, layout):
        layout.addWidget(widget)

    def addLayoutToLayout(self, child_layout, parent_layout):
        parent_layout.addLayout(child_layout)

    def addMultipleWidgetsToLayout(self, widgets, layout):
        for widget in widgets:
            layout.addWidget(widget)

    def addMultipleLayoutsToLayout(self, child_layouts, parent_layout):
        for child_layout in child_layouts:
            parent_layout.addLayout(child_layout)

    def extractWidget(self, layout, index):
        return layout.itemAt(index).widget()


Fonts = FontsHelperClass()
LineEdit = LineEditHelperClass()
Layout = LayoutHelperClass()
Label = LabelHelperClass()
