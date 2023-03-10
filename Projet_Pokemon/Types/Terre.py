from Base import Pokemon

class Terre(Pokemon):
    def __init__(self, nom, lvl):
        super().__init__(nom, lvl)
        self.setpv(30)
        self.pa += 14
        self.defense += 11