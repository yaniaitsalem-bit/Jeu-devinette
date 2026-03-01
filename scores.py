
import os

FICHIER_SCORES = \"scores.txt\"


def sauvegarder_score(nom_joueur, tentatives, difficulte):
    \"\"\"Sauvegarde un score dans le fichier.\"\"\"
    with open(FICHIER_SCORES, \"a\") as f:
        f.write(f\"{nom_joueur},{tentatives},{difficulte}\n\")
    print(\"Score sauvegarde !\")


def afficher_scores():
    \"\"\"Affiche les meilleurs scores enregistres.\"\"\"
    if not os.path.exists(FICHIER_SCORES):
        print(\"\nAucun score enregistre pour le moment.\")
        return

    print(\"\n=============================\")
    print(\"    MEILLEURS SCORES\")
    print(\"=============================\")
    print(f\"{'Joueur':<15} {'Tentatives':<12} {'Difficulte'}\")
    print(\"-\" * 40)

    scores = []
    with open(FICHIER_SCORES, \"r\") as f:
        for ligne in f:
            parties = ligne.strip().split(\",\")
            if len(parties) == 3:
                nom, tent, diff = parties
                scores.append((nom, int(tent), diff))

    scores.sort(key=lambda x: x[1])

    for nom, tent, diff in scores[:10]:
        print(f\"{nom:<15} {tent:<12} {diff}\")

    print(\"=============================\")
"
