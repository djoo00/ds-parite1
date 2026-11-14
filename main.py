taches = []


def ajouter():
    titre = input("Titre de la tâche : ").strip()
    if titre == "":
        print("Erreur : le titre ne peut pas être vide.")
    else:
        taches.append(titre)
        print("Tâche ajoutée avec succès.")


def afficher():
    if len(taches) == 0:
        print("Aucune tâche pour le moment.")
    else:
        for i in range(len(taches)):
            print(f"{i + 1}. {taches[i]}")


choix = ""
while choix != "0":
    print("\n=== GESTION DES TÂCHES ===")
    print("1. Ajouter une tâche   2. Afficher   0. Quitter")
    choix = input("Votre choix : ")
    if choix == "1":
        ajouter()
    elif choix == "2":
        afficher()
    elif choix == "0":
        print("Au revoir !")
    else:
        print("Choix invalide, veuillez réessayer.")
