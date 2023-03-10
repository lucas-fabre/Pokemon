import sys
sys.path.append('./Projet_Pokemon/Types')
from Types.Feu import *
from Types.Normal import *
from Types.Terre import *
from Types.Eau import *
from Types.Base import *
import random
import json

#Définie le choix du pokemon que voudra jouer le Joueur 1.
def choix():
    # "f" est une variable créée pour récupérer les objets à l'intérieur du fichier "Pokedex.json".
    with open('./Projet_Pokemon/Pokemon.json') as f:
        #"data" définie l'action d'accéder à la variable "f".
        data = json.load(f)
        #"cpkm" définie l'objet dans le quel récupérer les infos des objets dans l'objet "Pokemon".
        cpkm = data["Pokemon"]
    pc = input("Quel Pokemon voulez vous choisir ?")
    for i in cpkm:
        #"i" compare la string de "pc" à la valeur d'un objet "nom" dans la liste "cpkm" 
        if pc == i["nom"]:
            #Quand "pc" sera égal ("==") à "i", la variable "np" sera créée et prendra la valeur ("=") de "i".
            global np
            np = i["nom"]
        #Quand "i" sera définie par son "nom", la variable "tp" sera créée et prendra la valeur ("=") de l'objet "Type" de "i".
        global tp
        tp = i["Type"]
        #Si la valeur de "tp" est égal ("==") à la valeur de l'objet "Type" de "i".
        if tp == "Eau":
            #Alors la variable "tp" prendra la class ("=") correspondante comme valeur.
            tp = Eau
        if tp == "Feu":
            tp = Feu
        if tp == "Normal":
            tp = Normal
        if tp == "Terre":
            tp = Terre

#Définie le choix aléatoire de l'adversaire, sans comparer une valeur donné dans un "imput" comme dans la fonction "choix" au-dessus.
def adv_choix():
    with open('./Projet_Pokemon/Pokemon.json') as f:
        data = json.load(f)
        cpkm = data["Pokemon"]
    #"ap" permet de récupérer une valeur aléatoirement dans la liste "cpkm" après l'avoir mise en paramètre.
    ap = random.choice(cpkm)
    global np2
    np2 = ap["nom"]
    global tp2
    tp2 = ap["Type"]
    if tp2 == "Eau":
        tp2 = Eau
    if tp2 == "Feu":
        tp2 = Feu
    if tp2 == "Normal":
        tp2 = Normal
    if tp2 == "Terre":
        tp2 = Terre

