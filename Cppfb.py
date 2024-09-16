# definition de la fonction gagnant
def gagnant(joueur,bot):
    # 1=égalité,2= joueur gagnant et 3= bot gagnant
    window.blit(etoile,(230,108))
    if joueur=="ciseaux":
        if bot=="ciseaux":
            return 1
        elif bot=="pierre":
            window.blit(pierre_bot,(306,205))
            return 3
        elif bot=="feuille":
            window.blit(ciseaux_joueur,(306,205))
            return 2
        elif bot=="puit":
            window.blit(puit_bot,(306,205))
            return 3
        else: #bombe
            window.blit(ciseaux_joueur,(306,205))
            return 2
    elif joueur=="pierre":
        if bot=="ciseaux":
            window.blit(pierre_joueur,(306,205))
            return 2
        elif bot=="pierre":
            return 1
        elif bot=="feuille":
            window.blit(feuille_bot,(306,205))
            return 3
        elif bot=="puit":
            window.blit(puit_bot,(306,205))
            return 3
        else: #bombe
            window.blit(pierre_joueur,(306,205))
            return 2
    elif joueur=="feuille":
        if bot=="ciseaux":
            window.blit(ciseaux_bot,(306,205))
            return 3
        elif bot=="pierre":
            window.blit(feuille_joueur,(306,205))
            return 2
        elif bot=="feuille":
            return 1
        elif bot=="puit":
            window.blit(feuille_joueur,(306,205))
            return 2
        else: #bombe
            window.blit(bombe_bot,(306,205))
            return 3
    elif joueur=="puit":
        if bot=="ciseaux":
            window.blit(puit_joueur,(306,205))
            return 2
        elif bot=="pierre":
            window.blit(puit_joueur,(306,205))
            return 2
        elif bot=="feuille":
            window.blit(feuille_bot,(306,205))
            return 3
        elif bot=="puit":
            return 1
        else: #bombe
            window.blit(bombe_bot,(306,205))
            return 3
    else: #bombe
        if bot=="ciseaux":
            window.blit(ciseaux_bot,(306,205))
            return 3
        elif bot=="pierre":
            window.blit(pierre_bot,(306,205))
            return 3
        elif bot=="feuille":
            window.blit(bombe_joueur,(306,205))
            return 2
        elif bot=="puit":
            window.blit(bombe_joueur,(306,205))
            return 2
        else:#bombe
            return 1

#définition de la fonction choix signe du bot
def signe_bot(partie):
    if partie=="classique":
        bot=signes[random.randint(0,2)]
    else:
        bot=signes[random.randint(0,4)]
    return bot

#féfinition de la fonction choix signe du joueur
def signe_joueur(partie):
    if partie=="classique":
        joueur=0
        while joueur==0:
            clic=waitclic()
            if 478<=clic[1] and 320<=clic[0]<640:
                if clic[0]<=320:
                    joueur="pierre"
                elif clic[0]<=480:
                    joueur="feuille"
                else:
                    joueur="ciseaux"
    else:
        joueur=0
        while joueur==0:
            clic=waitclic()
            if 478<=clic[1]:
                if clic[0]<=160 :
                    joueur="bombe"
                elif clic[0]<=320:
                    joueur="pierre"
                elif clic[0]<=480:
                    joueur="feuille"
                elif clic[0]<=640:
                    joueur="ciseaux"
                else:
                    joueur="puit"
    return joueur

#definition de la fonction score
def score(gagnant):
    global score_bot,score_joueur
    if gagnant==2:
        score_joueur=score_joueur+1
    elif gagnant==3:
        score_bot=score_bot+1
    #affichage du tiret
    screen.blit(tiret,(350,30))
    #affichage du score du bot
    if score_bot==0:
        screen.blit(n0,(300,30))
    elif score_bot==1:
        screen.blit(n1,(300,30))
    elif score_bot==2:
        screen.blit(n2,(300,30))
    elif score_bot==3:
        screen.blit(n3,(300,30))
    elif score_bot==4:
        screen.blit(n4,(300,30))
    else:
        screen.blit(n5,(300,30))
    #affichage du score du joueur
    if score_joueur==0:
        screen.blit(n0,(400,30))
    elif score_joueur==1:
        screen.blit(n1,(400,30))
    elif score_joueur==2:
        screen.blit(n2,(400,30))
    elif score_joueur==3:
        screen.blit(n3,(400,30))
    elif score_joueur==4:
        screen.blit(n4,(400,30))
    else:
        screen.blit(n5,(400,30))

