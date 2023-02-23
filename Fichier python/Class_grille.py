# Fichier Class Grille, gère toute la partie affichage du projet 742 lignes (avec beaucoup de saut de ligne) pour 18000 caractères

from Class_jeu import *

import pygame
from pygame.locals import *
import sys



class Grille:


    def __init__(self):
        '''Créer un Objet grille, avec une liste de 9 atttributs qui correspondent aux informations de chaques cases d'un jeu de morpion

        Chaques cases peut avoir 3 états de jeu :  (ici n est un entier entre 1 et 9)
        Soit C[n] = 0 La case est libre, aucun coup n'a encore été jouer sur cette case
        Soit C[n] = 1 Le Joueur 1 à déja jouer sur cette case, un cercle est présente
        Soit C[n] = 2 Le Joueur 2 à déja jouer sur cette case, une croix est présent

        Lors de la création d'un object grille par défault toutes les cases sont libres

        _|_|O       C[0] | C[1] | C[2]
        _|X|_  -->  C[3] | C[4] | C[5]
        _|_|_       C[4] | C[6] | C[8]

        ex C[4] = 1 : Le joueur (J1) a déja jouer sur la case du milieu, une croix est présente
        ex C[2] = 2 : Le joueur (J2) a déja jouer sur la case en haut à droite, un cercle est présent

        '''

        
        self.cases = [0,0,0,0,0,0,0,0,0] # Int (0 ; 1 ; 2)

    def creer_grille(self,fenetre):
        '''Prend un paramètre :
        - fenetre : l'écran sur lequelle on doit afficher des objects
        
        Cette fonction affiche une grille de morpion Vide'''
        
        blanc = (255,255, 255)
        noir = (0,0,0)
        
        fenetre.fill(blanc)
        
        pygame.draw.line(fenetre, (noir), (200,75), (200, 650), 3)
        pygame.draw.line(fenetre, (noir), (400,75), (400, 650), 3)
        pygame.draw.line(fenetre, (noir), (0,250), (600, 250), 3)
        pygame.draw.line(fenetre, (noir), (0,450), (600, 450), 3)
    
        pygame.display.flip()
        
        return
        
        

    def cercle(self,fenetre,pos):
        '''Prend en paramètre :
        - fenetre : l'écran sur lequelle on doit afficher des objects
        - pos : int (0 à 8) qui indique la case sur laquell on doit afficher un cercle
        
        Cette fonction affiche à l'écran un cercle dans la case pos (0 à 8) et met à jour la valeur de l'attributs de cette case'''
        
        bleu = (0,0,255)
        
        self.cases[pos] = 1
        
        #(pos%3)*200+100 renvoie la valeur x du centre de la case
        #(pos//3)*200+150 renvoie la valeur y du centre de la case 
        pygame.draw.circle(fenetre,bleu,[(pos%3)*200+100,(pos//3)*200+150],50,8)
    
        pygame.display.flip()
        
        return
            


    def croix(self,fenetre,pos):
        '''Prend en paramètre :
        - fenetre : l'écran sur lequelle on doit afficher des objects
        - pos : int (0 à 8) qui indique la case sur laquell on doit afficher une croix
        
        Cette fonction affiche à l'écran une croix dans la case pos (0 à 8) et met à jour la valeur de l'attributs de cette case'''


        rouge = (255,0,0)
        
        self.cases[pos] = 2
        
        #pareil que pour les cercles
        pygame.draw.line(fenetre,rouge,[(pos%3)*200+50,(pos//3)*200+100],[(pos%3)*200+150,(pos//3)*200+200],8)
        pygame.draw.line(fenetre,rouge,[(pos%3)*200+50,(pos//3)*200+200],[(pos%3)*200+150,(pos//3)*200+100],8)
    
        pygame.display.flip()
        
        return

        


    def Trait(self,fenetre,gagnant,pos1,pos2):
        '''Prend en paramètre
        - fenetre : l'écran sur lequelle on doit afficher des objects
        - gagnant : int (1 ou 2) qui indique quel joueur à gagné
        - pos1 / pos2 : int (0 à 8) qui indique les deux cases à relier 
        
        
        Cette fonction trace un trait pour montrer qu'un des deux joueurs à 3 croix ou rond alignés'''
        
        bleu = (0,0,255)
        rouge = (255,0,0)
        
        # On met la couleur du trait à la couleur du gagnant
        if gagnant == 1:
            couleur = bleu
        else:
            couleur = rouge
        
        #(pos%3)*200+100 renvoie la valeur x du centre de la case
        #(pos//3)*200+150 renvoie la valeur y du centre de la case 
        # On récupère anisi les coordonné des deux points qu'on relie directement avec une seul ligne
        pygame.draw.line(fenetre,couleur,[(pos1%3)*200+100,(pos1//3)*200+150],[(pos2%3)*200+100,(pos2//3)*200+150],8)

        pygame.display.flip()

        
    def menu_fond(self,fenetre):
        '''Prend en paramètre
        - fenetre : l'écran sur lequelle on doit afficher des objects
        
        Cette fonction est utilisé par la fonction menu elle permet d'afficher tous ce qui ne change pas sur le menu du jeu
        '''
            
        blanc = (255,255, 255)
        noir = (0,0,0)
        
        # on réinitialise l'affichage
        fenetre.fill(blanc)
        
        # Bordure Noir
        pygame.draw.line(fenetre,noir,[0,0],[600,0],15)
        pygame.draw.line(fenetre,noir,[0,0],[0,650],15)
        pygame.draw.line(fenetre,noir,[600,0],[600,650],15)
        pygame.draw.line(fenetre,noir,[0,650],[600,650],15)
        
        #Police
        police_ecr_titre = pygame.font.Font(None, 130)
        police_ecr_sous_titre = pygame.font.Font(None, 60)
        
        #Jouer 1 et Jouer 2
        texte_Jouer = police_ecr_titre.render("Jouer", True, noir)
        fenetre.blit(texte_Jouer, (170, 75))
        fenetre.blit(texte_Jouer, (170, 275))
        
        # Sous titre Jouer 1 (à deux joueurs)
        texte_2joueur = police_ecr_sous_titre.render("à deux Joueurs", True, noir)
        fenetre.blit(texte_2joueur, (140, 165))
        
        # Sous titre Jouer 2 (contre une ia + de difficulté)
        texte_ia = police_ecr_sous_titre.render("Contre une ia", True, noir)
        fenetre.blit(texte_ia, (155, 365))
        texte_niveau = police_ecr_sous_titre.render("de difficulté ", True, noir)
        fenetre.blit(texte_niveau, (165, 400))

    def menu_fleche_gauche(self,fenetre):
        '''Prend en paramètre
        - fenetre : l'écran sur lequelle on doit afficher des objects
        
        Cette fonction est utilisé par la fonction menu elle permet d'afficher une flèche gauche à l'écran
        '''
        
        noir = (0,0,0)
        
        pygame.draw.line(fenetre,noir,[50,495],[130,495],8)
        pygame.draw.line(fenetre,noir,[50,495],[80,465],8)
        pygame.draw.line(fenetre,noir,[50,495],[80,525],8)
        
    def menu_fleche_droit(self,fenetre):
        '''Prend en paramètre
        - fenetre : l'écran sur lequelle on doit afficher des objects
        
        Cette fonction est utilisé par la fonction menu elle permet d'afficher une flèche droite à l'écran
        '''
        
        noir = (0,0,0)
        
        pygame.draw.line(fenetre,noir,[470,495],[550,495],8)
        pygame.draw.line(fenetre,noir,[520,465],[550,495],8)
        pygame.draw.line(fenetre,noir,[520,525],[550,495],8)
        
    def menu_affichage(self,fenetre,difficulter=2,surligner=0):
        '''Prend en paramètre
        - fenetre : l'écran sur lequelle on doit afficher des objects
        -difficulter : int( 1 à 3 ) indique qu'elle est la difficulté de l'ia choisit par le joueur par défault on est en mode modérée
        -surligner int ( 0 à 4 ) indique quelle object on doit afficher avec une barre de surlignage.
        il ne peut il y en avoir qu'un seul object surligner à la fois. 0 indique qu'il n'y a pas d'object surligner
        
        Cette fonction utilise les fonctions menu_fond / menu_fleche_gauche / menu_fleche_droit.
        
        Elle permet d'afficher le menu du jeu avec la possibilité d'interagir à l'aide de la souris et du clavier sur les bouton et donc de lancer le jeu dans le mode et la difficulté souhaiter par le joueur.
        
        '''
        
        noir = (0,0,0)
        self.menu_fond(fenetre)
        
        
        if difficulter ==1:  # ia Facile
            
            police_ecr_titre = pygame.font.Font(None, 85)
            
            texte_Facile = police_ecr_titre.render("Facile", True, noir)
            fenetre.blit(texte_Facile, (210, 470))
            
            self.menu_fleche_droit(fenetre)
            
        
        if difficulter ==2:   # ia modérée
            
            police_ecr_titre = pygame.font.Font(None, 85)
            
            texte_moyen = police_ecr_titre.render("Modéré", True, noir)
            fenetre.blit(texte_moyen, (190, 470))
            
            self.menu_fleche_droit(fenetre)
            self.menu_fleche_gauche(fenetre)
            
        if difficulter ==3:  # ia difficile
            
            police_ecr_titre = pygame.font.Font(None, 85)
            
            texte_difficile = police_ecr_titre.render("Difficile", True, noir)
            fenetre.blit(texte_difficile, (185, 470))
            
            self.menu_fleche_gauche(fenetre)
        
        bleu = (0,0,255)
        
        if surligner == 1: # on surligne Le bouton Jouer 1
            pygame.draw.line(fenetre,bleu,[170,157],[425,157],6)
        
        if surligner == 2: # on surligne Le bouton Jouer 2
            pygame.draw.line(fenetre,bleu,[170,357],[425,357],6)
            
        if surligner == 3: # on surligne la fleche gauche
            pygame.draw.line(fenetre,bleu,[55,532],[125,532],6)
            
        if surligner == 4: # on surligne la fleche droite
            pygame.draw.line(fenetre,bleu,[475,532],[545,532],6)
            
        
        pygame.display.flip()
        
        
    def menu(self,fenetre,difficulter=2,surligner=0):
        '''Prend en paramètre
        - fenetre : l'écran sur lequelle on doit afficher des objects
        
        Cette fonction détecte toutes les interactions possible sur le menu du jeu à l'aide de clavier/ souris (ex fleche gauche cliquer ou souris sur le bouton jouer) et met à jour l'affichage du menu du jeu à l'aide de la fonction menu_affichage
        
        Cette fonction renvoie une valeur int(0 à 3) qui indique si on joue contre une ia (0 ou 1,2,3) et si oui quelle est la difficulté de cette ia
        '''
        self.menu_affichage(fenetre,difficulter,surligner)
        clavier = False
        
        while True: # La boucle s'arretera au return de la fonction
            
            # Recuperer tout les inputs
            for event in pygame.event.get():
                
                if clavier == False:
                    surligner = 0
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                pos = pygame.mouse.get_pos()
                    
                if pos[0] > 170 and pos[0] < 425 and pos[1] > 80 and pos[1] < 170:
                    
                    # On lance le jeu à deux Joueurs 
                    if event.type == MOUSEBUTTONDOWN and event.button == 1: 
                        return 0
                    
                    surligner = 1
                    clavier = False
                    
                if pos[0] > 170 and pos[0] < 425 and pos[1] > 285 and pos[1] < 350:
                    
                    # On lance le jeu contre l'ia  (un seul Joueur)
                    if event.type == MOUSEBUTTONDOWN and event.button == 1: 
                        return difficulter
                        
                    surligner = 2
                    clavier = False
                    
                    
                if pos[0] > 50 and pos[0] < 125 and pos[1] > 465 and pos[1] < 525:
                    
                    if difficulter >=2:
                        surligner = 3
                        
                        # Flèche droite clicker: on augmente la difficulter de l'ia
                        if event.type == MOUSEBUTTONDOWN and event.button == 1: 
                            difficulter -=1
                    
                if pos[0] > 470 and pos[0] < 555 and pos[1] > 465 and pos[1] < 525: 
                
                    if difficulter <=2:
                        surligner = 4
                        
                        # Flèche droite clicker: on augmente la difficulter de l'ia
                        if event.type == MOUSEBUTTONDOWN and event.button == 1: 
                            difficulter +=1
                            
                if event.type == pygame.KEYDOWN:   
                
                    if event.key == pygame.K_UP:
                        surligner = 1
                        clavier = True
                        
                    if event.key == pygame.K_DOWN:
                        surligner = 2
                        clavier = True
                        
                    if event.key == pygame.K_LEFT:
                        if difficulter >=2:
                            difficulter -=1
                            
                    if event.key == pygame.K_RIGHT:
                        if difficulter <=2:
                            difficulter +=1
                            
                    if event.key == pygame.K_RETURN:
                        
                        if surligner == 1:
                            return 0
                        
                        if surligner == 2:
                            return difficulter
            
            
            pygame.time.wait(50)  # On fait une pause de 50 milisecondes donc 0,05 secondes pour éviter de surcharger inutilement
            self.menu_affichage(fenetre,difficulter,surligner)
                        
        

    def pseudo(self,fenetre,difficulter):
        '''Prend en paramètre
        - fenetre : l'écran sur lequelle on doit afficher des objects
        
        Cette fonction affiche un sous-menu pour permettre au Joueurs de choisir un pseudo et renvoie une liste contenant le nom des deux joueurs ou du joueur1 et de l'IA.
        
        A noter que je me suis basé sur un code que j'ai trouver sur internet que j'ai ensuite analysé et réadapté
        https://stacklima.com/comment-creer-une-zone-de-saisie-de-texte-avec-pygame/
        '''
        
        police_ecriture = pygame.font.Font(None, 48) # police d'écriture de base, taille 48
        nom_joueurs = ['',''] # [ nom du Joueur 1  , nom du Joueur 2 ]
        
        
        # si on joue contre une ia on lui donne un nom par défaut 
        if difficulter != 0:
            nom_bot = ["Bot(Jean Bombeur)","Bot(Louis Fine)","Bot(Anne Riz)","Bot(Le Père Spective)","Bot(Jone Yalidai)"]
            nom_joueurs[1] = nom_bot[randint(0,4)]
            
        couleur_active = pygame.Color('lightskyblue3') # couleurs de fond de texte, lorsqu'on écrit
        couleur_passive = pygame.Color('chartreuse4') # couleurs de fond de texte de base
        
        couleur_texte_j1 = couleur_active
        couleur_texte_j2 = couleur_passive
        
        largeur_texte_j1 = 140
        largeur_texte_j2 = 140
    
        ecrit = True
        actif = 0  # Permet de définir sur quel zone de texte on écrit, ( actif =0 : Joueurs 1 ) ,  ( actif =1 : Joueurs 2 )
        
        while ecrit == True:   # Tant qu'on a pas clicker sur la bouton valider
            
            for event in pygame.event.get(): 
        
                if event.type == pygame.QUIT:
                    
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN: # Si click gauche ou droit 
                    
                    pos = pygame.mouse.get_pos()
                    
                    # Si la position de la souris est sur le bouton valider
                    if pos[0] > 275 and pos[0] <325 and pos[1] > 500 and pos[1] < 550: 
                        
                        ecrit = False # On sort de la boucle
                    
                    # si la position de la souris est sur la zone de texte j1
                    if pos[0] > 100 and pos[0] <100+largeur_texte_j1 and pos[1] > 200 and pos[1] < 232: 
                        
                        # On définit qu'on va désormais écrire dans la zone j1
                        actif = 0
                        couleur_texte_j1 = couleur_active
                        couleur_texte_j2 = couleur_passive
                        
                    
                    if difficulter == 0:  # S'il y a bien 2 joueurs 
                    
                        # si la position de la souris est sur la zone de texte j2
                        if pos[0] > 100 and pos[0] <100+largeur_texte_j2 and pos[1] > 400 and pos[1] < 432: 
                            
                            # On définit qu'on va désormais écrire dans la zone j2
                            actif = 1
                            couleur_texte_j2 = couleur_active
                            couleur_texte_j1 = couleur_passive
                        
                
                if event.type == pygame.KEYDOWN:  # Si une touche du clavier est appuyer
                    
                    # Si la touche supprimer est appuyer, on supprimer la dernière lettre du nom de joueur
                    if event.key == pygame.K_BACKSPACE:
                        nom_joueurs[actif] = nom_joueurs[actif][:-1]
                    
                    elif event.key == K_RETURN:
                        if actif == 0 and difficulter == 0:
                            actif = 1
                        else:
                            ecrit = False
                        
                    # Si le nombre de caractère est infèrieur à 20, on ajoute tous les caractères unicode qui existe à notre nom de joueur
                    elif len(nom_joueurs[actif]) <= 20:
                        nom_joueurs[actif] += event.unicode
            
            # On réinitialise la fenètre pour éviter des bugs d'affichages
            blanc = (255,255, 255)
            fenetre.fill(blanc)
            
            noir = (0,0,0)
            police_ecr_titre = pygame.font.Font(None, 85)
            
            #On affiche le Titre Joueur 
            texte_Titre_Joueur_1 = police_ecr_titre.render("Joueur 1", True, noir)
            fenetre.blit(texte_Titre_Joueur_1, (100, 125))
            
             
            if difficulter >= 1:
                # On affiche le nom donné à l'IA
                texte_Titre_Joueur_2 = police_ecr_titre.render("Ordinateur : ", True, noir)
                fenetre.blit(texte_Titre_Joueur_2, (100, 325))
            else:
                # ou on affiche le nom du Joueur 2
                texte_Titre_Joueur_2 = police_ecr_titre.render("Joueur 2 : ", True, noir)
                fenetre.blit(texte_Titre_Joueur_2, (100, 325))
                
            
            # On définit nos zone de texte
            zone_texte_j1 = police_ecriture.render(nom_joueurs[0], True, (255, 255, 255))
            zone_texte_j2 = police_ecriture.render(nom_joueurs[1], True, (255, 255, 255))
            
            # On change la largeur des rectangles de zone de texte en fonction de la taille de notre texte, pour éviter qu'il dépasse 
            largeur_texte_j1 = max(100, zone_texte_j1.get_width()+15)
            largeur_texte_j2 = max(100, zone_texte_j2.get_width()+15)
            
            # On déssine les rectangles de zone de texte
            pygame.draw.rect(fenetre, couleur_texte_j1, (100, 200, largeur_texte_j1, 48))
            pygame.draw.rect(fenetre, couleur_texte_j2, (100, 400, largeur_texte_j2, 48))
            
            # Affiche les noms des différents joueurs
            fenetre.blit(zone_texte_j1, (108, 208))
            fenetre.blit(zone_texte_j2, (108, 408))
            
            
            vert = (119,178,85)
            
            #Bouton Valider
            pygame.draw.rect(fenetre, vert, (275, 500, 50, 50))
            pygame.draw.line(fenetre, blanc,[285,530],[295,540],6)
            pygame.draw.line(fenetre, blanc,[295,540],[315,510],6)
            
            pygame.display.flip()
            pygame.time.Clock().tick(60)
            
        # Si aucun nom n'est renseigné on donne un nom par default
        for i in range(len(nom_joueurs)):
            if nom_joueurs[i] == '':
                nom_joueurs[i] = "Joueur " + str(i+1)
        
        return nom_joueurs
        
        
    def tour_joueur(self,fenetre,nom_joueur,numero_joueur):
        '''Prend en paramètre
        - fenetre : l'écran sur lequelle on doit afficher des objects
        - nom_joueur : listes contenant les nom des deux joueurs, avec le nom du Joueurs 2 qui peut être le nom de l'IA
        - numéro_joueur : int (0,1) qui indique quel est le joueur qui dois jouer
        
        Cette fonction affiche en haut de l'écran quel est le joueur qui dois jouer
        ''' 
        
        bleu = (0,0,255)
        rouge= (255,0,0)
        blanc = (255,255,255)
        

        if numero_joueur == 0:
            couleur = bleu
            pseudo = nom_joueur[0]
        else:
            couleur = rouge
            pseudo = nom_joueur[1]
            
        # reset l'affichage du score pour éviter certains problèmes de superposition
        pygame.draw.rect(fenetre, blanc, (0, 0, 600, 75))
        
        police_ecr = pygame.font.Font('freesansbold.ttf', 25)
        chaine = "C'est au tour de " + str(pseudo)
        
        texte_Joueur = police_ecr.render(chaine, True, couleur)
        fenetre.blit(texte_Joueur, (20,20))
        
        pygame.display.flip()
        
    def fin_partie_surligner(self,fenetre):
        '''Prend en paramètre
        - fenetre : l'écran sur lequelle on doit afficher des objects
        
        Cette fonction surligne le bouton rejouer du menu de fin de partie
        '''
        
        bleu = (0,0,255)
        pygame.draw.line(fenetre,bleu,[230,575],[360,575],6)
    
        
    def fin_partie(self,fenetre,score,victoire,nom_joueurs):
        '''Prend en paramètre
        - fenetre : l'écran sur lequelle on doit afficher des objects
        - score : listes qui contient le Score de la partie : [nombre de Victoire (J1), nombre de match nul, nombre de Défaite (J1)]
        note : le nombre de défaite d'un joueur et égal au nombre de victoire du joueur adverse
        
        - victoire : tuple de type (boolean, numéro du Joueur qui gagne int(1 ou 2), numéro de case1 int (0 à 9), numéro de case 2 int (0 à 9))
        - nom_joueur : listes contenant les nom des deux joueurs, avec le nom du Joueurs 2 qui peut être le nom de l'IA
        
        Indique le score de la partie et quel Joueur à gagné la manche, et propose de relancer une partie.
        '''
        ## On affiche qui a gagné en haut de l'écran
        
        bleu = (0,0,255)
        rouge = (255,0,0)
        noir = (0,0,0)
        blanc = (255,255,255)
        
        pygame.draw.rect(fenetre, blanc, (0, 0, 600, 75))
        
        police_ecr = pygame.font.Font('freesansbold.ttf', 25)
        
        if victoire[0] == True:

            
            if victoire[1] == 2:
                couleur = rouge
                chaine_str = str(nom_joueurs[1]) + " à gagné la manche"
                
            else:
                couleur = bleu
                chaine_str = str(nom_joueurs[0]) + " à gagné la manche"
                  
            texte_joueur = police_ecr.render(chaine_str, True, couleur)
            fenetre.blit(texte_joueur, (20,20))
            

        else:
        
            texte_egaliter = police_ecr.render("égalité", True, noir)
            fenetre.blit(texte_egaliter, (250,20))
    
        pygame.display.flip()
        
        
        ## On met un délai de 3 secondes afin de bien voir la grille de jeu final, avec la possibilité passer directement à l'affichage du score en cliquant sur n'importe quel touche
        timer = 0
        while timer <= 60:
            pygame.time.wait(50)
            timer +=1
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    timer = 60
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    timer = 60
        
        ## On affiche le menu fin de partie avec les scores 
        fenetre.fill(blanc)
        
        # Bordure
        pygame.draw.line(fenetre,noir,[0,0],[600,0],15)
        pygame.draw.line(fenetre,noir,[0,0],[0,650],15)
        pygame.draw.line(fenetre,noir,[600,0],[600,650],15)
        pygame.draw.line(fenetre,noir,[0,650],[600,650],15)
        
        # Police d'écriture
        police_ecr = pygame.font.Font('freesansbold.ttf', 25)
        police_ecr_titre = pygame.font.Font(None, 60)
        
        # Nom Joueur 1
        txt_1 = nom_joueurs[0] + " :"
        
        # Nombre de partie gagné par le Joueur 1
        if score[0] >= 2:
            txt_2 = str(score[0]) + " parties Gagnées"
        else:
            txt_2 = str(score[0]) + " partie Gagnée"
        
        # Nombre d'égalités
        if score[1] >= 2:
            txt_3 = str(score[1]) + " égalités"
        else:
            txt_3 = str(score[1]) + " égalité"
        
        # Nombre de partie Joués
        if score[0]+score[1]+score[2] >= 2:
            txt_4 = "pour " + str(score[0]+score[1]+score[2]) + " parties jouées"
        else:
            txt_4 = "pour " + str(score[0]+score[1]+score[2]) + " partie jouée"
            
        # Nom Joueur 2 ou IA
        txt_5 = nom_joueurs[1] + " :"
         
        # Nombre de partie gagné par le Joueur 1 ou l'IA
        if score[0] >= 2:
            txt_6 = str(score[2]) + " parties Gagnées"
        else:
            txt_6 = str(score[2]) + " partie Gagnée"
        
        # On définit les zones de textes
        zone_txt_1 = police_ecr.render(txt_1, True, bleu)
        zone_txt_2 = police_ecr.render(txt_2, True, bleu)
        zone_txt_3 = police_ecr.render(txt_3, True, noir)
        zone_txt_4 = police_ecr.render(txt_4, True, noir)
        zone_txt_5 = police_ecr.render(txt_5, True, rouge)
        zone_txt_6 = police_ecr.render(txt_6, True, rouge)
        
        
        # on affiche les differents textes
        fenetre.blit(zone_txt_1, (100,230))
        fenetre.blit(zone_txt_2, (100,260))
        fenetre.blit(zone_txt_3, (100,310))
        fenetre.blit(zone_txt_4, (100,340))
        fenetre.blit(zone_txt_5, (100,390))
        fenetre.blit(zone_txt_6, (100,420))
        
        
        
        # Si on gagne 
        if victoire[0] == True:
            # Indique qui à gagné la partie
            if victoire[1] == 2:
            
                texte_joueur = police_ecr_titre.render(nom_joueurs[1], True, rouge)
                fenetre.blit(texte_joueur, (100,70))
                texte_gagnant = police_ecr_titre.render("à gagné la manche", True, rouge)
                fenetre.blit(texte_gagnant, (100,120))
                
            else:
                
                texte_joueur = police_ecr_titre.render(nom_joueurs[0], True, bleu)
                fenetre.blit(texte_joueur, (100,70))
                texte_gagnant = police_ecr_titre.render("à gagné la manche", True, bleu)
                fenetre.blit(texte_gagnant, (100,120))
            
        
        else:
            # Indique qu'il y a eu égalité
            texte_egaliter = police_ecr_titre.render("égalité", True, noir)
            fenetre.blit(texte_egaliter, (225,70))
        
        # Affiche un bouton rejouer
        texte_rejouer = police_ecr_titre.render("Rejouer", True, noir)
        fenetre.blit(texte_rejouer, (220,530))
        
        # Affiche une croix rouge en haut à droite
        pygame.draw.line(fenetre,rouge,[540,20],[580,60],8)
        pygame.draw.line(fenetre,rouge,[540,60],[580,20],8)
    
        pygame.display.flip()
        pygame.time.wait(100)
        
        while True: # La boucle s'arretera au return de la fonction
            
            surligner = False
            
            # Recuperer tout les inputs
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                # Si la souris est sur le bouton jouer
                pos = pygame.mouse.get_pos()
                if pos[0] > 220 and pos[0] < 370 and pos[1] > 525 and pos[1] < 570:
                    
                    surligner = True
                    
                    # Si en plus on click dessus ou relancer une partie
                    if event.type == MOUSEBUTTONDOWN and event.button == 1: 
                        return True
                
                # Si on clique sur la croix rouge on quitte pygame
                if pos[0] > 540 and pos[0] < 580 and pos[1] > 20 and pos[1] < 60 and event.type == MOUSEBUTTONDOWN and event.button == 1:
                    pygame.quit()
                    sys.exit()
                    return False
                    
                # Si souris sur le bouton jouer on surligne le bouton
                if surligner == True:
                    self.fin_partie_surligner(fenetre)
                
                # Sinon on affiche un rectangle blanc pour cacher le surlignage
                else:
                    pygame.draw.rect(fenetre, blanc, (200, 571, 200, 10))
                    
                    
                if event.type == pygame.KEYDOWN:
                    
                    # Si touche entrée appuyé on relance une partie 
                    if event.key == K_RETURN:
                        return True
                    
                    # si touche echap appuyer on quitte pygame
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                        return False
                    
            pygame.time.wait(50)
            pygame.display.flip()