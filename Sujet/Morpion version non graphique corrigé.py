# Proposition de corrigé du projet Morpion
# M. Pereira - T. Rey
# 100 lignes de codes effectives - le reste c'est de la documentation et des commentaires...

from random import randint

def grille_vide():
    """Cette fonction retourne une grille de Morpion vide
    c'est-à-dire une liste de trois listes remplies de 0."""
    return [[0,0,0],[0,0,0],[0,0,0]]


def affiche(g):
    """Cette fonction affiche la grille de Morpion g (au sens de la fonction grille_vide).
    0 = case vide
    1 = case occupée par le joueur 1 : X
    2 = case occupée par le joueur 2 = O.
    """
    # On crée une table des caractères utilisés :
    table = ['.','X','O']
    # Première ligne :
    print(' |A|B|C')
    # On traite chaque ligne :
    for l in range(3):
        # On crée une chaine contenant le numéro de ligne
        ligne = str(l+1)
        # e va contenir les éléments 0, 1 ou 2
        for e in g[l]:
            # On ajoute le caractère précédé d'une |
            ligne += '|' + table[e]
        # Affichage de la ligne :
        print(ligne)


def colonne_ligne(coup):
    """Cette fonction retourne le numéro de colonne et de ligne du coup passé en paramètre.
    Un coup est une chaîne de la forme 'Ln' où :
    L est une lettre parmi A, B et C
    n est un chiffre parmi 1, 2, 3.
    PAr exemple colonne_ligne('A3') retourne 0,2.
    """
    assert coup[0] in ['A', 'B', 'C'], "Mauvaise lettre de colonne (A, B ou C)"
    assert coup[1] in ['1', '2', '3'], "Mauvaise ligne : 1, 2 ou 3"
    colonne = ord(coup[0]) - 65 # ord(caractère) retourne le code ASCII du caractère (A=65, B=66, C=67) donc en retirant 65 on a 0, 1 ou 2
    ligne = int(coup[1]) - 1
    return colonne, ligne



def coup_possible(g,c):
    """Retourne un booléen indiquant si la case représentée par la chaîne c est libre dans la grille de Morpion g."""
    colonne, ligne = colonne_ligne(c)
    return g[ligne][colonne] == 0


def jouer(g,j,Ln):
    """Cette fonction joue le coup c du joueur j dans la grille g.
    C'est-à-dire qu'il place la valeur du joueur au bon endroit dans la grille.
    """
    assert coup_possible(g,Ln), "Ce coup est impossible"
    colonne, ligne = colonne_ligne(Ln)
    g[ligne][colonne] = j

def horiz(g,j):
    """Cette fonction détermine si le joueur j a 3 pions alignés horizontalement. Elle retourne un booléen correspondant."""
    for ligne in g:
        p = ligne[0]*ligne[1]*ligne[2]
        # Il y a un alignement sur CETTE ligne ?
        if p == j**3:
            return True
    # A la fin on n'a pas vu d'alignement  donc :
    return False


def vertic(g,j):
    """Cette fonction détermine si le joueur j a 3 pions alignés vericalement. Elle retourne un booléen correspondant."""
    for c in range(3):
        p = g[0][c]*g[1][c]*g[2][c]
        # Il y a un alignement sur CETTE colonne ?
        if p == j**3:
            return True
    # A la fin on n'a pas vu d'alignement  donc :
    return False


def diag(g,j):
    """Cette fonction détermine si le joueur j a 3 pions alignés en diagonale. Elle retourne un booléen correspondant."""
    if g[0][0] * g[1][1] * g[2][2] == j**3:
        return True
    if g[0][2] * g[1][1] * g[2][0] == j**3:
        return True
    return False

def victoire(g,j):
    """ """
    return horiz(g,j) or vertic(g,j) or diag(g,j)

def partie_nulle(g):
    """ """
    # Un vainqueur :
    for j in range(1,3):
        if victoire(g,j):
            # Il y a un gagnant donc la partie n'est pas nulle
            return False
    # Pas de case vide :
    # Produit de toute les cases : si ce produit est nul
    # C'est qu'une case est nulle donc vide donc partie non finie
    p = 1
    for ligne in g:
        for e in ligne:
            p = p * e
    return p != 0



def partie_a_deux():
    """Cette fonction permet de lancer une partie à deux joueurs"""
    noms = []
    for j in range(1,3):
        noms.append(input("Joueur " +str(j)+ ", quel est ton nom ? "))

    grille = grille_vide()
    # Joueur courant :
    j = randint(1,2)

    # Quand j = 1 ou 2 alors j%2+1 vaut l'autre valeur.
    while not partie_nulle(grille) and not victoire(grille,j%2 + 1):
        affiche(grille)
        coup = input(noms[j-1] + ", quel coup joues-tu (ex : A2) ? ")
        while not coup_possible(grille, coup):
            print("Déjà pris !")
            coup = input(noms[j-1] + ", quel coup joues-tu (ex : A2) ? ")
        jouer(grille,j,coup)
        j = j%2 + 1

    affiche(grille)
    if victoire(grille, j%2+1):
        print("Bravo "+noms[j%2])
    else:
        print("Partie nulle")

