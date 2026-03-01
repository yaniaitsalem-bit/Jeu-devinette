
import random
from menu import obtenir_difficulte


def jouer_partie():
    \"\"\"Lance une partie de devinette.\"\"\"
    borne_max, nom_difficulte = obtenir_difficulte()
    nombre_secret = random.randint(1, borne_max)
    tentatives = 0

    print(f\"\nDifficulte : {nom_difficulte}\")
    print(f\"J'ai choisi un nombre entre 1 et {borne_max}.\")
    print(\"A vous de deviner !\n\")

    while True:
        saisie = input(\"Votre proposition : \")

        try:
            nombre = int(saisie)
        except ValueError:
            print(\"Erreur : veuillez entrer un nombre valide.\")
            continue

        if nombre < 1 or nombre > borne_max:
            print(f\"Erreur : le nombre doit etre entre 1 et {borne_max}.\")
            continue

        tentatives += 1

        if nombre < nombre_secret:
            print(\"C'est plus grand !\")
        elif nombre > nombre_secret:
            print(\"C'est plus petit !\")
        else:
            print(f\"\nBravo ! Vous avez trouve {nombre_secret} en {tentatives} tentatives !\")
            return tentatives, nom_difficulte
"

