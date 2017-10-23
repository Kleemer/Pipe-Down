# -*- coding: cp1252 -*-

#PIPE DOWN : Version 1.01

print("Début des importations ...")
from constantes import *
print("Importation Constantes terminée !")
from fonctions import *
print("Importation Fonctions terminée !")
import pygame
from pygame.locals import *
print("Importation PyGame terminée !")
print("Lancement du jeu !")

def remplissage(coo, recup, origine, a, pos_x, pos_y, numeroabs, numeroord, niveau):
    global fini
    possibilite = str("config"+coo)
    recup = eval(possibilite)
    
    if origine in recup:
        g = str(origine+"gauche")
        d = str(origine+"droite")
        h = str(origine+"haut")
        b = str(origine+"bas")
        
        if g in recup:
            a = str("tuyau"+coo)
            a = eval(a)
            anim = str(a+origine+"gauche")
            anim = eval(anim)
            anim(pos_x,pos_y)
            numeroabs -= 1
            pos_x -= 120
            coo = str(liste_lettre[numeroabs]+numeroord)
            origine = "droite"
            remplissage(coo, recup, origine, a, pos_x, pos_y, numeroabs, numeroord, niveau)
            
        elif d in recup:
            a = str("tuyau"+coo)
            a = eval(a)
            anim = str(a+origine+"droite")
            anim = eval(anim)
            anim(pos_x,pos_y)
            numeroabs += 1
            pos_x += 120
            coo = str(liste_lettre[numeroabs]+numeroord)
            origine = "gauche"
            remplissage(coo, recup, origine, a, pos_x, pos_y, numeroabs, numeroord, niveau)
            
        elif h in recup:
            a = str("tuyau"+coo)
            a = eval(a)
            anim = str(a+origine+"haut")
            anim = eval(anim)
            anim(pos_x,pos_y)
            pos_y -= 120
            numeroord = int(numeroord)
            numeroord -= 1
            numeroord = str(numeroord)
            coo = str(liste_lettre[numeroabs]+numeroord)
            origine = "bas"
            remplissage(coo, recup, origine, a, pos_x, pos_y, numeroabs, numeroord, niveau)
            
        elif b in recup:
            a = (str("tuyau"+coo))
            a = eval(a)
            anim = str(a+origine+"bas")
            anim = eval(anim)
            anim(pos_x,pos_y)
            pos_y += 120
            numeroord = int(numeroord)
            numeroord += 1
            numeroord = str(numeroord)
            coo = str(liste_lettre[numeroabs]+numeroord)
            origine = "haut"
            
            #Détection de victoire :
            if coo == "g6" and niveau == 2 or coo == "g6" and niveau == 3 or coo == "g6" and niveau == 4 or coo == "g6" and niveau == 5 or coo == "a6" and niveau == 6:
                finish(pos_x,pos_y, niveau)
                clics = font.render(coup, True, white)
                texteclic = font.render("clics !", True, white)
                fenetre.blit(clics,(420,300))
                fenetre.blit(texteclic, (600,300))
                pygame.display.flip()
                etoile(niveau, coup)
                fini = 1
                return fini
            #Pas de victoire, la boucle se rappelle
            else:
                remplissage(coo, recup, origine, a, pos_x, pos_y, numeroabs, numeroord, niveau)

        #Détection de défaite                    
        elif "vide" in recup:
            pygame.time.delay(500)
            fenetre.blit(perdu, (0,0))
            jeu_son.stop()
            fail_son.play()
            pygame.display.flip()
            fini = 0
            return fini
        
    #Détection de défaite 
    else:
        pygame.time.delay(500)
        fenetre.blit(perdu, (0,0))
        jeu_son.stop()
        fail_son.play()
        pygame.display.flip()
        fini = 0
        return fini
                
pygame.init()

#Quelques paramètres d'affichages pour Pygame
pygame.display.set_caption("Pipe Down")
fenetre = pygame.display.set_mode((1280,720))

#Intro
fenetre.blit(logo, (388,288))
pygame.display.flip()
logo_son.play()
pygame.time.delay(1000)

#Toutes les variables qui nous permettent de faire des boucles while
continuer = 1
continuer_menu = 1
continuer_selection = 1
continuer_apropos = 1
continuer_jeu = 1
continuer_niveau = 1
continuer_retourselection = 1
niveau = 0
menu_son.play(10)
menu_musique = 1

