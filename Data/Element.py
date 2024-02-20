class Element:
    def __init__(self, name=None, classes=None, find_all=False):
        if classes is None:
            classes = []

        self._name = name
        self._classes = str(classes).split()
        self._find_all = find_all

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def classes(self):
        return self._classes

    @classes.setter
    def classes(self, value):
        self._classes = str(value).split()

    @property
    def find_all(self):
        return self._find_all

    @find_all.setter
    def find_all(self, value):
        self._find_all = value


