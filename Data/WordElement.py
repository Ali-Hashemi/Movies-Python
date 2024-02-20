class WordElement:
    def __init__(self, content, style, alignment=1, is_checkbox=0, check_state=0, width=None, height=None):
        self._content = content
        self._style = style
        self._alignment = alignment
        self._is_checkbox = is_checkbox
        self._check_state = check_state
        self._width = width
        self._height = height

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

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

    @property
    def is_checkbox(self):
        return self._is_checkbox

    @is_checkbox.setter
    def is_checkbox(self, value):
        self._is_checkbox = value

    @property
    def check_state(self):
        return self._check_state

    @check_state.setter
    def check_state(self, value):
        self._check_state = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