#Pose les bases de la méchanique de jeu.
class Combat():
    def __init__(self, pkm1, pkm2):
        #"self.fin" définie la condition d'arrêt du duel.
        self.fin = False
        #"self.pkm1" et "self.pkm2" seront les valeurs définies avant le combat, renseignées au début par la fonction "choix (pkm1)" et "adv_choix (pkm2)"
        self.pkm1 = pkm1
        self.pkm2 = pkm2

    #Vérifie la santé des deux Pokemons et détermine la fin du match si la vie d'un des deux tombe à 0.
    def verif_vie(self):
        if self.pkm2.getpv() <= 0:
            self.fin = True
            print("Joueur 1 gagne !")
        
        elif self.pkm1.getpv() <= 0:
            self.fin = True
            print("joueur 2 gagne !")
        
    #Définie le fonctionnement du tour de jeu du Joueur1 et définie aussi si il réussi ou non son attaque.
    def def_tour1(self):
        i1 = random.randint(0, 1)
        c1 = input("Joueur 1, que veux tu faire ?")
        #Définie une boucle pour répéter l'input dans le cas où la personne ne marque pas une action reconnue. 
        while c1 not in ["attaquer", "Attaquer"]:
            print("Je n'ai pas compris, \nJoueur 1, que veux tu faire ?")
            c1 = input()

        #Si l'action est reconnue (== à "attaquer" ou "Attaquer")
        else:
            if i1 == 0:
                #self.pkm1.pa signifie que je veut récupérer la valeur "self.pa" de mon pkm1.
                dmg = self.pkm1.pa - self.pkm2.defense
                self.pkm2.evie(dmg)
                print(self.pkm1.getnom(), "attaque", self.pkm2.getnom(), "et lui infige", dmg, "points de dégâts")
                print(self.pkm2.getnom(), "a", self.pkm2.getpv(), "points de vies")
            
            elif i1 == 1:
                print(self.pkm1.getnom(), "a raté son attaque !")

    #Définie le fonctionnement du tour de jeu du deuxième pokemon et définie aussi si il réussi ou non son attaque.
    def def_tour2(self):
        i2 = random.randint(0, 1)
        c2 = input("Joueur 2, que veux tu faire ?")
        
        while c2 not in ["attaquer", "Attaquer"]:
            print("Je n'ai pas compris, \nJoueur 1, que veux tu faire ?")
            c2 = input()

        else:
            if i2 == 0:
                #Définie le calcul pour enlever des pv au pokemon attaqué.
                dmg = self.pkm2.pa - self.pkm1.defense
                #"self.pkm1.evie(dmg)" est définie dans la class "Base" et permet de décrémenter "dmg" à la valeur de "self.__pv" du pokemon attaqué.
                self.pkm1.evie(dmg)
                print(self.pkm2.getnom(), "attaque", self.pkm1.getnom(), "et lui infige", dmg, "points de dégâts")
                print(self.pkm1.getnom(), "a", self.pkm1.getpv(), "points de vies")
            
            elif i2 == 1:
                print(self.pkm2.getnom(), "a raté son attaque !")
                pass

    #Applique les modifications du tableau pour le pokemon du Joueur 1.
    def comp1(self):
        if tp == Feu:
            if tp2 == Eau:
                self.pkm1.setpa(0.5)
            if tp2 == Terre:
                self.pkm1.setpa(2)
        
        elif tp == Eau:
            if tp2 == Feu:
                self.pkm1.setpa(2)
            if tp2 == Terre:
                self.pkm1.setpa(0.5)
        
        elif tp == Terre:
            if tp2 == Eau:
                self.pkm1.setpa(2)
            if tp2 == Feu:
                self.pkm1.setpa(0.5)

        elif tp == Normal:
            if tp2 == Eau:
                self.pkm1.setpa(0.75)
            if tp2 == Terre:
                self.pkm1.setpa(0.75)
            if tp2 == Feu:
                self.pkm1.setpa(0.75)

    #Applique les modifications du tableau pour le Pokemon du Joueur 2.
    def comp2(self):
        if tp2 == Feu:
            if tp == Eau:
                self.pkm1.setpa(0.5)
            if tp == Terre:
                self.pkm1.setpa(2)
        
        elif tp2 == Eau:
            if tp == Feu:
                self.pkm1.setpa(2)
            if tp == Terre:
                self.pkm1.setpa(0.5)
        
        elif tp2 == Terre:
            if tp == Eau:
                self.pkm1.setpa(2)
            if tp == Feu:
                self.pkm1.setpa(0.5)

        elif tp2 == Normal:
            if tp == Eau:
                self.pkm1.setpa(0.75)
            if tp == Terre:
                self.pkm1.setpa(0.75)
            if tp == Feu:
                self.pkm1.setpa(0.75)

    #La boucle qui va permettre de lancer le combat en vérifiant entre chaque actions des pokemons, les vies de ces derniers avec la condition de victoire.
    def combat(self):
        self.comp1()
        self.comp2()
        #Tant que "self.fin" est n'est pas "True", la boucle se répète.
        while self.fin != True:
            self.def_tour1()
            self.verif_vie()
            self.def_tour2()
            self.verif_vie()

#J'appelle ma fonction "choix" pour choisir mon pokemon.
#J'appelle ma fonction "adv_choix" pour définir aléatoirement l'adversaire.
choix()
adv_choix()

#Définie les objets qui vont être en paramètre de ma classe "Combat".
pkm1 = tp(np, 1)
pkm2 = tp2(np2, 1)
print("Ton adversaire sera", pkm2.getnom())

#Définie la variable de l'instance "Combat" et utilise les objets "pkm1" et "pkm2" comme paramètres.
Duel = Combat(pkm1, pkm2)
#Appelle la méthode "combat" dans la variable d'instance "Duel".
Duel.combat()