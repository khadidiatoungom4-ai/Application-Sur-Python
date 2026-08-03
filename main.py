# Partie 1: Types de base, variables, Entrées et sorties
print("  Les métadonnées d'un dataset  ")
nom  = input("Nom du projet :  ")
domaine = input("Domaine : ")
lignes = int(input("Nombre de lignes : "))
colonnes = int(input("Nombre de colonnes : "))
Mo = float(input("Taille en Mo : "))
format = input("Format (csv/json) : ")
public = input("Public True/False : ")

# Partie 2 Structure de controle
while True:

    print("\n====================")
    print("1. Ajouter un dataset")
    print("2. Afficher les datasets")
    print("3. Rechercher")
    print("4. Quitter")
    print("====================")

    choix = input("Votre choix : ")

    if choix == "1":
        print("Ajout d'un dataset")

    elif choix == "2":
        print("Affichage")

    elif choix == "3":
        print("Recherche")

    elif choix == "4":
        print("Au revoir")
        break

    else:
        print("Choix invalide")