#Boucle principale
while continuer:

    #On réinitialise toutes les variables pour pouvoir retourner au menu une fois un niveau fini ou quitté par l'utilisateur
    continuer_menu = 1
    continuer_selection = 1
    continuer_apropos = 1
    continuer_jeu = 1
    continuer_niveau = 1


    while continuer_menu and continuer_retourselection:

        #Affichage menu
        for a in range (25):
            fenetre.blit(menu[a], (0,0))
            fenetre.blit(newgame, (820,100))
            fenetre.blit(levels, (820,300))
            fenetre.blit(bouton_apropos, (820,500))
            pygame.display.flip()
            a += 1

        #Reconnaissance d'évènements
        for event in pygame.event.get():

            if event.type == QUIT:
                continuer = 0
                pygame.quit()

            if event.type == MOUSEBUTTONUP:

                if event.button == 1:
                    
                    p_x = event.pos[0]
                    p_y = event.pos[1]

                    if p_x >820 and p_x < 1080:

                        #Nouvelle partie (= tuto)
                        if p_y > 100 and p_y < 222:
                            menu_musique = 0
                            menu_son.stop()
                            jeu_son.play(10)
                            niveau = 1
                            continuer_menu = 0
                            continuer_selection = 0
                            continuer_apropos = 0

                        #Sélection niveaux
                        elif p_y > 300 and p_y < 422:
                            continuer_menu = 0
                            continuer_apropos = 0

                        #A propos
                        elif p_y > 500 and p_y < 622:
                            continuer_menu = 0
                            continuer_selection = 0

    #Boucle de la sélection niveau
    while continuer_selection:

        fenetre.blit(fond_jeu, (0,0))
        fenetre.blit(n1, (40,70))
        fenetre.blit(n2, (440,70))
        fenetre.blit(n3, (840,70))
        fenetre.blit(n4, (40,350))
        fenetre.blit(n5, (440,350))
        fenetre.blit(n6, (840,350))
        fenetre.blit(retour, (505, 570))
        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == QUIT:
                continuer = 0
                pygame.quit()

            if event.type == MOUSEBUTTONUP:

                if event.button == 1:

                    p_x = event.pos[0]
                    p_y = event.pos[1]

                    if p_x > 505 and p_x < 769:

                        #Bouton retour
                        if p_y > 570 and p_y < 696:
                            if menu_musique == 0:
                                menu_musique = 1
                                jeu_son.stop()
                                menu_son.play(10)
                            niveau = 0
                            continuer_selection = 0
                            continuer_apropos = 0

                    if p_x > 40 and p_x < 436:

                        #Tutoriel
                        if p_y > 70 and p_y < 264:
                            
                            if menu_musique == 1:
                                menu_musique = 0
                                menu_son.stop()
                                jeu_son.play(10)
                            
                            niveau = 1
                            continuer_selection = 0
                            continuer_apropos = 0

                        #Niveau 3
                        elif p_y > 350 and p_y < 544:
                            
                            if menu_musique == 1:
                                menu_musique = 0
                                menu_son.stop()
                                jeu_son.play(10)
                            
                            niveau = 4
                            continuer_selection = 0
                            continuer_apropos = 0

                    elif p_x > 440 and p_x < 836:

                        #Niveau 1
                        if p_y > 70 and p_y < 264:

                            if menu_musique == 1:
                                menu_musique = 0
                                menu_son.stop()
                                jeu_son.play(10)
    
                            niveau = 2
                            continuer_selection = 0
                            continuer_apropos = 0

                        #Niveau 4
                        elif p_y > 350 and p_y < 544:

                            if menu_musique == 1:
                                menu_musique = 0
                                menu_son.stop()
                                jeu_son.play(10)

                            niveau = 5
                            continuer_selection = 0
                            continuer_apropos = 0

                    elif p_x > 840 and p_x < 1236:

                        #Niveau 2
                        if p_y > 70 and p_y < 264:

                            if menu_musique == 1:
                                menu_musique = 0
                                menu_son.stop()
                                jeu_son.play(10)

                            niveau = 3
                            continuer_selection = 0
                            continuer_apropos = 0

                        #Niveau 5
                        elif p_y > 350 and p_y < 544:

                            if menu_musique == 1:
                                menu_musique = 0
                                menu_son.stop()
                                jeu_son.play(10)
                            
                            niveau = 6
                            continuer_selection = 0
                            continuer_apropos = 0

    #Boucle du menu à propos, qui est sautée lorsqu'un niveau est choisi dans la Sélection
    while continuer_apropos:

        fenetre.blit(apropos, (0,0))
        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == QUIT:

                continuer = 0
                pygame.quit()

            if event.type == MOUSEBUTTONUP:

                p_x = event.pos[0]
                p_y = event.pos[1]

            #Bouton retour
            if p_x > 505 and p_x < 769:
                if p_y > 570 and p_y < 696:

                    niveau = 0
                    continuer_menu = 0
                    continuer_selection = 0
                    continuer_apropos = 0


    #Boucle jeu principale, qui contient la boucle continuer_niveau
    while continuer_jeu:
        continuer_niveau = 1
        
        #Les boutons Retour renvoient ici, qui renvoie directement au début de la boucle
        if niveau == 0:

            continuer_jeu = 0
            continuer_menu = 1
            continuer_retourselection = 1

        #Tutoriel
        elif niveau == 1:
            
            fenetre.blit(fond1, (0,0))
            fenetre.blit(depart,(120,0))
            fenetre.blit(horizontal_vide, (480,360))
            fenetre.blit(virages1_vide, (240,360))
            fenetre.blit(croix_vide, (600, 360))
            fenetre.blit(viragedh_vide, (120,120))
            fenetre.blit(viragegb_vide, (240,120))
            fenetre.blit(viragegb_vide, (720,360))
            fenetre.blit(croix_vide, (240,240))
            fenetre.blit(vertical_vide, (360,360))
            fenetre.blit(vertical_vide, (720,480))
            fenetre.blit(vertical_vide, (720,600))
            fenetre.blit(arrivee, (720,600))
            fenetre.blit(quadri, (0,0))
            pygame.display.flip()
            pygame.time.delay(1000)
            fenetre.blit(tuto1, (0,0))
            pygame.display.flip()
            pygame.time.delay(1000)
            fenetre.blit(tuto2, (0,0))
            pygame.display.flip()
            pygame.time.delay(1000)
            fenetre.blit(tuto3, (0,0))
            pygame.display.flip()
            
            i = j = 0
            numeroabs = 1
            numeroord = 1
            fait = 0
            fini = 0

            while continuer_niveau:
                for event in pygame.event.get():

                    if event.type == QUIT:
                        continuer = 0
                        pygame.quit()

                    elif event.type == MOUSEBUTTONUP:

                        pos_x = event.pos[0]
                        pos_y = event.pos[1]

                        if pos_x > 970 and pos_x < 1270:

                            if pos_y > 360 and pos_y < 500:
                                menu_musique = 1
                                jeu_son.stop()
                                menu_son.play(10)
                                continuer_niveau = 0
                                continuer_jeu = 0
                                continuer_menu = 1
                                continuer_retourselection = 1

                            elif pos_y > 520 and pos_y <680:
                                continuer_niveau = 0
                                continuer_jeu = 0
                                continuer_retourselection = 0

                        while i < 960:

                            if pos_x > i+120:
                                i += 120
                                numeroabs += 1

                            else:
                                pos_x = i
                                i = 960

                        while j < 720:

                            if pos_y > j+120:
                                j += 120
                                numeroord += 1

                            else:
                                pos_y = j
                                j = 720

                        numeroord = str(numeroord)
                        coo = str(liste_lettre[numeroabs]+numeroord)

                        if coo == "d4":
                            fenetre.blit(fondfond, (pos_x, pos_y))
                            fenetre.blit(horizontal_vide, (pos_x, pos_y))
                            fenetre.blit(quadri, (0,0))
                            fenetre.blit(tuto1, (0,0))
                            fenetre.blit(tuto2, (0,0))
                            fenetre.blit(tuto3, (0,0))
                            fenetre.blit(tuto4, (0,0))
                            pygame.display.flip()
                            fait = 1

                        if coo == "b1" and fait == 1:
                            fenetre.blit(bleututo, (0,0))
                            departanim(120,0)
                            viragehautdroite(120,120)
                            viragegauchebas(240,120)
                            croixhautbas(240,240)
                            virageshautdroite(240,360)
                            traitgauchedroite(360,360)
                            traitgauchedroite(480,360)
                            croixgauchedroite(600,360)
                            viragegauchebas(720,360)
                            traithautbas(720,480)
                            finish(720,600, niveau)
                            fini = 1

                        if event.type == MOUSEBUTTONUP and fini == 1:

                            pos_x = event.pos[0]
                            pos_y = event.pos[1]

                            if pos_y > 500:
                                niveau = niveau + 1
                                continuer_niveau = 0
                                continuer_menu = 0
                                continuer_retourselection = 0
                                continuer_selection = 0
                                continuer_jeu = 1
                                continuer_apropos = 0
                                
                        i = j = 0
                        coo = 0
                        numeroord = numeroabs = 1

        #Niveau 1
        elif niveau == 2:

            fenetre.blit(fond2, (0,0))
            fenetre.blit(depart,(120,0))
            fenetre.blit(viragedb_vide, (120,120))
            fenetre.blit(viragedb_vide, (240,120))
            fenetre.blit(viragedb_vide, (120,240))
            fenetre.blit(horizontal_vide, (240,240))
            fenetre.blit(horizontal_vide, (360,240))
            fenetre.blit(horizontal_vide, (480,240))
            fenetre.blit(croix_vide, (720,240))
            fenetre.blit(horizontal_vide, (240,360))
            fenetre.blit(viragedb_vide, (360,360))
            fenetre.blit(horizontal_vide, (480,360))
            fenetre.blit(horizontal_vide, (600,360))
            fenetre.blit(viragedb_vide, (720,360))
            fenetre.blit(viragedb_vide, (120,480))
            fenetre.blit(croix_vide, (240, 480))
            fenetre.blit(horizontal_vide, (360,480))
            fenetre.blit(viragedb_vide, (600,480))
            fenetre.blit(horizontal_vide, (720,480))
            fenetre.blit(virages1_vide, (240,600))
            fenetre.blit(viragedb_vide, (360,600))
            fenetre.blit(vertical_vide, (720,600))
            fenetre.blit(arrivee, (720,600))
            fenetre.blit(quadri, (0,0))

            fini = 2
            
            tuyaub2 = tuyauc2 = tuyaub3 = tuyaud4 = tuyaug4 = tuyaub5 = tuyauf5 = tuyaud6 = liste_tuyau[0]
            configb2 = configc2 = configb3 = configd4 = configg4 = configb5 = configf5 = configd6 = "droitebas basdroite"
            tuyauc3 = tuyaud3 = tuyaue3 = tuyauc4 = tuyaue4 = tuyauf4 = tuyaud5 = tuyaug5 = tuyaug6 = liste_tuyau[1]
            configc3 = configd3 = confige3 = configc4 = confige4 = configf4 = configd5 = configg5 = "gauchedroite droitegauche"  
            tuyaug3 = tuyauc5 = liste_tuyau[2]
            configc5 = configg3 = "hautbas bashaut gauchedroite droitegauche"
            tuyauc6 = liste_tuyau[3]
            configc6 = "hautdroite droitehaut basgauche gauchebas"
            configg6 = "hautbas bashaut"
            b2 = c2 = 1
            b3 = c3 = d3 = e3 = g3 = 1
            c4 = d4 = e4 = f4 = g4 = 1
            b5 = c5 = d5 = f5 = g5 = 1
            c6 = d6 = g6 = 1
            configa7 = configb7 = configc7 = configd7 = confige7 = configf7 = configg7 = configh7 = configa0 = configb0 = configc0 = configd0 = confige0 = configf0 = configg0 = configh0 = configa1 = configa2 = configa3 = configa4 = configa5 = configa6 = configb1 = configb4 = configb6 = configc1 = configd1 = configd2 = confige1 = confige2 = confige5 = confige6 = configf1 = configf2 = configf3 = configf6 = configg1 = configg2 = configh1 = configh2 = configh3 = configh4 = configh5 = configh6 = liste_tuyau[6]
            i = j = 0
            
            origine = 0
            origine = str(origine)

            numeroabs = 1
            numeroord = 1
            coup = 0
            coup = str(coup)
            clics = font.render(coup, True, white)
            fenetre.blit(clics, (1120-(len(coup)*53)/2,142))
            pygame.display.flip()

            while continuer_niveau:
                for event in pygame.event.get():

                    if event.type == QUIT:
                        continuer = 0
                        pygame.quit()

                    elif event.type == MOUSEBUTTONUP and fini == 2:

                        pos_x = event.pos[0]
                        pos_y = event.pos[1]

                        if pos_x > 970 and pos_x < 1270:

                            if pos_y > 360 and pos_y < 500:
                                menu_musique = 1
                                jeu_son.stop()
                                menu_son.play(10)
                                continuer_niveau = 0
                                continuer_jeu = 0
                                continuer_menu = 1
                                continuer_retourselection = 1

                            elif pos_y > 520 and pos_y <680:
                                continuer_niveau = 0
                                continuer_jeu = 0
                                continuer_retourselection = 0
                                
                        while i < 960:

                            if pos_x > i+120:
                                i += 120
                                numeroabs += 1

                            else:
                                pos_x = i
                                i = 960

                        while j < 720:

                            if pos_y > j+120:
                                j += 120
                                numeroord += 1

                            else:
                                pos_y = j
                                j = 720

                        numeroord = str(numeroord)
                        coo = str(liste_lettre[numeroabs]+numeroord)

                        if coo == "b2":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            b2 += 1
                            if b2 > 4:
                                b2 = 1

                            pos = liste_direction[b2]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb2 = "droitebas basdroite"
                                

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb2 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb2 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb2 = "droitehaut hautdroite"

                        elif coo == "c2":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            c2 += 1
                            if c2 > 4:
                                c2 = 1

                            pos = liste_direction[c2]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc2 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc2 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc2 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc2 = "droitehaut hautdroite"

                        elif coo == "b3":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            b3 += 1
                            if b3 > 4:
                                b3 = 1

                            pos = liste_direction[b3]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb3 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                config3 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb3 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb3 = "droitehaut hautdroite"

                        elif coo == "d4":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            d4 += 1
                            if d4 > 4:
                                d4 = 1

                            pos = liste_direction[d4]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd4 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd4 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd4 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd4 = "droitehaut hautdroite"

                        elif coo == "g4":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            g4 += 1
                            if g4 > 4:
                                g4 = 1

                            pos = liste_direction[g4]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg4 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg4 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg4 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg4 = "droitehaut hautdroite"

                        elif coo == "b5":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            b5 += 1
                            if b5 > 4:
                                b5 = 1

                            pos = liste_direction[b5]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb5 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb5 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb5 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                liste_b5 = "droitehaut hautdroite"

                        elif coo == "f5":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            f5 += 1
                            if f5 > 4:
                                f5 = 1

                            pos = liste_direction[f5]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf5 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf5 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf5 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf5 = "droitehaut hautdroite"

                        elif coo == "d6":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            d6 += 1
                            if d6 > 4:
                                d6 = 1

                            pos = liste_direction[d6]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd6 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd6 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd6 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd6 = "droitehaut hautdroite"

                        elif coo == "c3":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            c3 += 1
                            if c3 > 2:
                                c3 = 1

                            pos = liste_direction[c3]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc3 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc3 = "hautbas bashaut"

                        elif coo == "d3":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            d3 += 1
                            if d3 > 2:
                                d3 = 1

                            pos = liste_direction[d3]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd3 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd3 = "hautbas bashaut"


                        elif coo == "e3":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            e3 += 1
                            if e3 > 2:
                                e3 = 1

                            pos = liste_direction[e3]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                confige3 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                confige3 = "hautbas bashaut"


                        elif coo == "c4":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            c4 += 1
                            if c4 > 2:
                                c4 = 1

                            pos = liste_direction[c4]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc4 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc4 = "hautbas bashaut"


                        elif coo == "e4":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            e4 += 1
                            if e4 > 2:
                                e4 = 1

                            pos = liste_direction[e4]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                confige4 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                confige4 = "hautbas bashaut"


                        elif coo == "f4":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            f4 += 1
                            if f4 > 4:
                                f4 = 1

                            pos = liste_direction[f4]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf4 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf4 = "hautbas bashaut"


                        elif coo == "d5":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            d5 += 1
                            if d5 > 2:
                                d5 = 1

                            pos = liste_direction[d5]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                liste_d5 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd5 = "hautbas bashaut"


                        elif coo == "g5":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            g5 += 1
                            if g5 > 2:
                                g5 = 1

                            pos = liste_direction[g5]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg5 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg5 = "hautbas bashaut"


                        elif coo == "c6":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            c6 += 1
                            if c6 > 2:
                                c6 = 1

                            pos = liste_direction[c6]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(virages1_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc6 = "hautdroite droitehaut basgauche gauchebas"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(virages2_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc6 = "hautgauche gauchehaut basdroite droitebas"

                        elif coo == "b1":
                            departanim(pos_x, pos_y)
                            numeroord = int(numeroord)
                            numeroord += 1
                            numeroord = str(numeroord)
                            coo = str(liste_lettre[numeroabs]+(numeroord))
                            origine = "haut"
                            pos_y += 120
                            recup = "0"
                            a = "0"
                            remplissage(coo, recup, origine, a, pos_x, pos_y, numeroabs, numeroord, niveau)
                            
                    if event.type == MOUSEBUTTONUP and fini == 1:

                        pos_x = event.pos[0]
                        pos_y = event.pos[1]

                        if pos_y > 500:
                            niveau += 1
                            continuer_niveau=0
                            continuer_menu=0
                            continuer_retourselection=0
                            continuer_selection=0
                            continuer_apropos=0
                            continuer_jeu = 1

                    elif event.type == MOUSEBUTTONUP and fini == 0:

                        pos_x = event.pos[0]
                        pos_y = event.pos[1]

                        if pos_y > 500:
                            jeu_son.play(10)
                            continuer_niveau=0
                            continuer_menu=0
                            continuer_retourselection = 0
                            continuer_selection = 0
                            continuer_apropos = 0
                            continuer_jeu = 1
                        
                if fini == 2:    
                    fenetre.blit(noirnoir, (0,0))
                    clics = font.render(coup, True, white)
                    fenetre.blit(clics, (1120-(len(coup)*53)/2,142))
                    pygame.display.flip()
                    
                i = j = 0
                coo = 0
                numeroabs = numeroord = 1

        #Niveau 2
        elif niveau == 3:

            fenetre.blit(fond3, (0,0))
            fenetre.blit(depart,(0,0))
            fenetre.blit(viragedb_vide, (120,0))
            fenetre.blit(viragedb_vide, (240,0))
            fenetre.blit(viragedb_vide, (360,0))
            fenetre.blit(horizontal_vide, (0,120))
            fenetre.blit(croix_vide, (120,120))
            fenetre.blit(virages1_vide, (240,120))
            fenetre.blit(viragedb_vide, (360,120))
            fenetre.blit(viragedb_vide, (0,240))
            fenetre.blit(virages1_vide, (120,240))
            fenetre.blit(horizontal_vide, (240,240))
            fenetre.blit(viragedb_vide, (360,240))
            fenetre.blit(viragedb_vide, (480,240))
            fenetre.blit(viragedb_vide, (0,360))
            fenetre.blit(croix_vide, (120,360))
            fenetre.blit(horizontal_vide, (240,360))
            fenetre.blit(viragedb_vide, (360,360))
            fenetre.blit(virages1_vide, (480,360))
            fenetre.blit(horizontal_vide, (600,360))
            fenetre.blit(viragedb_vide, (720,360))
            fenetre.blit(viragedb_vide, (120,480))
            fenetre.blit(viragedb_vide, (240,480))
            fenetre.blit(horizontal_vide, (720,480))
            fenetre.blit(vertical_vide, (720,600))
            fenetre.blit(arrivee, (720,600))
            fenetre.blit(quadri, (0,0))

            tuyaub1 = tuyauc1 = tuyaud1 = tuyaud2 = tuyaua3 = tuyaud3 = tuyaue3 = tuyaua4 = tuyaud4 = tuyaug4 = tuyaub5 = tuyauc5 = liste_tuyau[0]
            configb1 = configc1 = configd1 = configd2 = configa3 = configd3 = confige3 = configa4 = configd4 = configg4 = configb5 = configc5 = "droitebas basdroite"
            tuyaua2 = tuyauc3 = tuyauc4 = tuyauf4 = tuyaug5 = liste_tuyau[1]
            configa2 = configc3 = configc4 = configf4 = configg5 = "gauchedroite droitegauche"  
            tuyaub2 = tuyaub4 = liste_tuyau[2]
            configb2 = configb4 = "hautbas bashaut gauchedroite droitegauche"
            tuyauc2 = tuyaub3 = tuyaue4 = liste_tuyau[3]
            configc2 = configb3 = confige4 = "hautdroite droitehaut basgauche gauchebas"
            configg6 = "hautbas bashaut"
            configa7 = configb7 = configc7 = configd7 = confige7 = configf7 = configg7 = configh7 = configa0 = configb0 = configc0 = configd0 = confige0 = configf0 = configg0 = configh0 = configa5 = configa6 = configb6 = configc6 = configd5 = configd6 = confige1 = confige2 = confige5 = confige6 = configf1 = configf2 = configf3 = configf5 = configf6 = configg1 = configg2 = configg3 = configh1 = configh2 = configh3 = configh4 = configh5 = configh6 = configz1 = configz2 = configz3 = configz4 = configz5 = configz6 = liste_tuyau[6]
            
            fini = 2
            a1 = b1 = c1 = d1 = 1
            a2 = b2 = c2 = d2 = 1
            a3 = b3 = c3 = d3 = e3 = 1
            a4 = b4 = c4 = d4 = e4 = f4 = g4 = 1
            b5 = c5 = g5 = 1
            g6 = 1
            
            i = j = 0
            numeroabs = 1
            numeroord = 1
            coup = 0
            coup = str(coup)
            clics = font.render(coup, True, white)
            fenetre.blit(clics, (1120-(len(coup)*53)/2,142))
            pygame.display.flip()

            while continuer_niveau:
                for event in pygame.event.get():

                    if event.type == QUIT:
                        continuer = 0
                        pygame.quit()

                    elif event.type == MOUSEBUTTONUP and fini == 2:

                        pos_x = event.pos[0]
                        pos_y = event.pos[1]

                        if pos_x > 970 and pos_x < 1270:

                            if pos_y > 360 and pos_y < 500:
                                menu_musique = 1
                                jeu_son.stop()
                                menu_son.play(10)
                                continuer_niveau = 0
                                continuer_jeu = 0
                                continuer_menu = 1
                                continuer_retourselection = 1

                            elif pos_y > 520 and pos_y <680:
                                continuer_niveau = 0
                                continuer_jeu = 0
                                continuer_retourselection = 0

                        while i < 960:

                            if pos_x > i+120:
                                i += 120
                                numeroabs += 1

                            else:
                                pos_x = i
                                i = 960

                        while j < 720:

                            if pos_y > j+120:
                                j += 120
                                numeroord += 1

                            else:
                                pos_y = j
                                j = 720

                        numeroord = str(numeroord)
                        coo = str(liste_lettre[numeroabs]+numeroord)

                        if coo == "b1":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            b1 += 1
                            if b1 > 4:
                                b1 = 1

                            pos = liste_direction[b1]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb1 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb1 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb1 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb1 = "droitehaut hautdroite"

                        if coo == "c1":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            c1 += 1
                            if c1 > 4:
                                c1 = 1

                            pos = liste_direction[c1]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc1 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc1 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc1 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc1 = "droitehaut hautdroite"

                        if coo == "d1":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            d1 += 1
                            if d1 > 4:
                                d1 = 1

                            pos = liste_direction[d1]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd1 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd1 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd1 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd1 = "droitehaut hautdroite"

                        if coo == "d2":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            d2 += 1
                            if d2 > 4:
                                d2 = 1

                            pos = liste_direction[d2]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd2 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd2 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd2 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd2 = "droitehaut hautdroite"

                        if coo == "a3":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            a3 += 1
                            if a3 > 4:
                                a3 = 1

                            pos = liste_direction[a3]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configa3 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configa3 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configa3 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configa3 = "droitehaut hautdroite"


                        if coo == "d3":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            d3 += 1
                            if d3 > 4:
                                d3 = 1

                            pos = liste_direction[d3]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd3 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd3 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd3 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd3 = "droitehaut hautdroite"

                        if coo == "e3":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            e3 += 1
                            if e3 > 4:
                                e3 = 1

                            pos = liste_direction[e3]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                confige3 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                confige3 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                confige3 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                confige3 = "droitehaut hautdroite"

                        if coo == "a4":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            a4 += 1
                            if a4 > 4:
                                a4 = 1

                            pos = liste_direction[a4]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configa4 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configa4 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configa4 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configa4 = "droitehaut hautdroite"


                        if coo == "d4":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            d4 += 1
                            if d4 > 4:
                                d4 = 1

                            pos = liste_direction[d4]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd4 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd4 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd4 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd4 = "droitehaut hautdroite"

                        if coo == "g4":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            g4 += 1
                            if g4 > 4:
                                g4 = 1

                            pos = liste_direction[g4]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg4 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg4 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg4 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg4 = "droitehaut hautdroite"

                        if coo == "b5":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            b5 += 1
                            if b5 > 4:
                                b5 = 1

                            pos = liste_direction[b5]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb5 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb5 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb5 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb5 = "droitehaut hautdroite"

                        elif coo == "c5":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            c5 += 1
                            if c5 > 4:
                                c5 = 1

                            pos = liste_direction[c5]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc5 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc5 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc5 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc5 = "droitehaut hautdroite"

                        elif coo == "a2":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            a2 += 1
                            if a2 > 2:
                                a2 = 1

                            pos = liste_direction[a2]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configa2 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configa2 = "hautbas bashaut"

                        elif coo == "c3":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            c3 += 1
                            if c3 > 2:
                                c3 = 1

                            pos = liste_direction[c3]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc3 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc3 = "hautbas bashaut"

                        elif coo == "c4":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            c4 += 1
                            if c4 > 2:
                                c4 = 1

                            pos = liste_direction[c4]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc4 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc4 = "hautbas bashaut"

                        elif coo == "f4":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            f4 += 1
                            if f4 > 2:
                                f4 = 1

                            pos = liste_direction[f4]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf4 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf4 = "hautbas bashaut"
                                
                        elif coo == "g5":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            g5 += 1
                            if g5 > 2:
                                g5 = 1

                            pos = liste_direction[g5]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg5 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg5 = "hautbas bashaut"

                        elif coo == "c2":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            c2 += 1
                            if c2 > 2:
                                c2 = 1

                            pos = liste_direction[c2]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(virages1_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc2 = "hautdroite droitehaut basgauche gauchebas"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(virages2_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc2 = "hautgauche gauchehaut basdroite droitebas"

                        elif coo == "b3":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            b3 += 1
                            if b3 > 2:
                                b3 = 1

                            pos = liste_direction[b3]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(virages1_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb3 = "hautdroite droitehaut basgauche gauchebas"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(virages2_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb3 = "hautgauche gauchehaut basdroite droitebas"

                        elif coo == "e4":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            e4 += 1
                            if e4 > 2:
                                e4 = 1

                            pos = liste_direction[e4]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(virages1_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                confige4 = "hautdroite droitehaut basgauche gauchebas"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(virages2_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                confige4 = "hautgauche gauchehaut basdroite droitebas"

                        elif coo == "a1":
                            departanim(pos_x, pos_y)
                            numeroord = int(numeroord)
                            numeroord += 1
                            numeroord = str(numeroord)
                            coo = str(liste_lettre[numeroabs]+(numeroord))
                            origine = "haut"
                            pos_y += 120
                            recup = "0"
                            a = "0"
                            remplissage(coo, recup, origine, a, pos_x, pos_y, numeroabs, numeroord, niveau)
                            
                    if event.type == MOUSEBUTTONUP and fini == 1:

                        pos_x = event.pos[0]
                        pos_y = event.pos[1]

                        if pos_y > 500:
                            niveau = niveau + 1
                            continuer_niveau = 0
                            continuer_menu = 0
                            continuer_retourselection = 0
                            continuer_selection = 0
                            continuer_jeu = 1
                            continuer_apropos = 0
                            
                    elif event.type == MOUSEBUTTONUP and fini == 0:

                        pos_x = event.pos[0]
                        pos_y = event.pos[1]

                        if pos_y > 500:
                            jeu_son.play(10)
                            continuer_niveau = 0
                            continuer_menu = 0
                            continuer_retourselection = 0
                            continuer_selection = 0
                            continuer_jeu = 1
                            continuer_apropos = 0

                    if fini == 2:
                        fenetre.blit(noirnoir, (0,0))
                        clics = font.render(coup, True, white)
                        fenetre.blit(clics, (1120-(len(coup)*53)/2,142))
                        pygame.display.flip()
                            
                i = j = 0
                coo = 0
                numeroabs = numeroord = 1

        #Niveau 3
        elif niveau == 4:

            fenetre.blit(fond4, (0,0))
            fenetre.blit(depart,(240,0))
            fenetre.blit(viragedb_vide, (0,120))
            fenetre.blit(croix_vide, (120,120))
            fenetre.blit(virages1_vide, (240,120))
            fenetre.blit(viragedb_vide, (360,120))
            fenetre.blit(horizontal_vide, (480,120))
            fenetre.blit(virages1_vide, (600,120))
            fenetre.blit(horizontal_vide, (0,240))
            fenetre.blit(viragedb_vide, (120,240))
            fenetre.blit(horizontal_vide, (360,240))
            fenetre.blit(croix_vide, (480,240))
            fenetre.blit(horizontal_vide, (600,240))
            fenetre.blit(horizontal_vide, (0,360))
            fenetre.blit(viragedb_vide, (120,360))
            fenetre.blit(horizontal_vide, (240,360))
            fenetre.blit(virages1_vide, (360,360))
            fenetre.blit(croix_vide, (600,360))
            fenetre.blit(viragedb_vide, (720,360))
            fenetre.blit(viragedb_vide, (0,480))
            fenetre.blit(viragedb_vide, (120,480))
            fenetre.blit(croix_vide, (360,480))
            fenetre.blit(viragedb_vide, (600,480))
            fenetre.blit(virages1_vide, (720,480))
            fenetre.blit(viragedb_vide, (0,600))
            fenetre.blit(horizontal_vide, (120,600))
            fenetre.blit(horizontal_vide, (240,600))
            fenetre.blit(viragedb_vide, (360,600))
            fenetre.blit(vertical_vide, (720,600))
            fenetre.blit(arrivee, (720,600))
            fenetre.blit(quadri, (0,0))

            tuyaua2 = tuyaub3 = tuyaua5 = tuyaub5 = tuyaua6 = tuyaud6 = tuyaud2 = tuyauf5 = tuyaug4 = tuyaub4 = liste_tuyau[0]
            configa2 = configb3 = configa5 = configb5 = configd6 = configa6 = configd2 = configf5 = configg4 = configb4 = "droitebas basdroite"
            tuyaua3 = tuyaua4 = tuyaub6 = tuyauc4 = tuyauc6 = tuyaud3 = tuyaue2 = tuyauf3 = liste_tuyau[1]
            configa3 = configa4 = configb6 = configc4 = configc6 = configd3 = confige2 = configf3 = "gauchedroite droitegauche"  
            tuyaub2 = tuyaud5 = tuyaue3 = tuyauf4 = liste_tuyau[2]
            configb2 = configd5 = confige3 = configf4 = "hautbas bashaut gauchedroite droitegauche"
            tuyauc2 = tuyaud4 = tuyauf2 = tuyaug5 = liste_tuyau[3]
            configc2 = configd4 = configf2 = configg5 = "hautdroite droitehaut basgauche gauchebas"
            configg6 = "hautbas bashaut"
            configa7 = configb7 = configc7 = configd7 = confige7 = configf7 = configg7 = configh7 = configa0 = configb0 = configc0 = configd0 = confige0 = configf0 = configg0 = configh0 = configd1 = configa1 = configb1 = confige1 = configf1 = configg1 = configh1 = configg2 = configh2 = configg3 = configh3 = configc3 = confige4 = configh4 = configc5 = confige5 = configh5 = confige6 = configf6 = configg6 = configz1 = configz2 = configz3 = configz4 = configz5 = configz6 = liste_tuyau[6]

            fini = 2
            c1 = 1
            a2 = b2 = c2 = d2 = e2 = f2 = 1
            a3 = b3 = d3 = e3 = f3 = 1
            a4 = b4 = c4 = d4 = f4 = g4 = 1
            a5 = b5 = d5 = f5 = g5 = 1
            a6 = b6 = c6 = d6 = g6 = 1
            
            i = j = 0
            numeroabs = 1
            numeroord = 1
            coup = 0
            coup = str(coup)
            clics = font.render(coup, True, white)
            fenetre.blit(clics, (1120-(len(coup)*53)/2,142))
            pygame.display.flip()

            while continuer_niveau:
                for event in pygame.event.get():

                    if event.type == QUIT:
                        continuer = 0
                        pygame.quit()

                    elif event.type == MOUSEBUTTONUP and fini == 2:

                        pos_x = event.pos[0]
                        pos_y = event.pos[1]

                        if pos_x > 970 and pos_x < 1270:

                            if pos_y > 360 and pos_y < 500:
                                menu_musique = 1
                                jeu_son.stop()
                                menu_son.play(10)
                                continuer_niveau = 0
                                continuer_jeu = 0
                                continuer_menu = 1
                                continuer_retourselection = 1

                            elif pos_y > 520 and pos_y <680:
                                continuer_niveau = 0
                                continuer_jeu = 0
                                continuer_retourselection = 0

                        while i < 960:

                            if pos_x > i+120:
                                i += 120
                                numeroabs += 1

                            else:
                                pos_x = i
                                i = 960

                        while j < 720:

                            if pos_y > j+120:
                                j += 120
                                numeroord += 1

                            else:
                                pos_y = j
                                j = 720

                        numeroord = str(numeroord)
                        coo = str(liste_lettre[numeroabs]+numeroord)

                        if coo == "a2":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            a2 += 1
                            if a2 > 4:
                                a2 = 1

                            pos = liste_direction[a2]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configa2 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configa2 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configa2 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configa2 = "droitehaut hautdroite"

                        elif coo == "d2":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            d2 += 1
                            if d2 > 4:
                                d2 = 1

                            pos = liste_direction[d2]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd2 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd2 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd2 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd2 = "droitehaut hautdroite"

                        elif coo == "b3":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            b3 += 1
                            if b3 > 4:
                                b3 = 1

                            pos = liste_direction[b3]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb3 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb3 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb3 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb3 = "droitehaut hautdroite"

                        elif coo == "b4":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            b4 += 1
                            if b4 > 4:
                                b4 = 1

                            pos = liste_direction[b4]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb4 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb4 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb4 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb4 = "droitehaut hautdroite"

                        elif coo == "g4":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            g4 += 1
                            if g4 > 4:
                                g4 = 1

                            pos = liste_direction[g4]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg4 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg4 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg4 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg4 = "droitehaut hautdroite"

                        elif coo == "a5":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            a5 += 1
                            if a5 > 4:
                                a5 = 1

                            pos = liste_direction[a5]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configa5 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configa5 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configa5 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configa5 = "droitehaut hautdroite"

                        elif coo == "b5":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            b5 += 1
                            if b5 > 4:
                                b5 = 1

                            pos = liste_direction[b5]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb5 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb5 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb5 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb5 = "droitehaut hautdroite"

                        elif coo == "f5":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            f5 += 1
                            if f5 > 4:
                                f5 = 1

                            pos = liste_direction[f5]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf5 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf5 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf5 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf5 = "droitehaut hautdroite"

                        elif coo == "a6":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            a6 += 1
                            if a6 > 4:
                                a6 = 1

                            pos = liste_direction[a6]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configa6 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configa6 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configa6 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configa6 = "droitehaut hautdroite"

                        elif coo == "d6":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            d6 += 1
                            if d6 > 4:
                                d6 = 1

                            pos = liste_direction[d6]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd6 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd6 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd6 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd6 = "droitehaut hautdroite"

                        elif coo == "e2":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            e2 += 1
                            if e2 > 2:
                                e2 = 1

                            pos = liste_direction[e2]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                confige2 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                confige2 = "hautbas bashaut"
                                
                        elif coo == "a3":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            a3 += 1
                            if a3 > 2:
                                a3 = 1

                            pos = liste_direction[a3]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configa3 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configa3 = "hautbas bashaut"

                        elif coo == "d3":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            d3 += 1
                            if d3 > 2:
                                d3 = 1

                            pos = liste_direction[d3]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd3 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd3 = "hautbas bashaut"

                        elif coo == "f3":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            f3 += 1
                            if f3 > 2:
                                f3 = 1

                            pos = liste_direction[f3]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf3 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf3 = "hautbas bashaut"

                        elif coo == "a4":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            a4 += 1
                            if a4 > 2:
                                a4 = 1

                            pos = liste_direction[a4]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configa4 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configa4 = "hautbas bashaut"

                        elif coo == "c4":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            c4 += 1
                            if c4 > 2:
                                c4 = 1

                            pos = liste_direction[c4]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc4 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc4 = "hautbas bashaut"

                        elif coo == "b6":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            b6 += 1
                            if b6 > 2:
                                b6 = 1

                            pos = liste_direction[b6]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb6 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb6 = "hautbas bashaut"

                        elif coo == "c6":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            c6 += 1
                            if c6 > 2:
                                c6 = 1

                            pos = liste_direction[c6]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc6 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc6 = "hautbas bashaut"

                        elif coo == "c2":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            c2 += 1
                            if c2 > 2:
                                c2 = 1

                            pos = liste_direction[c2]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(virages1_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc2 = "hautdroite droitehaut basgauche gauchebas"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(virages2_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc2 = "hautgauche gauchehaut basdroite droitebas"


                        elif coo == "f2":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            f2 += 1
                            if f2 > 2:
                                f2 = 1

                            pos = liste_direction[f2]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(virages1_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf2 = "hautdroite droitehaut basgauche gauchebas"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(virages2_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf2 = "hautgauche gauchehaut basdroite droitebas"


                        elif coo == "d4":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            d4 += 1
                            if d4 > 2:
                                d4 = 1

                            pos = liste_direction[d4]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(virages1_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd4 = "hautdroite droitehaut basgauche gauchebas"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(virages2_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd4 = "hautgauche gauchehaut basdroite droitebas"


                        elif coo == "g5":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            g5 += 1
                            if g5 > 2:
                                g5 = 1

                            pos = liste_direction[g5]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(virages1_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg5 = "hautdroite droitehaut basgauche gauchebas"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(virages2_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg5 = "hautgauche gauchehaut basdroite droitebas"


                        elif coo == "c1":
                            departanim(pos_x, pos_y)
                            numeroord = int(numeroord)
                            numeroord += 1
                            numeroord = str(numeroord)
                            coo = str(liste_lettre[numeroabs]+(numeroord))
                            origine = "haut"
                            pos_y += 120
                            recup = "0"
                            a = "0"
                            remplissage(coo, recup, origine, a, pos_x, pos_y, numeroabs, numeroord, niveau)
                            
                    if event.type == MOUSEBUTTONUP and fini == 1:

                        pos_x = event.pos[0]
                        pos_y = event.pos[1]

                        if pos_y > 500:
                            niveau = niveau + 1
                            continuer_niveau = 0
                            continuer_menu = 0
                            continuer_retourselection = 0
                            continuer_selection = 0
                            continuer_jeu = 1
                            continuer_apropos = 0
                            
                    elif event.type == MOUSEBUTTONUP and fini == 0:

                        pos_x = event.pos[0]
                        pos_y = event.pos[1]

                        if pos_y > 500:
                            jeu_son.play(10)
                            continuer_niveau = 0
                            continuer_menu = 0
                            continuer_retourselection = 0
                            continuer_selection = 0
                            continuer_jeu = 1
                            continuer_apropos = 0

                    if fini == 2:
                        fenetre.blit(noirnoir, (0,0))
                        clics = font.render(coup, True, white)
                        fenetre.blit(clics, (1120-(len(coup)*53)/2,142))
                        pygame.display.flip()

                        
                i = j = 0
                coo = 0
                numeroabs = numeroord = 1
                        
        #Niveau 4
        elif niveau == 5:

            fenetre.blit(fond5, (0,0))
            fenetre.blit(depart, (480,0))
            fenetre.blit(viragedb_vide, (600,0))
            fenetre.blit(viragedb_vide, (720,0))
            fenetre.blit(viragedb_vide, (360,120))
            fenetre.blit(virages1_vide, (480,120))
            fenetre.blit(horizontal_vide, (600,120))
            fenetre.blit(viragedb_vide, (720,120))
            fenetre.blit(viragedb_vide, (840,120))
            fenetre.blit(viragedb_vide, (240,240))
            fenetre.blit(croix_vide, (360,240))
            fenetre.blit(horizontal_vide, (480,240))
            fenetre.blit(croix_vide, (600,240))
            fenetre.blit(horizontal_vide, (720,240))
            fenetre.blit(viragedb_vide, (840,240))
            fenetre.blit(virages1_vide, (240,360))
            fenetre.blit(viragedb_vide, (360,360))
            fenetre.blit(viragedb_vide, (600,360))
            fenetre.blit(viragedb_vide, (720,360))
            fenetre.blit(viragedb_vide, (240,480))
            fenetre.blit(horizontal_vide, (360,480))
            fenetre.blit(croix_vide, (480,480))
            fenetre.blit(horizontal_vide, (600,480))
            fenetre.blit(horizontal_vide, (720,480))
            fenetre.blit(horizontal_vide, (600,600))
            fenetre.blit(vertical_vide, (720,600))
            fenetre.blit(arrivee, (720,600))
            fenetre.blit(quadri, (0,0))

            tuyauf1 = tuyaug1 = tuyaud2 = tuyaug2 = tuyauh2 = tuyauc3 = tuyauh3 = tuyaud4 = tuyauf4 = tuyaug4 = tuyaub4 = tuyauc5 = liste_tuyau[0]
            configf1 = configg1 = configd2 = configg2 = configh2 = configc3 = configh3 = configd4 = configf4 = configg4 = configb4 = configc5 = "droitebas basdroite"
            tuyauf2 = tuyaue3 = tuyaug3 = tuyaud5 = tuyauf5 = tuyaug5 = tuyauf6 = liste_tuyau[1]
            configf2 = confige3 = configg3 = configd5 = configf5 = configg5 = configf6 = "gauchedroite droitegauche"  
            tuyaud3 = tuyauf3 = tuyaue5 = liste_tuyau[2]
            configd3 = configf3 = confige5 = "hautbas bashaut gauchedroite droitegauche"
            tuyaue2 = tuyauc4 = liste_tuyau[3]
            confige2 = configc4 = "hautdroite droitehaut basgauche gauchebas"
            configg6 = "hautbas bashaut"
            configa7 = configb7 = configc7 = configd7 = confige7 = configf7 = configg7 = configh7 = configa0 = configb0 = configc0 = configd0 = confige0 = configf0 = configg0 = configh0 = configa1 = configb1 = configc1 = configd1 = configh1 = configa2 = configb2 = configc2 = configa3 = configb3 = configa4 = configb4 = confige4 = configh4 = configa5 = configb5 = configh5 = configa6 = configb6 = configc6 = configd6 = confige6 = configh6 = configz1 = configz2 = configz3 = configz4 = configz5 = configz6 = liste_tuyau[6]

            fini = 2

            e1 = f1 = g1 = 1
            d2 = e2 = f2 = g2 = h2 = 1
            c3 = d3 = e3 = f3 = g3 = h3 = 1
            c4 = d4 = f4 = g4 = 1
            c5 = d5 = e5 = f5 = g5 = 1
            f6 = g6 = 1
            
            i = j = 0
            numeroabs = 1
            numeroord = 1
            coup = 0
            coup = str(coup)
            clics = font.render(coup, True, white)
            fenetre.blit(clics, (1120-(len(coup)*53)/2,142))
            pygame.display.flip()

            while continuer_niveau:
                for event in pygame.event.get():

                    if event.type == QUIT:
                        continuer = 0
                        pygame.quit()

                    elif event.type == MOUSEBUTTONUP and fini == 2:

                        pos_x = event.pos[0]
                        pos_y = event.pos[1]

                        if pos_x > 970 and pos_x < 1270:

                            if pos_y > 360 and pos_y < 500:
                                menu_musique = 1
                                jeu_son.stop()
                                menu_son.play(10)
                                continuer_niveau = 0
                                continuer_jeu = 0
                                continuer_menu = 1
                                continuer_retourselection = 1

                            elif pos_y > 520 and pos_y <680:
                                continuer_niveau = 0
                                continuer_jeu = 0
                                continuer_retourselection = 0

                        while i < 960:

                            if pos_x > i+120:
                                i += 120
                                numeroabs += 1

                            else:
                                pos_x = i
                                i = 960

                        while j < 720:

                            if pos_y > j+120:
                                j += 120
                                numeroord += 1

                            else:
                                pos_y = j
                                j = 720

                        numeroord = str(numeroord)
                        coo = str(liste_lettre[numeroabs]+numeroord)

                        if coo == "f1":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            f1 += 1
                            if f1 > 4:
                                f1 = 1

                            pos = liste_direction[f1]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf1 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf1 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf1 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf1 = "droitehaut hautdroite"

                        elif coo == "g1":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            g1 += 1
                            if g1 > 4:
                                g1 = 1

                            pos = liste_direction[g1]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg1 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg1 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg1 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg1 = "droitehaut hautdroite"

                        elif coo == "d2":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            d2 += 1
                            if d2 > 4:
                                d2 = 1

                            pos = liste_direction[d2]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd2 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd2 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd2 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd2 = "droitehaut hautdroite"

                        elif coo == "g2":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            g2 += 1
                            if g2 > 4:
                                g2 = 1

                            pos = liste_direction[g2]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg2 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg2 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg2 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg2 = "droitehaut hautdroite"

                        elif coo == "h2":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            h2 += 1
                            if h2 > 4:
                                h2 = 1

                            pos = liste_direction[h2]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configh2 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configh2 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configh2 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configh2 = "droitehaut hautdroite"

                        elif coo == "c3":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            c3 += 1
                            if c3> 4:
                                c3 = 1

                            pos = liste_direction[c3]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc3 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc3 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc3 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc3 = "droitehaut hautdroite"

                        elif coo == "h3":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            h3 += 1
                            if h3> 4:
                                h3 = 1

                            pos = liste_direction[h3]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configh3 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configh3 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configh3 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configh3 = "droitehaut hautdroite"

                        elif coo == "d4":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            d4 += 1
                            if d4 > 4:
                                d4 = 1

                            pos = liste_direction[d4]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd4 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd4 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd4 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd4 = "droitehaut hautdroite"

                        elif coo == "f4":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            f4 += 1
                            if f4 > 4:
                                f4 = 1

                            pos = liste_direction[f4]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf4 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf4 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf4 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf4 = "droitehaut hautdroite"

                        elif coo == "g4":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            g4 += 1
                            if g4 > 4:
                                g4 = 1

                            pos = liste_direction[g4]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg4 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg4 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg4 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg4 = "droitehaut hautdroite"

                        elif coo == "c5":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            c5 += 1
                            if c5 > 4:
                                c5 = 1

                            pos = liste_direction[c5]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc5 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc5 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc5 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc5 = "droitehaut hautdroite"

                        elif coo == "f2":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            f2 += 1
                            if f2 > 2:
                                f2 = 1

                            pos = liste_direction[f2]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf2 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf2 = "hautbas bashaut"

                        elif coo == "e3":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            e3 += 1
                            if e3 > 2:
                                e3 = 1

                            pos = liste_direction[e3]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                confige3 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                confige3 = "hautbas bashaut"

                        elif coo == "g3":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            g3 += 1
                            if g3 > 2:
                                g3 = 1

                            pos = liste_direction[g3]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg3 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg3 = "hautbas bashaut"

                        elif coo == "d5":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            d5 += 1
                            if d5 > 2:
                                d5 = 1

                            pos = liste_direction[d5]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd5 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd5 = "hautbas bashaut"

                        elif coo == "f5":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            f5 += 1
                            if f5 > 2:
                                f5 = 1

                            pos = liste_direction[f5]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf5 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf5 = "hautbas bashaut"

                        elif coo == "g5":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            g5 += 1
                            if g5 > 2:
                                g5 = 1

                            pos = liste_direction[g5]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg5 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg5 = "hautbas bashaut"


                        elif coo == "f6":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            f6 += 1
                            if f6 > 2:
                                f6 = 1

                            pos = liste_direction[f6]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf6 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf6 = "hautbas bashaut"

                        elif coo == "e2":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            e2 += 1
                            if e2 > 2:
                                e2 = 1

                            pos = liste_direction[e2]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(virages1_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                confige2 = "hautdroite droitehaut basgauche gauchebas"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(virages2_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                confige2 = "hautgauche gauchehaut basdroite droitebas"

                        elif coo == "c4":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            c4 += 1
                            if c4 > 2:
                                c4 = 1

                            pos = liste_direction[c4]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(virages1_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc4 = "hautdroite droitehaut basgauche gauchebas"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(virages2_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc4 = "hautgauche gauchehaut basdroite droitebas"

                        elif coo == "e1":
                            
                            departanim(pos_x, pos_y)
                            numeroord = int(numeroord)
                            numeroord += 1
                            numeroord = str(numeroord)
                            coo = str(liste_lettre[numeroabs]+(numeroord))
                            origine = "haut"
                            pos_y += 120
                            recup = "0"
                            a = "0"
                            remplissage(coo, recup, origine, a, pos_x, pos_y, numeroabs, numeroord, niveau)
                            
                    if event.type == MOUSEBUTTONUP and fini == 1:

                        pos_x = event.pos[0]
                        pos_y = event.pos[1]

                        if pos_y > 500:
                            niveau = niveau + 1
                            continuer_niveau = 0
                            continuer_menu = 0
                            continuer_retourselection = 0
                            continuer_selection = 0
                            continuer_jeu = 1
                            continuer_apropos = 0
                            
                    elif event.type == MOUSEBUTTONUP and fini == 0:

                        pos_x = event.pos[0]
                        pos_y = event.pos[1]

                        if pos_y > 500:
                            jeu_son.play(10)
                            continuer_niveau = 0
                            continuer_menu = 0
                            continuer_retourselection = 0
                            continuer_selection = 0
                            continuer_jeu = 1
                            continuer_apropos = 0

                if fini == 2:   
                    fenetre.blit(noirnoir, (0,0))
                    clics = font.render(coup, True, white)
                    fenetre.blit(clics, (1120-(len(coup)*53)/2,142))
                    pygame.display.flip()
                    
                i = j = 0
                coo = 0
                numeroabs = numeroord = 1

        #Niveau 5
        elif niveau == 6:

            fenetre.blit(fond6, (0,0))
            fenetre.blit(viragedb_vide, (120,0))
            fenetre.blit(horizontal_vide, (240,0))
            fenetre.blit(croix_vide, (360,0))
            fenetre.blit(croix_vide, (480,0))
            fenetre.blit(horizontal_vide, (600,0))
            fenetre.blit(viragedb_vide, (720,0))
            fenetre.blit(depart,(840,0))
            fenetre.blit(virages1_vide, (120,120))
            fenetre.blit(viragedb_vide, (240,120))
            fenetre.blit(virages1_vide, (360,120))
            fenetre.blit(croix_vide, (480,120))
            fenetre.blit(viragedb_vide, (720,120))
            fenetre.blit(virages1_vide, (840,120))
            fenetre.blit(virages1_vide, (0,240))
            fenetre.blit(viragedb_vide, (240,240))
            fenetre.blit(horizontal_vide, (360,240))
            fenetre.blit(horizontal_vide, (480,240))
            fenetre.blit(croix_vide, (600,240))
            fenetre.blit(viragedb_vide, (720,240))
            fenetre.blit(viragedb_vide, (0,360))
            fenetre.blit(horizontal_vide, (120,360))
            fenetre.blit(horizontal_vide, (240,360))
            fenetre.blit(viragedb_vide, (360,360))
            fenetre.blit(viragedb_vide, (480,360))
            fenetre.blit(virages1_vide, (600,360))
            fenetre.blit(croix_vide, (720,360))
            fenetre.blit(horizontal_vide, (0,480))
            fenetre.blit(croix_vide, (360,480))
            fenetre.blit(horizontal_vide, (480,480))
            fenetre.blit(viragedb_vide, (600,480))
            fenetre.blit(viragedb_vide, (720,480))
            fenetre.blit(vertical_vide, (0,600))
            fenetre.blit(arrivee, (0,600))
            fenetre.blit(viragedb_vide, (360,600))
            fenetre.blit(horizontal_vide, (480,600))
            fenetre.blit(viragedb_vide, (600,600))
            fenetre.blit(croix_vide, (720,600))
            fenetre.blit(quadri, (0,0))
            fini = 2
            
            tuyaub1 = tuyaug1 = tuyauc2 = tuyaug2 = tuyauc3 = tuyaug3 = tuyaua4 = tuyaud4 = tuyaue4 = tuyauf5 = tuyaug5 = tuyaud6 = tuyauf6 = liste_tuyau[0]
            configb1 = configg1 = configc2 = configg2 = configc3 = configg3 = configa4 = configd4 = confige4 = configf5 = configg5 = tuyaua6 = configd6 = configf6 = "droitebas basdroite"
            tuyauc1 = tuyauf1 = tuyaud3 = tuyaue3 = tuyaub4 = tuyauc4 = tuyaua5 = tuyaue5 = tuyaue6 = liste_tuyau[1]
            configc1 = configf1 = configd3 = confige3 = configb4 = configc4 = configa5 = confige5 = confige6 = "gauchedroite droitegauche"
            #Croix
            tuyaud1 = tuyaue1 = tuyaue2 = tuyauf3 = tuyaug4 = tuyaud5 = tuyaug6 = liste_tuyau[2]
            configd1 = confige1 = confige2 = configf3 = configg4 = configd5 = configg6 = "hautbas bashaut gauchedroite droitegauche"
            #Doubles Virages
            tuyaub2 = tuyaud2 = tuyauh2 = tuyaua3 = tuyauf4 = liste_tuyau[3]
            configb2 = configd2 = configa3 = configf4 = configh2 = "hautdroite droitehaut basgauche gauchebas"
            
            configa6 = "hautbas bashaut"
                        
            b1 = c1 = d1 = e1 = f1 = g1 = h1 = 1
            b2 = c2 = d2 = e2 = g2 = h2 = 1
            a3 = c3 = d3 = e3 = f3 = g3 = 1
            a4 = b4 = c4 = d4 = e4 = f4 = g4 = 1
            a5 = b5 = d5 = e5 = f5 = g5 = 1
            d6 = e6 = f6 = g6 = 1
            configa7 = configb7 = configc7 = configd7 = confige7 = configf7 = configg7 = configh7 = configa0 = configb0 = configc0 = configd0 = confige0 = configf0 = configg0 = configh0 = configa1 = configa2 = configb3 = configb5 = configb6 = configc5 = configc6 = configf2 = configh3 = configh4 = configh5 = configh6 = configz1 = configz2 = configz3 = configz4 = configz5 = configz6 = liste_tuyau[6]
            
            i = j = 0
            origine = 0
            origine = str(origine)
            numeroabs = 1
            numeroord = 1
            coup = 0
            coup = str(coup)
            clics = font.render(coup, True, white)
            fenetre.blit(clics, (1120-(len(coup)*53)/2,142))
            pygame.display.flip()

            while continuer_niveau:
                for event in pygame.event.get():

                    if event.type == QUIT:
                        continuer = 0
                        pygame.quit()

                    elif event.type == MOUSEBUTTONUP and fini == 2:

                        pos_x = event.pos[0]
                        pos_y = event.pos[1]

                        if pos_x > 970 and pos_x < 1270:

                            if pos_y > 360 and pos_y < 500:
                                menu_musique = 1
                                jeu_son.stop()
                                menu_son.play(10)    
                                continuer_niveau = 0
                                continuer_jeu = 0
                                continuer_menu = 1
                                continuer_retourselection = 1

                            elif pos_y > 520 and pos_y <680:
                                continuer_niveau = 0
                                continuer_jeu = 0
                                continuer_retourselection = 0

                        while i < 960:

                            if pos_x > i+120:
                                i += 120
                                numeroabs += 1

                            else:
                                pos_x = i
                                i = 960

                        while j < 720:

                            if pos_y > j+120:
                                j += 120
                                numeroord += 1

                            else:
                                pos_y = j
                                j = 720

                        numeroord = str(numeroord)
                        coo = str(liste_lettre[numeroabs]+numeroord)

                        if coo == "b1":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            b1 += 1
                            if b1 > 4:
                                b1 = 1

                            pos = liste_direction[b1]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb1 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb1 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb1 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb1 = "droitehaut hautdroite"

                        elif coo == "g1":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            g1 += 1
                            if g1 > 4:
                                g1 = 1

                            pos = liste_direction[g1]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg1 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg1 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg1 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg1 = "droitehaut hautdroite"

                        elif coo == "c2":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            c2 += 1
                            if c2 > 4:
                                c2 = 1

                            pos = liste_direction[c2]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc2 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc2 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc2 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc2 = "droitehaut hautdroite"

                        elif coo == "g2":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            g2 += 1
                            if g2 > 4:
                                g2 = 1

                            pos = liste_direction[g2]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg2 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg2 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg2 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg2 = "droitehaut hautdroite"

                        elif coo == "c3":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            c3 += 1
                            if c3 > 4:
                                c3 = 1

                            pos = liste_direction[c3]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc3 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc3 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc3 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc3 = "droitehaut hautdroite"

                        elif coo == "g3":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            g3 += 1
                            if g3 > 4:
                                g3 = 1

                            pos = liste_direction[g3]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg3 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg3 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg3 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg3 = "droitehaut hautdroite"

                        elif coo == "a4":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            a4 += 1
                            if a4 > 4:
                                a4 = 1

                            pos = liste_direction[a4]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configa4 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configa4 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configa4 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configa4 = "droitehaut hautdroite"

                        elif coo == "d4":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            d4 += 1
                            if d4 > 4:
                                d4 = 1

                            pos = liste_direction[d4]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd4 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd4 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd4 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd4 = "droitehaut hautdroite"

                        elif coo == "e4":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            e4 += 1
                            if e4 > 4:
                                e4 = 1

                            pos = liste_direction[e4]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                confige4 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                confige4 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                confige4 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                confige4 = "droitehaut hautdroite"

                        elif coo == "f5":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            f5 += 1
                            if f5 > 4:
                                f5 = 1

                            pos = liste_direction[f5]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf5 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf5 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf5 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf5 = "droitehaut hautdroite"

                        elif coo == "g5":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            g5 += 1
                            if g5 > 4:
                                g5 = 1

                            pos = liste_direction[g5]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg5 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg5 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg5 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configg5 = "droitehaut hautdroite"

                        elif coo == "d6":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            d6 += 1
                            if d6 > 4:
                                d6 = 1

                            pos = liste_direction[d6]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd6 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd6 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd6 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd6 = "droitehaut hautdroite"

                        elif coo == "f6":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            f6 += 1
                            if f6 > 4:
                                f6 = 1

                            pos = liste_direction[f6]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf6 = "droitebas basdroite"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegb_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf6 = "gauchebas basgauche"

                            elif pos == "gauche":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragegh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf6 = "gauchehaut hautgauche"

                            elif pos == "haut":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(viragedh_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf6 = "droitehaut hautdroite"

                        #Vertical horizontal
                        elif coo == "c1":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            c1 += 1
                            if c1 > 2:
                                c1 = 1

                            pos = liste_direction[c1]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc1 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc1 = "hautbas bashaut"


                        elif coo == "f1":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            f1 += 1
                            if f1 > 2:
                                f1 = 1

                            pos = liste_direction[f1]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf1 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf1 = "hautbas bashaut"

                        elif coo == "d3":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            d3 += 1
                            if d3 > 2:
                                d3 = 1

                            pos = liste_direction[d3]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd3 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd3 = "hautbas bashaut"

                        elif coo == "e3":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            e3 += 1
                            if e3 > 2:
                                e3 = 1

                            pos = liste_direction[e3]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                confige3 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                confige3 = "hautbas bashaut"

                        elif coo == "b4":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            b4 += 1
                            if b4 > 2:
                                b4 = 1

                            pos = liste_direction[b4]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb4 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb4 = "hautbas bashaut"

                        elif coo == "c4":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            c4 += 1
                            if c4 > 2:
                                c4 = 1

                            pos = liste_direction[c4]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc4 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configc4 = "hautbas bashaut"

                        elif coo == "a5":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            a5 += 1
                            if a5 > 2:
                                a5 = 1

                            pos = liste_direction[a5]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configa5 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configa5 = "hautbas bashaut"

                        elif coo == "e5":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            e5 += 1
                            if e5 > 2:
                                e5 = 1

                            pos = liste_direction[e5]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                confige5 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                confige5 = "hautbas bashaut"

                        elif coo == "e6":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            e6 += 1
                            if e6 > 2:
                                e6 = 1

                            pos = liste_direction[e6]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(horizontal_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                confige6 = "gauchedroite droitegauche"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(vertical_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                confige6 = "hautbas bashaut"

                        #Doubles virages
                        elif coo == "b2":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            b2 += 1
                            if b2 > 2:
                                b2 = 1

                            pos = liste_direction[b2]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(virages1_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb2 = "hautdroite droitehaut basgauche gauchebas"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(virages2_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configb2 = "hautgauche gauchehaut basdroite droitebas"

                        elif coo == "d2":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            d2 += 1
                            if d2 > 2:
                                d2 = 1

                            pos = liste_direction[d2]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(virages1_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd2 = "hautdroite droitehaut basgauche gauchebas"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(virages2_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configd2 = "hautgauche gauchehaut basdroite droitebas"


                        elif coo == "h2":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            h2 += 1
                            if h2 > 2:
                                h2 = 1

                            pos = liste_direction[h2]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(virages1_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configh2 = "hautdroite droitehaut basgauche gauchebas"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(virages2_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configh2 = "hautgauche gauchehaut basdroite droitebas"


                        elif coo == "a3":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            a3 += 1
                            if a3 > 2:
                                a3 = 1

                            pos = liste_direction[a3]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(virages1_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configa3 = "hautdroite droitehaut basgauche gauchebas"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(virages2_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configa3 = "hautgauche gauchehaut basdroite droitebas"


                        elif coo == "f4":
                            coup = int(coup)
                            coup += 1
                            coup = str(coup)
                            f4 += 1
                            if f4 > 2:
                                f4 = 1

                            pos = liste_direction[f4]

                            if pos == "droite":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(virages1_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf4 = "hautdroite droitehaut basgauche gauchebas"

                            elif pos == "bas":

                                fenetre.blit(fondfond, (pos_x, pos_y))
                                fenetre.blit(virages2_vide, (pos_x, pos_y))
                                fenetre.blit(quadri, (0,0))
                                pygame.display.flip()
                                configf4 = "hautgauche gauchehaut basdroite droitebas"

                        elif coo == "h1":
                            
                            departanim(pos_x, pos_y)
                            numeroord = int(numeroord)
                            numeroord += 1
                            numeroord = str(numeroord)
                            coo = str(liste_lettre[numeroabs]+(numeroord))
                            origine = "haut"
                            pos_y += 120
                            recup = "0"
                            a = "0"
                            remplissage(coo, recup, origine, a, pos_x, pos_y, numeroabs, numeroord, niveau)
                            
                    if event.type == MOUSEBUTTONUP and fini == 1:

                        pos_x = event.pos[0]
                        pos_y = event.pos[1]

                        if pos_y > 500:
                            menu_musique = 1
                            jeu_son.stop()
                            menu_son.play(10)
                            continuer_niveau = 0
                            continuer_menu = 1
                            continuer_retourselection = 1
                            continuer_selection = 0
                            continuer_jeu = 0
                            continuer_apropos = 0
                    
                    elif event.type == MOUSEBUTTONUP and fini == 0:

                        pos_x = event.pos[0]
                        pos_y = event.pos[1]

                        if pos_y > 500:
                            jeu_son.play(10)
                            continuer_niveau = 0
                            continuer_menu = 0
                            continuer_retourselection = 0
                            continuer_selection = 0
                            continuer_jeu = 1
                            continuer_apropos = 0
                            
                if fini == 2:   
                    fenetre.blit(noirnoir, (0,0))
                    clics = font.render(coup, True, white)
                    fenetre.blit(clics, (1120-(len(coup)*53)/2,142))
                    pygame.display.flip()
                    
                i = j = 0
                coo = 0
                numeroabs = numeroord = 1
