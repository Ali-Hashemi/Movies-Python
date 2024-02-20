from Config import *


class BasePrimaryButton(QPushButton):
    def __init__(self, title, parent=None):
        super().__init__(title, parent)

        self.setFont(CustomStyle.radio_btn_font_size)
        self.setStyleSheet("QPushButton"
                           "{"
                           "background-color : red;"
                           "color: white;"
                           "}"
                           "QPushButton::pressed"
                           "{"
                           "background-color : lightgreen;"
                           "color: red"
                           "}"
                           )
        self.clicked.connect(lambda: (parent.get_items(parent.listbox_view)))
        self.setGeometry(CustomStyle.fix_button_size)
