from menu import afficher_menu, lire_choix


def main():
    \"\"\"Boucle principale du jeu.\"\"\"
    while True:
        afficher_menu()
        choix = lire_choix()

        if choix == \"1\":
            print(\"\n[Lancement d'une nouvelle partie...]\")
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

