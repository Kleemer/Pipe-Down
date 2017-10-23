# -*- coding: cp1252 -*-
#Constantes.py#
#Ce fichier est l'endroit où je stocke toutes les ouvertures des images,        #
#sons et aussi là où je stocke mes constantes, pour épurer le code du programme #
#et pour pouvoir les changer plus rapidement si besoin.                         #

import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((1280,720))

white = (255, 255, 255)
pygame.font.init()
pygame.font.get_fonts()
font = pygame.font.SysFont("arialblack", 80)
logo = pygame.image.load("YAFATA.png").convert_alpha()
quadri = pygame.image.load("Traits.png").convert_alpha()
bouton_apropos = pygame.image.load("Boutons/menu/APropos.png")
newgame = pygame.image.load("Boutons/menu/NouvellePartie.png")
levels = pygame.image.load("Boutons/menu/SelectionNiveau.png")
apropos = pygame.image.load("A Propos.png")
fond_jeu = pygame.image.load("FOND.png")

tuto1 = pygame.image.load("Boutons/ingame/Texte1.png")
tuto2 = pygame.image.load("Boutons/ingame/Texte2.png")
tuto3 = pygame.image.load("Boutons/ingame/Texte3.png")
tuto4 = pygame.image.load("Boutons/ingame/Texte4.png")

n1 = pygame.image.load("Boutons/selection/Tuto.png")
n2 = pygame.image.load("Boutons/selection/Niveau1.png")
n3 = pygame.image.load("Boutons/selection/Niveau2.png")
n4 = pygame.image.load("Boutons/selection/Niveau3.png")
n5 = pygame.image.load("Boutons/selection/Niveau4.png")
n6 = pygame.image.load("Boutons/selection/Niveau5.png")
fond1 = pygame.image.load("fond1.png")
fond2 = pygame.image.load("fond2.png")
fond3 = pygame.image.load("fond3.png")
fond4 = pygame.image.load("fond4.png")
fond5 = pygame.image.load("fond5.png")
fond6 = pygame.image.load("fond6.png")
star1 = pygame.image.load("Boutons/selection/1etoile.png").convert_alpha()
star2 = pygame.image.load("Boutons/selection/2etoiles.png").convert_alpha()
star3 = pygame.image.load("Boutons/selection/3etoiles.png").convert_alpha()
retour = pygame.image.load("Boutons/selection/Retour.png")
bleututo = pygame.image.load("bleututo.png").convert_alpha()
bravotuto = pygame.image.load("Boutons/ingame/Bravo_tuto.png")
bravo5 = pygame.image.load("Boutons/ingame/Bravo_niveau5.png")
bravo = pygame.image.load("Boutons/ingame/Bravo.png")
perdu = pygame.image.load("Boutons/ingame/Perdu.png")

logo_son = pygame.mixer.Sound("Sounds/00 Yafata.wav")
menu_son = pygame.mixer.Sound("Sounds/01 Menu Title.wav")
jeu_son = pygame.mixer.Sound("Sounds/02 In Game Track.wav")
ouverture_son = pygame.mixer.Sound("Sounds/03 Valve Rotating.wav")
win_son = pygame.mixer.Sound("Sounds/05 Win.wav")
fail_son = pygame.mixer.Sound("Sounds/06 Fail.wav")
star1_son = pygame.mixer.Sound("Sounds/07 Getting First Star.wav")
star2_son = pygame.mixer.Sound("Sounds/08 Getting Second Star.wav")
star3_son = pygame.mixer.Sound("Sounds/09 Getting Third Star.wav")

liste_direction = [None, "droite", "bas", "gauche", "haut"]
liste_lettre = ["z", "a", "b", "c", "d", "e", "f", "g", "h", "z"]
liste_tuyau = ["virage", "trait", "croix", "virages", "croixpleine", "viragesplein", "vide"]

depart = pygame.image.load("Tuyaux/Tuyau Initial/TuyauInitial.png").convert_alpha()
croix_vide = pygame.image.load("Tuyaux/Croix/CroixVide.png").convert_alpha()
virages1_vide = pygame.image.load("Tuyaux/Doubles Virages/Config1/ConfigUn.png").convert_alpha()
virages2_vide = pygame.image.load("Tuyaux/Doubles Virages/Config2/ConfigDeux.png").convert_alpha()
horizontal_vide = pygame.image.load("Tuyaux/Droits/Horizontaux/HorizontalVide.png").convert_alpha()
vertical_vide = pygame.image.load("Tuyaux/Droits/Verticaux/VerticalVide.png").convert_alpha()
viragedb_vide = pygame.image.load("Tuyaux/Virages/virage1.png").convert_alpha()
viragedh_vide = pygame.image.load("Tuyaux/Virages/virage4.png").convert_alpha()
viragegb_vide = pygame.image.load("Tuyaux/Virages/virage2.png").convert_alpha()
viragegh_vide = pygame.image.load("Tuyaux/Virages/virage3.png").convert_alpha()
arrivee = pygame.image.load("Tuyaux/Arrivee.png").convert_alpha()
fondfond = pygame.image.load("fondaremettre.png")
noirnoir = pygame.image.load("noiraremettre.png").convert_alpha()

