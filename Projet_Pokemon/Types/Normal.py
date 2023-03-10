from Base import Pokemon

class Normal(Pokemon):
    def __init__(self, nom, lvl):
        super().__init__(nom, lvl)
        self.setpv(20)
        self.pa += 12
        self.defense += 10