# #définition de la fonction affichage signes
def affichage_signes(joueur,bot):
    window.blit(variante,(0,0))
    pygame.display.flip()
    pygame.time.delay(4)
    window.blit(variante,(0,0))
    gagné=int(gagnant(joueur,bot))
    if joueur=="ciseaux":
        window.blit(ciseaux_joueur,(609,205))
    elif joueur=="pierre":
        window.blit(pierre_joueur,(609,205))
    elif joueur=="feuille":
        window.blit(feuille_joueur,(609,205))
    elif joueur=="puit":
        window.blit(puit_joueur,(609,205))
    else: #bombe
        window.blit(bombe_joueur,(609,205))
    if bot=="ciseaux":
        window.blit(ciseaux_bot,(0,205))
    elif bot=="pierre":
        window.blit(pierre_bot,(0,205))
    elif bot=="feuille":
        window.blit(feuille_bot,(0,205))
    elif bot=="puit":
        window.blit(puit_bot,(0,205))
    else: #bombe
        window.blit(bombe_bot,(0,205))
    score(gagné)
#définition de la fonction waitclic
def waitclic():
    """ attend que l'utilisateur clique, et renvoie les coordonnées du point cliqué. ferme le programme si clic sur croix"""
    continuer = 1
    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit(0)
            if event.type== MOUSEBUTTONDOWN :
                return event.pos


#définition des signes utilisés
signes=["pierre","feuille","ciseaux","puit","bombe"]

#INITIALISATION
import random
import pygame
from pygame.locals import *
pygame.init() # initialisation de pygame
#ouverture de la fenêtre graphique
window = pygame.display.set_mode((800,600))
screen= pygame.display.get_surface()


##importation des images
variante = pygame.image.load("partie_variante.png").convert()
classique = pygame.image.load("partie_classique.png").convert()
ciseaux_bot = pygame.image.load("ciseaux_bot.png").convert_alpha()
ciseaux_joueur = pygame.image.load("ciseaux_joueur.png").convert_alpha()
bombe_bot = pygame.image.load("bombe_bot.png").convert_alpha()
bombe_joueur = pygame.image.load("bombe_joueur.png").convert_alpha()
puit_bot = pygame.image.load("puit_bot.png").convert_alpha()
puit_joueur = pygame.image.load("puit_joueur.png").convert_alpha()
pierre_bot = pygame.image.load("pierre_bot.png").convert_alpha()
pierre_joueur = pygame.image.load("pierre_joueur.png").convert_alpha()
feuille_bot = pygame.image.load("feuille_bot.png").convert_alpha()
feuille_joueur = pygame.image.load("feuille_joueur.png").convert_alpha()
etoile = pygame.image.load("etoile.png").convert_alpha()
cache = pygame.image.load("cache.png").convert()
n0 = pygame.image.load("0.png").convert_alpha()
n1 = pygame.image.load("1.png").convert_alpha()
n2 = pygame.image.load("2.png").convert_alpha()
n3 = pygame.image.load("3.png").convert_alpha()
n4 = pygame.image.load("4.png").convert_alpha()
n5 = pygame.image.load("5.png").convert_alpha()
tiret = pygame.image.load("-.png").convert_alpha()

score_bot=0
score_joueur=0

window.blit(variante,(0,0))
pygame.display.flip()
while (score_bot<5) and (score_joueur<5):
    joueur=signe_joueur("variante")
    bot=signe_bot("variante")
    affichage_signes(joueur,bot)
    pygame.display.flip()

pygame.time.delay(1900)
pygame.quit()