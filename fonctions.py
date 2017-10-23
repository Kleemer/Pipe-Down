import pygame
from pygame.locals import *
from constantes import *


#Depart
def departanim (x,y):
    ouverture_son.play()
    for a in range (21):
        fenetre.blit(fondfond, (x,y))
        fenetre.blit(depart_anim[a], (x,y))
        fenetre.blit(quadri, (0,0))
        pygame.display.flip()
        
        a = a + 1

#Croix
def croixdroitegauche (x,y):
    for a in range (11):
        fenetre.blit(croixdg[a], (x,y))
        fenetre.blit(quadri, (0,0))
        pygame.display.flip()
        
        a = a + 1
        g = 1
        b = d = h = 0

def croixgauchedroite (x,y):
    for a in range (11):
        fenetre.blit(croixgd[a], (x,y))
        fenetre.blit(quadri, (0,0))
        pygame.display.flip()
        
        a = a + 1

def croixhautbas (x,y):
    for a in range (11):
        fenetre.blit(croixhb[a], (x,y))
        fenetre.blit(quadri, (0,0))
        pygame.display.flip()
        
        a=a+1

def croixbashaut (x,y):
    for a in range (11):
        fenetre.blit(croixbh[a], (x,y))
        fenetre.blit(quadri, (0,0))
        pygame.display.flip()
        
        a=a+1

#Virages simples
def viragedroitebas (x,y):
    for a in range (11):
        fenetre.blit(viragedb[a], (x,y))
        fenetre.blit(quadri, (0,0))
        pygame.display.flip()
        
        a=a+1
        
def viragebasdroite (x,y):
    for a in range (11):
        fenetre.blit(viragebd[a], (x,y))
        fenetre.blit(quadri, (0,0))
        pygame.display.flip()
        
        a=a+1

def viragegauchebas (x,y):
    for a in range (11):
        fenetre.blit(viragegb[a], (x,y))
        fenetre.blit(quadri, (0,0))
        pygame.display.flip()
        
        a=a+1

def viragebasgauche (x,y):
    for a in range (11):
        fenetre.blit(viragebg[a], (x,y))
        fenetre.blit(quadri, (0,0))
        pygame.display.flip()
        
        a=a+1

def viragegauchehaut (x,y):
    for a in range (11):
        fenetre.blit(viragegh[a], (x,y))
        fenetre.blit(quadri, (0,0))
        pygame.display.flip()
        
        a=a+1

def viragehautgauche (x,y):
    for a in range (11):
        fenetre.blit(viragehg[a], (x,y))
        fenetre.blit(quadri, (0,0))
        pygame.display.flip()
        
        a=a+1

def viragedroitehaut (x,y):
    for a in range (11):
        fenetre.blit(viragedh[a], (x,y))
        fenetre.blit(quadri, (0,0))
        pygame.display.flip()
        
        a=a+1

def viragehautdroite (x,y):
    for a in range (11):
        fenetre.blit(viragehd[a], (x,y))
        fenetre.blit(quadri, (0,0))
        pygame.display.flip()
        
        a=a+1

#Droits
def traitbashaut (x,y):
    for a in range (11):
        fenetre.blit(droitvbh[a], (x,y))
        fenetre.blit(quadri, (0,0))
        pygame.display.flip()
        
        a=a+1

def traithautbas (x,y):
    for a in range (11):
        fenetre.blit(droitvhb[a], (x,y))
        fenetre.blit(quadri, (0,0))
        pygame.display.flip()
        
        a=a+1

def traitdroitegauche (x,y):
    for a in range (11):
        fenetre.blit(droithdg[a], (x,y))
        fenetre.blit(quadri, (0,0))
        pygame.display.flip()
        
        a=a+1

def traitgauchedroite (x,y):
    for a in range (11):
        fenetre.blit(droithgd[a], (x,y))
        fenetre.blit(quadri, (0,0))
        pygame.display.flip()
        
        a=a+1

