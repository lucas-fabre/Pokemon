class Pokemon:
    def __init__(self, nom, lvl):
        self.__nom = nom
        self.__pv = 100
        self.level = lvl
        self.defense = 0
        self.coup = ""
        self.pa = 10

    def getpv(self):
        return(self.__pv)
    
    def setpv(self, npv):
        self.__pv += npv
    
    def getnom(self):
        return(self.__nom)
    
    def evie(self, npv):
        self.__pv -= npv
    
    def setpa(self, npa):
        self.pa *= npa

#----BASE DU JEU----#
#1.Définir un nom(privé), TYPE, PV(100)(privé), lvl, PA, DEF(0). X
#2.Créer class Pokemon comportant les stats du point 1. X
#3.Créer class Types qui modifie les valeurs des Pokemons. X
    #Définir les TYPES: Normal, Feu, Eau, Terre. X
    #Créer un fichier pour chaque types. X
    #Chaque "types" heritent class "Pokemon". X

#----COMBATS----#
#1.Créer methode() pour créer combats.
    #Créer methode() vérifie premier 0 vie.
    #Créer methode() return nom gagnant.
    #Créer methode() aleatoire entre 1 et 0.
        #Si 1 alors Pokemon attaque.
        #Si 0 alors attaque raté.
#2.Créer methode() verification PV début combat.
#3.Créer methode() if PV = 0: fin combat/ Nom du Pokemon Gagnant.
#4.Créer methode() return type/puissance de l'adversaire et le multiplie par rapport au tableau.
#5.Créer methode() enlève PV par rapport a DEF.
#6.Créer methode() return Pokemon perdant.
#7.Créer methode() return Pokemon dans Pokedex.

#----Pokedex----#
#1.Créer un fichier Pokedex.json
#2.Créer methode() pour enregistrer infos des Pokemons dans fichier .json.
#3.Créer methode() vérification pour éviter doublons.
#4.Créer methode() afficher les Pokemons et le nombre de fois rencontré.

#----Menus----#
#1.Créer methode() "Lancer une partie".
#2.Créer methode() Ajouter Pokemon dans .json.
#3.Créer methode() Acceder à Pokedex.
