class TableElement:
    def __init__(self, style, alignment=1):
        self._style = style
        self._alignment = alignment

    @property
    def style(self):
        return self._style

    @style.setter
    def style(self, value):
        self._style = value

    @property
    def alignment(self):
        return self._alignment

    @alignment.setter
    def alignment(self, value):
        self._alignment = value