#Virages doubles
def viragesbasgauche (x,y):
    for a in range (11):
        fenetre.blit(virages1vbg[a], (x,y))
        fenetre.blit(quadri, (0,0))
        pygame.display.flip()
        
        a=a+1

def viragesdroitehaut (x,y):
    for a in range (11):
        fenetre.blit(viragesdh[a], (x,y))
        fenetre.blit(quadri, (0,0))
        pygame.display.flip()
        
        a=a+1

def viragesgauchebas (x,y):
    for a in range (11):
        fenetre.blit(virages1vgb[a], (x,y))
        fenetre.blit(quadri, (0,0))
        pygame.display.flip()
        
        a=a+1

def virageshautdroite (x,y):
    for a in range (11):
        fenetre.blit(virages1vhd[a], (x,y))
        fenetre.blit(quadri, (0,0))
        pygame.display.flip()
        
        a=a+1

def viragesbasdroite (x,y):
    for a in range (11):
        fenetre.blit(virages2vbd[a], (x,y))
        fenetre.blit(quadri, (0,0))
        pygame.display.flip()
        
        a=a+1

def viragesdroitebas (x,y):
    for a in range (11):
        fenetre.blit(virages2vdb[a], (x,y))
        fenetre.blit(quadri, (0,0))
        pygame.display.flip()
        
        a=a+1

def viragesgauchehaut (x,y):
    for a in range (11):
        fenetre.blit(virages2vgh[a], (x,y))
        fenetre.blit(quadri, (0,0))
        pygame.display.flip()
        
        a=a+1

def virageshautgauche (x,y):
    for a in range (11):
        fenetre.blit(virages2vhg[a], (x,y))
        fenetre.blit(quadri, (0,0))
        pygame.display.flip()
        
        a=a+1

def finish (x,y, niveau):
    for a in range (11):
        fenetre.blit(finishlist[a], (x,y))
        fenetre.blit(arrivee, (x,y))
        fenetre.blit(quadri, (0,0))
        pygame.display.flip()
        
        a=a+1
    if niveau == 1:
        pygame.time.delay(300)
        fenetre.blit(bravotuto, (0,0))
        pygame.display.flip()
    elif niveau == 6:
        pygame.time.delay(300)
        fenetre.blit(bravo5, (0,0))
        pygame.display.flip()
    else:
        pygame.time.delay(300)
        fenetre.blit(bravo,(0,0))
        pygame.display.flip()


