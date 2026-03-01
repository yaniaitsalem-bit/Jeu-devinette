"\"\"\"
Module de gestion du menu principal
\"\"\"


def afficher_menu():
    \"\"\"Affiche le menu principal du jeu.\"\"\"
    print(\"\n=============================\")
    print(\"    JEU DE DEVINETTE\")
    print(\"=============================\")
    print(\"1. Nouvelle partie\")
    print(\"2. Voir les scores\")
    print(\"3. Quitter\")
    print(\"=============================\")


def afficher_difficulte():
    \"\"\"Affiche le menu de selection de la difficulte.\"\"\"
    print(\"\nChoisissez la difficulte :\")
    print(\"1. Facile   (nombre entre 1 et 10)\")
    print(\"2. Moyen    (nombre entre 1 et 50)\")
    print(\"3. Difficile (nombre entre 1 et 100)\")


def lire_choix():
    \"\"\"Lit et retourne le choix du joueur.\"\"\"
    choix = input(\"Votre choix (1-3) : \")
    return choix


def obtenir_difficulte():
    \"\"\"Retourne la borne max selon la difficulte choisie.\"\"\"
    afficher_difficulte()
    choix = lire_choix()
    if choix == \"1\":
        return 10, \"Facile\"
    elif choix == \"2\":
        return 50, \"Moyen\"
    elif choix == \"3\":
        return 100, \"Difficile\"
    else:
        print(\"Choix invalide, difficulte Facile par defaut.\")
        return 10, \"Facile\"
"
Observation: Overwrite successful: /app/projet_rattrapage/menu.py
