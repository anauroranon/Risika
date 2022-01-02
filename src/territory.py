class Territory:

    def __init__(self, name, n_troops=0, centroid=(), card=None):
        self.name = name
        self.n_troops = n_troops
        self.centroid = centroid
        self.card = card

    @property
    def name(self):
        return self._name

    @property
    def n_troops(self):
        return self._n_troops

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) < 50:
            self._name = value
        else:
            raise "Territory name is not valid"

    @n_troops.setter
    def n_troops(self, value):
        if isinstance(value, int):
            self._n_troops = value
        else:
            raise "Territory troops number can only be an integer number"

    @property
    def centroid(self):
        return self._centroid

    @centroid.setter
    def centroid(self, value):
        if isinstance(value, list): #and len(list) == 2:
            self._centroid = value
        else:
            raise "Centroid is wrong"

    def add_troop(self):
        self._n_troops += 1









