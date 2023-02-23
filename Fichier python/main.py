# Fichier Principal, gère minimax et permet de lancer le jeu.  224 lignes (avec beaucoup de saut de ligne) pour 4700 caractères

from Class_grille import *
from Class_jeu import *

import pygame
from pygame.locals import *
import sys
from random import randint

def coup_ordi(Liste_cases,info_jeu,profondeur):
    '''Cette fonction prend en paramètre
    - Liste_cases qui contient les informations de chaques cases du jeu
    - info_jeu : Un Object de la class Grille
    - profondeur : int positif qui indique la profondeur maximal utilisé pour minimax

    Cette fonction renvoie un coup possible calculer à l'aide de la fonction minimax
    '''

    meilleur_score = -1000
    meilleur_coup = "nothing"
    ordi = 1
    L_coup = []

     # On parcourt toutes les cases du jeu
    for i in range(0,9):

        # Si une des cases est vide
        if Liste_cases[i] == 0:

            # On change ça valeur temporairement et on lance la fonction minimax qui va nous renvoyer un score indiquant si le coup est interessant ou non
            Liste_cases[i] = ordi
            score = minimax(Liste_cases,profondeur,False,info_jeu)
            Liste_cases[i] = 0

            #On ajoute chaque coup interessant à une liste
            if score > meilleur_score:
                meilleur_score = score
                L_coup = [i]
            if score == meilleur_score:
                L_coup.append(i)

    # On renvoie un des meilleurs coups interessant à jouer de manière aléatoire pour éviter que le bot joue systèmatiquement les mêmes coups
    return L_coup[randint(0,len(L_coup)-1)]

def minimax(Liste_cases,profondeur,tour_ordi,info_jeu):
    '''Cette fonction prend en paramètre
    - Liste_cases qui contient les informations de chaques cases du jeu
    - profondeur : int positif qui indique la profondeur maximal utilisé pour minimax
    - tour_ordi : boolean qui indique à l'algorithme si c'est au tour de l'IA ou du joueur de Jouer
    - info_jeu : Un Object de la class Grille

    Cette fonction fait une simulation de tous les coups jouable possible selon une profondeur définie et renvoie un score(int) qui indique si le coup est interessant à jouer ou non.

    Cette fonction et récursive et utilise le principe de l’algorithme MiniMax.
    '''


    ordi = 1 # numéro de joueur de l'IA
    victoire = info_jeu.info_victoire(Liste_cases)

    # On attributs les points en cas de victoire ou d'égalité
    if victoire[0] == True:

        if victoire[1] == 1:
            return 100
        else:
            return -100

    if info_jeu.partie_nulle(Liste_cases,victoire) == True:
        return 0

    if profondeur == 1:
        return 0

    L_coup = []

    # On joue pour l'ordi
    if tour_ordi:

        meilleur_score = -1000

        for i in range(0,9):
            if Liste_cases[i] == 0:
                Liste_cases[i] = ordi
                score = minimax(Liste_cases,profondeur-1,False,info_jeu)
                Liste_cases[i] = 0

                #On ajoute chaque coup interessant à une liste
                if score > meilleur_score:
                    meilleur_score = score
                    L_coup = [i]
                if score == meilleur_score:
                    L_coup.append(i)

        return L_coup[randint(0,len(L_coup)-1)]

    # On joue pour le joueur adverse
    else:

        meilleur_score = 1000

        for i in range(0,9):
            if Liste_cases[i] == 0:
                Liste_cases[i] = 2
                score = minimax(Liste_cases,profondeur-1,False,info_jeu)
                Liste_cases[i] = 0

                if score < meilleur_score:
                    meilleur_score = score
                    L_coup = [i]
                if score == meilleur_score:
                    L_coup.append(i)

        # On renvoie un des meilleurs coups interessant à jouer de manière aléatoire pour éviter que le bot joue systèmatiquement les mêmes coups
        return L_coup[randint(0,len(L_coup)-1)]

def facile(Liste_cases):
    '''Cette fonction prend en paramètre
    - Liste_cases qui contient les informations de chaques cases du jeu

    Cette fonction renvoie un coup possible de manière aléatoire
    '''
    L_coup_possible = []

    for i in range(0,9):

        #On vérifie si la case est libre
        if Liste_cases[i] == 0:
            L_coup_possible.append(i)

    return L_coup_possible[randint(0,len(L_coup_possible)-1)]


def jouer():
    '''Lance le Jeu de Morpion'''
    pygame.init()

    #Crée la fenetre taille 600 de large(x 0 à 600) et 600 de hauteur(y 0 à 600)
    fenetre = pygame.display.set_mode((600,650))
    pygame.display.set_caption("Morpion Version Graphique")

    pygame.display.flip()

    affichage = Grille() # Créer un Object Grille
    info_jeu = Jeu()  # Créer un Objet Jeu

    difficulter = affichage.menu(fenetre,2)

    # difficulter = 0 signifie qu'il n'y a pas de bot et donc que 2 joueurs s'affronte

    nom_joueurs = affichage.pseudo(fenetre,difficulter)

    while True: # La boucle s'arretera au return de la fonction

        affichage.creer_grille(fenetre)

        tour = randint(0,1)

        affichage.tour_joueur(fenetre,nom_joueurs,tour)

        partie_fini = False

        # tant que la parti n'est pas fini
        while partie_fini == False:

            # Si tour du Joueur 1
            if tour == 0:
                pos = info_jeu.coup_jouer(affichage)
                affichage.cercle(fenetre,pos)
                tour=1

            else:
                # Si 2 joueurs fait jouer le joueur 2
                if difficulter ==  0:
                    pos = info_jeu.coup_jouer(affichage)

                # Si un seul joueur, On fait jouer l'IA avec la difficulter choisit
                if difficulter ==1: # aléatoire
                    pos = facile(affichage.cases)

                if difficulter == 2: #minimax(prof=2)
                    pos = coup_ordi(affichage.cases,info_jeu,2)

                if difficulter == 3: #minimax(prof=4)
                    pos = coup_ordi(affichage.cases,info_jeu,4)

                affichage.croix(fenetre,pos)
                tour=0

            affichage.tour_joueur(fenetre,nom_joueurs,tour)

            victoire = info_jeu.info_victoire(affichage.cases)
            egaliter = info_jeu.partie_nulle(affichage.cases,victoire)

            # Si victoire ou égaliter
            if victoire[0] == True or egaliter == True:
                partie_fini = True

                # On actualise le score
                if victoire[0] == True:

                    affichage.Trait(fenetre,victoire[1],victoire[2],victoire[3])

                    if victoire[1] == 1:
                        info_jeu.score[0] += 1
                    else:
                        info_jeu.score[2] += 1

                else:
                    info_jeu.score[1] += 1

                # On réinitialise la grille
                affichage.cases = [0,0,0,0,0,0,0,0,0]

                # On affiche le menu de fin avec la possibilité de rejouer
                rejoue = affichage.fin_partie(fenetre,info_jeu.score,victoire,nom_joueurs)

                if rejoue == False:
                    return # On sort de la fonction le jeu est fini.







