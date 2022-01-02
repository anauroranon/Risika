class Dice:

    def __init__(self, color, faces_path):
        self.values = list(range(6))
        self.color = color
        self.faces = faces_path

    @property
    def color(self):
        return self._color

    @property
    def faces(self):
        return self._faces

    @color.setter
    def color(self, value):
        self._color = value

    @faces.setter
    def faces(self, value):
        self._faces = value