croixdg = []
croixgd = []
croixhb = []
croixbh = []
viragedb = []
viragebd = []
viragegb = []
viragebg = []
viragegh = []
viragehg = []
viragedh = []
viragehd = []
droitvbh = []
droitvhb = []
droithdg = []
droithgd = []
virages1vbg = []
viragesdh = []
virages1vgb = []
virages1vhd = []
virages2vbd = []
virages2vdb = []
virages2vgh = []
virages2vhg = []
finishlist = []


for a in range (11):
    croixdg.append(pygame.image.load("Tuyaux/Droits/Horizontaux/Droite Gauche/{}.png".format(a)).convert_alpha())
    croixgd.append(pygame.image.load("Tuyaux/Droits/Horizontaux/Gauche Droite/{}.png".format(a)).convert_alpha())
    croixhb.append(pygame.image.load("Tuyaux/Droits/Verticaux/Haut Bas/{}.png".format(a)).convert_alpha())
    croixbh.append(pygame.image.load("Tuyaux/Droits/Verticaux/Bas Haut/{}.png".format(a)).convert_alpha())
    viragedb.append(pygame.image.load("Tuyaux/Virages/Droite Bas/{}.png".format(a)).convert_alpha())
    viragebd.append(pygame.image.load("Tuyaux/Virages/Bas Droite/{}.png".format(a)).convert_alpha())
    viragegb.append(pygame.image.load("Tuyaux/Virages/Gauche Bas/{}.png".format(a)).convert_alpha())
    viragebg.append(pygame.image.load("Tuyaux/Virages/Bas Gauche/{}.png".format(a)).convert_alpha())
    viragegh.append(pygame.image.load("Tuyaux/Virages/Gauche Haut/{}.png".format(a)).convert_alpha())
    viragehg.append(pygame.image.load("Tuyaux/Virages/Haut Gauche/{}.png".format(a)).convert_alpha())
    viragedh.append(pygame.image.load("Tuyaux/Virages/Droite Haut/{}.png".format(a)).convert_alpha())
    viragehd.append(pygame.image.load("Tuyaux/Virages/Haut Droite/{}.png".format(a)).convert_alpha())
    droitvbh.append(pygame.image.load("Tuyaux/Droits/Verticaux/Bas Haut/{}.png".format(a)).convert_alpha())
    droitvhb.append(pygame.image.load("Tuyaux/Droits/Verticaux/Haut Bas/{}.png".format(a)).convert_alpha())
    droithdg.append(pygame.image.load("Tuyaux/Droits/Horizontaux/Droite Gauche/{}.png".format(a)).convert_alpha())
    droithgd.append(pygame.image.load("Tuyaux/Droits/Horizontaux/Gauche Droite/{}.png".format(a)).convert_alpha())
    virages1vbg.append(pygame.image.load("Tuyaux/Virages/Bas Gauche/{}.png".format(a)).convert_alpha())
    viragesdh.append(pygame.image.load("Tuyaux/Virages/Droite Haut/{}.png".format(a)).convert_alpha())
    virages1vgb.append(pygame.image.load("Tuyaux/Virages/Gauche Bas/{}.png".format(a)).convert_alpha())
    virages1vhd.append(pygame.image.load("Tuyaux/Virages/Haut Droite/{}.png".format(a)).convert_alpha())
    virages2vbd.append(pygame.image.load("Tuyaux/Virages/Bas Droite/{}.png".format(a)).convert_alpha())
    virages2vdb.append(pygame.image.load("Tuyaux/Virages/Droite Bas/{}.png".format(a)).convert_alpha())
    virages2vgh.append(pygame.image.load("Tuyaux/Virages/Gauche Haut/{}.png".format(a)).convert_alpha())
    virages2vhg.append(pygame.image.load("Tuyaux/Virages/Haut Gauche/{}.png".format(a)).convert_alpha())
    finishlist.append(pygame.image.load("Tuyaux/Droits/Verticaux/Haut Bas/{}.png".format(a)).convert_alpha())

menu = []
depart_anim = []
for a in range (21):
    depart_anim.append(pygame.image.load("Tuyaux/Tuyau Initial/Animation/{}.png".format(a)).convert_alpha())

for a in range (25):
    menu.append(pygame.image.load("Anime/menu-{} (glissees).png".format(a)))


a1 = b1 = c1 = d1 = e1 = f1 = g1 = h1 = 0
a2 = b2 = c2 = d2 = e2 = f2 = g2 = h2 = 0
a3 = b3 = c3 = d3 = e3 = f3 = g3 = h3 = 0
a4 = b4 = c4 = d4 = e4 = f4 = g4 = h4 = 0
a5 = b5 = c5 = d5 = e5 = f5 = g5 = h5 = 0
a6 = b6 = c6 = d6 = e6 = f6 = g6 = h6 = 0