def etoile (niveau, coup):
    coup = int (coup)

    #NIVEAU 1
    if niveau == 2:
        if coup < 19:
            niveau1_3etoile = 1
            pygame.time.delay(100)
            fenetre.blit(star1, (443,330))
            star1_son.play()
            pygame.display.flip()
            pygame.time.delay(400)
            fenetre.blit(star2, (443,330))
            star2_son.play()
            pygame.display.flip()
            pygame.time.delay(400)
            fenetre.blit(star3, (443,330))
            star3_son.play()
            pygame.display.flip()
            pygame.time.delay(400)
            win_son.play()
            pygame.time.delay(200)
        
        elif coup > 18 and coup < 26:
            niveau1_2etoile = 1
            pygame.time.delay(100)
            fenetre.blit(star1, (443,330))
            star1_son.play()
            pygame.display.flip()
            pygame.time.delay(400)
            fenetre.blit(star2, (443,330))
            star2_son.play()
            pygame.display.flip()
            pygame.time.delay(200)
        
        else:
            niveau1_1etoile = 1
            pygame.time.delay(100)
            fenetre.blit(star1, (443,330))
            star1_son.play()
            pygame.display.flip()
            pygame.time.delay(200)

    #NIVEAU 2
    if niveau == 3:
        if coup < 24:
            pygame.time.delay(100)
            fenetre.blit(star1, (443,330))
            star1_son.play()
            pygame.display.flip()
            pygame.time.delay(400)
            fenetre.blit(star2, (443,330))
            star2_son.play()
            pygame.display.flip()
            pygame.time.delay(400)
            fenetre.blit(star3, (443,330))
            star3_son.play()
            pygame.display.flip()
            pygame.time.delay(400)
            win_son.play()
            pygame.time.delay(200)
            
        elif coup > 23 and coup < 34:
            pygame.time.delay(100)
            fenetre.blit(star1, (443,330))
            star1_son.play()
            pygame.display.flip()
            pygame.time.delay(400)
            fenetre.blit(star2, (443,330))
            star2_son.play()
            pygame.display.flip()
            pygame.time.delay(200)
            
        else:
            pygame.time.delay(100)
            fenetre.blit(star1, (443,330))
            star1_son.play()
            pygame.display.flip()
            pygame.time.delay(200)

    #NIVEAU 3
    if niveau == 4:
        if coup < 25:
            pygame.time.delay(100)
            fenetre.blit(star1, (443,330))
            star1_son.play()
            pygame.display.flip()
            pygame.time.delay(400)
            fenetre.blit(star2, (443,330))
            star2_son.play()
            pygame.display.flip()
            pygame.time.delay(400)
            fenetre.blit(star3, (443,330))
            star3_son.play()
            pygame.display.flip()
            pygame.time.delay(400)
            win_son.play()
            pygame.time.delay(200)
            
        elif coup > 24 and coup < 36:
            pygame.time.delay(100)
            fenetre.blit(star1, (443,330))
            star1_son.play()
            pygame.display.flip()
            pygame.time.delay(400)
            fenetre.blit(star2, (443,330))
            star2_son.play()
            pygame.display.flip()
            pygame.time.delay(200)
            
        else:
            pygame.time.delay(100)
            fenetre.blit(star1, (443,330))
            star1_son.play()
            pygame.display.flip()
            pygame.time.delay(200)

    #NIVEAU 4
    if niveau == 5:
        if coup < 25:
            pygame.time.delay(100)
            fenetre.blit(star1, (443,330))
            star1_son.play()
            pygame.display.flip()
            pygame.time.delay(400)
            fenetre.blit(star2, (443,330))
            star2_son.play()
            pygame.display.flip()
            pygame.time.delay(400)
            fenetre.blit(star3, (443,330))
            star3_son.play()
            pygame.display.flip()
            pygame.time.delay(400)
            win_son.play()
            pygame.time.delay(200)
            
        elif coup > 24 and coup < 36:
            pygame.time.delay(100)
            fenetre.blit(star1, (443,330))
            star1_son.play()
            pygame.display.flip()
            pygame.time.delay(400)
            fenetre.blit(star2, (443,330))
            star2_son.play()
            pygame.display.flip()
            pygame.time.delay(200)
            
        else:
            pygame.time.delay(100)
            fenetre.blit(star1, (443,330))
            star1_son.play()
            pygame.display.flip()
            pygame.time.delay(200)

    #NIVEAU 5
    if niveau == 6:
        if coup < 35:
            pygame.time.delay(100)
            fenetre.blit(star1, (443,330))
            star1_son.play()
            pygame.display.flip()
            pygame.time.delay(400)
            fenetre.blit(star2, (443,330))
            star2_son.play()
            pygame.display.flip()
            pygame.time.delay(400)
            fenetre.blit(star3, (443,330))
            star3_son.play()
            pygame.display.flip()
            pygame.time.delay(400)
            win_son.play()
            pygame.time.delay(200)
            
        elif coup > 34 and coup < 47:
            pygame.time.delay(100)
            fenetre.blit(star1, (443,330))
            star1_son.play()
            pygame.display.flip()
            pygame.time.delay(400)
            fenetre.blit(star2, (443,330))
            star2_son.play()
            pygame.display.flip()
            pygame.time.delay(200)
            
        else:
            pygame.time.delay(100)
            fenetre.blit(star1, (443,330))
            star1_son.play()
            pygame.display.flip()
            pygame.time.delay(200)
