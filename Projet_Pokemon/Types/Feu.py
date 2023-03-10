from Base import Pokemon

class Feu(Pokemon):
    def __init__(self, nom, lvl):
        super().__init__(nom, lvl)
        self.setpv(10)
        self.pa += 12
        self.defense += 12