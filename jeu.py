from random import randrange

# Affichage du plateau
def afficher_plateau(plateau):
    print("+-------" * 3 + "+")
    for ligne in range(3):
        print("|       " * 3 + "|")
        print("|  {}    |  {}    |  {}    |".format(plateau[ligne][0], plateau[ligne][1], plateau[ligne][2]))
        print("|       " * 3 + "|")
        print("+-------" * 3 + "+")

# Initialisation du plateau
plateau = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
plateau[1][1] = 'X'  # premier coup de l'ordi au centre

# Saisie du coup par le joueur
def entrer_coup(plateau):
    valide = False
    while not valide:
        coup = input("Entrez votre coup : ")
        valide = len(coup) == 1 and '1' <= coup <= '9'
        if not valide:
            print("Coup invalide – réessayez !")
            continue
        coup = int(coup) - 1
        ligne = coup // 3
        colonne = coup % 3
        case = plateau[ligne][colonne]
        valide = case not in ['O', 'X']
        if not valide:
            print("Case déjà occupée – réessayez !")
            continue
    plateau[ligne][colonne] = 'O'

# Liste des cases libres
def liste_cases_libres(plateau):
    libres = []
    for ligne in range(3):
        for colonne in range(3):
            if plateau[ligne][colonne] not in ['O', 'X']:
                libres.append((ligne, colonne))
    return libres

# Vérifie si un joueur a gagné
def victoire_pour(plateau, symbole):
    gagnant = 'ordinateur' if symbole == 'X' else 'vous'
    diagonale1 = diagonale2 = True
    for i in range(3):
        if all(plateau[i][j] == symbole for j in range(3)) or all(plateau[j][i] == symbole for j in range(3)):
            return gagnant
        if plateau[i][i] != symbole:
            diagonale1 = False
        if plateau[2 - i][i] != symbole:
            diagonale2 = False
    if diagonale1 or diagonale2:
        return gagnant
    return None

# Coup aléatoire de l’ordinateur
def jouer_ordinateur(plateau):
    libres = liste_cases_libres(plateau)
    if libres:
        i = randrange(len(libres))
        ligne, colonne = libres[i]
        plateau[ligne][colonne] = 'X'

# Boucle principale de jeu
cases_libres = liste_cases_libres(plateau)
tour_joueur = True
gagnant = None

while cases_libres:
    afficher_plateau(plateau)
    if tour_joueur:
        entrer_coup(plateau)
        gagnant = victoire_pour(plateau, 'O')
    else:
        jouer_ordinateur(plateau)
        gagnant = victoire_pour(plateau, 'X')
    if gagnant is not None:
        break
    tour_joueur = not tour_joueur
    cases_libres = liste_cases_libres(plateau)

afficher_plateau(plateau)
if gagnant == 'vous':
    print(" Bravo, vous avez gagné !")
elif gagnant == 'ordinateur':
    print(" L'ordinateur a gagné !")
else:
    print(" Match nul !")
