from menu import afficher_menu, lire_choix
from jeu import jouer_partie
from scores import sauvegarder_score, afficher_scores
from utils import demander_rejouer


def main():
    \"\"\"Boucle principale du jeu.\"\"\"
    print(\"\nBienvenue dans le Jeu de Devinette !\")

    while True:
        afficher_menu()
        choix = lire_choix()

        if choix == \"1\":
            nom = input(\"Entrez votre nom : \")
            tentatives, difficulte = jouer_partie()
            sauvegarder_score(nom, tentatives, difficulte)
            while demander_rejouer():
                tentatives, difficulte = jouer_partie()
                sauvegarder_score(nom, tentatives, difficulte)
        elif choix == \"2\":
            afficher_scores()
        elif choix == \"3\":
            print(\"\nMerci d'avoir joue ! A bientot.\")
            break
        else:
            print(\"\nChoix invalide, veuillez reessayer.\")


if __name__ == \"__main__\":
    main()
"
