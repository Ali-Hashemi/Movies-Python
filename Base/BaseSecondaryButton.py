from Config import *


class BaseSecondaryButton(QPushButton):
    def __init__(self, title, parent=None):
        super().__init__(title, parent)

        self.setFont(CustomStyle.radio_btn_font_size)
        self.setStyleSheet("QPushButton"
                           "{"
                           "background-color : blue;"
                           "color: white;"
                           "}"
                           "QPushButton::pressed"
                           "{"
                           "background-color : lightblue;"
                           "}"
                           )
        self.clicked.connect(lambda: (parent.listbox_view.clear()))
        self.setGeometry(CustomStyle.clear_button_size)
