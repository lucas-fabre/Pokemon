from Base import Pokemon

class Eau(Pokemon):
    def __init__(self, nom, lvl):
        super().__init__(nom, lvl)
        self.setpv(15)
        self.pa += 14
        self.defense += 5