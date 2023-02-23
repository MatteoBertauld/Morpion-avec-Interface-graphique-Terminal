# Fichier Class Jeu, gère toute ce qui est autres que l'affichage et minimax du projet 177 lignes (avec beaucoup de saut de ligne) pour 3700 caractères
# Ce fichier reprend en grande partie le de corrigé du projet Morpion

import pygame
from pygame.locals import *
import sys
from random import randint


class Jeu:
    
    def __init__(self):
        '''Créer un Objet Jeu avec un attribut score'''

        self.score = [0,0,0] # Score de la partie : [nombre de Victoire (J1), nombre de match nul, nombre de Défaite (J1)]

    
    
    def coup_jouer(self,info_jeu):
        """Cette fonction prend en paramètre
        - info_jeu : Un Object de la class Grille
        Cette fonction renvoie le numéro de la case séléctionner par le Joueur, tel que représenté sur ce schéma
        
        _|_|O       0|1|2
        _|X|_  -->  3|4|5
        _|_|_       6|7|8
        """
        
        Jouer= False
        
        while Jouer == False:
            
            # Recuperer tout les inputs
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                num_case = -1
                
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    
                    num_case = 0
                    
                    pos = pygame.mouse.get_pos()
                        
                    if 200 < pos[0] < 400:
                        num_case +=1
                        
                    elif pos[0] > 400:
                        num_case +=2

                    if 250 < pos[1] < 450:
                        num_case +=3
                    elif pos[1] > 450:
                        num_case +=6
                        
                
                if event.type == pygame.KEYDOWN:  # Si une touche du clavier est appuyer
                    
                    # Renvoie la touche correspondante au pavé numérique
                    if event.key == pygame.K_KP1:
                        num_case = 6
                    if event.key == pygame.K_KP2:
                        num_case = 7
                    if event.key == pygame.K_KP3:
                        num_case = 8
                    if event.key == pygame.K_KP4:
                        num_case = 3
                    if event.key == pygame.K_KP5:
                        num_case = 4
                    if event.key == pygame.K_KP6:
                        num_case = 5
                    if event.key == pygame.K_KP7:
                        num_case = 0
                    if event.key == pygame.K_KP8:
                        num_case = 1
                    if event.key == pygame.K_KP9:
                        num_case = 2
            
                if num_case != -1:
                    if info_jeu.cases[num_case] == 0:
                        
                        return (num_case)
                
                
                        

    def horiz(self,Liste_cases):
        """Cette fonction prend en paramètre
        - Liste_cases qui contient les informations de chaques cases du jeu
        
        Cette fonction détermine si un des deux joueurs à 3 croix ou rond alignés en horizontal. 
        
        Elle retroune un tuple de type (boolean, numéro du Joueur qui gagne int(1 ou 2), numéro de case1 int (0 à 9), numéro de case 2 int (0 à 9))."""

        for i in range(0,3):
            if Liste_cases[i*3] == Liste_cases[i*3+1] == Liste_cases[i*3+2] != 0:
                return (True,Liste_cases[i*3],i*3,i*3+2)
        return (False,None,None,None)

    def vertic(self,Liste_cases):
        """Cette fonction prend en paramètre
        - Liste_cases qui contient les informations de chaques cases du jeu
        
        Cette fonction détermine si un des deux joueurs à 3 croix ou rond alignés en vertical. 
        
        Elle retroune un tuple de type (boolean, numéro du Joueur qui gagne int(1 ou 2), numéro de case1 int (0 à 9), numéro de case 2 int (0 à 9))"""

        for i in range(0,3):
            if Liste_cases[i] == Liste_cases[i+3] == Liste_cases[i+6] != 0:
                return (True,Liste_cases[i],i,i+6)
        return (False,None,None,None)


    def diag(self,Liste_cases):
        """Cette fonction prend en paramètre
        - Liste_cases qui contient les informations de chaques cases du jeu
        
        Cette fonction détermine si un des deux joueurs à 3 croix ou rond alignés en diagonal. 
        
        Elle retroune un tuple de type (boolean, numéro du Joueur qui gagne int(1 ou 2), numéro de case1 int (0 à 9), numéro de case 2 int (0 à 9))
        
        
        """

        if Liste_cases[0] == Liste_cases[4] == Liste_cases[8] != 0:
            return (True,Liste_cases[0],0,8)
            
        if Liste_cases[2] == Liste_cases[4] == Liste_cases[6] != 0:
            return (True,Liste_cases[2],2,6)
            
        return (False,None,None,None)


    def info_victoire(self,Liste_cases):
        """ Cette fonction prend en paramètre
        - Liste_cases qui contient les informations de chaques cases du jeu
        
        Cette fonction utilise les fonction diag, horiz, et vertic et détermine si un des deux joueurs à fini la partie. 
        
        Elle retroune un tuple de type (boolean, numéro du Joueur qui gagne int(1 ou 2), numéro de case1 int (0 à 9), numéro de case 2 int (0 à 9))"""
        
        horizontal = self.horiz(Liste_cases)
        vertical = self.vertic(Liste_cases)
        diagonal = self.diag(Liste_cases)
        
        if horizontal[0] == True:
            return horizontal
            
        if vertical[0] == True:
            return vertical
            
        if diagonal[0] == True:
            return diagonal
            
        return (False,None,None,None)


    def partie_nulle(self,Liste_cases,victoire):
        """Cette fonction prend en paramètre
        - Liste_cases qui contient les informations de chaques cases du jeu
        - victoire : Boolean particulié de type  False ou (True,numéro du Joueur qui gagne int(1 ou 2), numéro de case1 int (0 à 9), numéro de case 2 int (0 à 9))
        
        Cette fonction détermine si la partie est nulle c'est à dire qu'elle est terminé et qu'aucun des joueurs ne gagne. Elle retroune un booléen correspondant """

        if victoire[0] == False:
            
            for valeur in Liste_cases:
                if valeur == 0:
                    return False
            return True
        return False
            
    # Pas de case vide + Pas de victoire : Match nulle