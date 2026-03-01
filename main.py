from menu import afficher_menu, lire_choix
from jeu import jouer_partie
from utils import demander_rejouer


def main():
    \"\"\"Boucle principale du jeu.\"\"\"
    print(\"\nBienvenue dans le Jeu de Devinette !\")

    while True:
        afficher_menu()
        choix = lire_choix()

        if choix == \"1\":
            tentatives, difficulte = jouer_partie()
            while demander_rejouer():
                tentatives, difficulte = jouer_partie()
        elif choix == \"2\":
            print(\"\n[Affichage des scores...]\")
        elif choix == \"3\":
            print(\"\nMerci d'avoir joue ! A bientot.\")
            break
        else:
            print(\"\nChoix invalide, veuillez reessayer.\")


if __name__ == \"__main__\":
    main()
"

