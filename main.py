
#         #              Partie 4: Tuples 
# DOMAINE = (
#             "Santé",
#             "Finance",
#             "Agriculture",
#             "Transport",
#             "Education"
#         )
  
#              ##### Partie 8: Gerer les Exceptions 
import csv
datasets = []

def afficher_menu():
    print("\n====================")
    print("1. Ajouter un dataset")
    print("2. Afficher les datasets")
    print("3. Rechercher")
    print("4. Trier")
    print("5. Modifier")
    print("6. Supprimer")
    print("7. Statistiques")
    print("8. Sauvegarder dans csv")
    print("9. Recharger et afficher dans csv")
    print("10. Quitter")
    print("====================")

def ajouter_datasets():
        print(" Ajouter un dataset")       
        nom = input("Nom du dataset : ")
        domaine = input("Domaine : ")
        try: 
         lignes = int(input("Nombre de lignes : "))
        except ValueError:print("Erreur: vous devez entrer un nombre")
        try: 
          colonnes = int(input("Nombre de Colonnes : "))
        except ValueError:print("Erreur: vous devez entrer un nombre")
        Mo = float(input("Taille en Mo : "))
        format = input("Format : ")

        public = input("Public : ").lower() == "true"
        dataset = {
                         "nom": nom,
                         "domaine": domaine,
                         "lignes": lignes,
                         "colonnes": colonnes,
                         "taille": Mo,
                         "format": format,
                         "public": public
                     }
        print(dataset)
        datasets.append(dataset)

def afficher_datasets():
          for i, dataset in enumerate(datasets, start=1):
            print("Afficher les datasets")
            print("Nom du dataset : ",dataset["nom"])
            print("Domaine",dataset["domaine"]) 
            print("Nombre de lignes : ",dataset["lignes"]) 
            print("Nombre de colonnes : " ,dataset["colonnes"]) 
            print("Taille du dataset :",dataset["taille"]) 
            print("Format",dataset["format"]) 
            print("Public",dataset["public"]) 

def rechercher_datasets():
   nom_recherche = input("Nom du dataset à rechercher : ")
   trouve = False
   for d in datasets:
            if d["nom"].lower() == nom_recherche.lower():
               print(d)
               trouve = True
               break
            if not trouve:
               print("Dataset introuvable.")

def trier_datasets():
  datasets.sort(key=lambda d: d["nom"])
  print("Liste triée :")
  for d in datasets:
    print(d)

def modifier_datasets():
    nom_recherche = input("Nom du dataset à modifier : ")
    trouve = False
    for d in datasets:
     if d["nom"].lower() == nom_recherche.lower():

        d["domaine"] = input("Nouveau domaine : ")
        d["lignes"] = int(input("Nouveau nombre de lignes : "))
        d["colonnes"] = int(input("Nouveau nombre de colonnes : "))
        d["taille"] = float(input("Nouvelle taille : "))
        d["format"] = input("Nouveau format : ")
        d["public"] = input("Public (true/false) : ").lower() == "true"

        print("Dataset modifié avec succès.")
        trouve = True
        break

    if not trouve:
      print("Dataset introuvable.")

def statistiques():
          print("Nombre de datasets :", len(datasets))           ### Nombre de Datasets 
          total = sum(d["lignes"] for d in datasets)             #### Nombre de Lignes
          print("Nombre total de lignes :", total)
          csv = sum(1 for d in datasets if d["format"] == "csv")  ### Nombre de datasets format csv
 
          repartition = {                                        ## Repartition par domaine 
          domaine: len([d for d in datasets if d["domaine"] == domaine])
          for domaine in set(d["domaine"] for d in datasets)
 }
          for domaine, nombre in repartition.items():
           print(domaine, ":", nombre)

def supprimer_datasets():
         nom_recherche = input("Nom du dataset à supprimer : ")
         trouve = False
         for d in datasets:
          if d["nom"].lower() == nom_recherche.lower():
             datasets.remove(d)
             print("dataset supprimé.")
             trouve = True
             break
         if not trouve:
          print("dataset introuvable.")

def sauvegarder():
   with open("datasets.csv", "w", newline="", encoding="utf-8") as fichier:

    champs = [
        "nom",
        "domaine",
        "lignes",
        "colonnes",
        "taille",
        "format",
        "public"
    ]

    writer = csv.DictWriter(fichier, fieldnames=champs)

    writer.writeheader()
    writer.writerows(datasets)
    print("Datasets sauvegardés dans datasets.csv")

import csv

def recharger():

    try:

        with open("datasets.csv", "r", encoding="utf-8") as fichier:

            reader = csv.DictReader(fichier)

            for ligne in reader:

                dataset = {
                    "nom": ligne["nom"],
                    "domaine": ligne["domaine"],
                    "lignes": int(ligne["lignes"]),
                    "colonnes": int(ligne["colonnes"]),
                    "taille": float(ligne["taille"]),
                    "format": ligne["format"],
                    "public": ligne["public"] == "True"
                }

                datasets.append(dataset)

        if len(datasets) == 0:
            print("Le fichier est vide.")
        else:
            afficher_datasets()
            print("Datasets rechargés avec succès.")

    except FileNotFoundError:
        print("Le fichier datasets.csv n'existe pas.")
  
while True:                          #### Afficher le menu 
    afficher_menu()
    choix = input("Votre choix : ")
    if choix == "1":                         #Ajouter un dataset
        ajouter_datasets()
    if choix == "2":   
       afficher_datasets()                 # Afficher les datatsets     
    if choix == "3":   
       rechercher_datasets                           ### Rechercher les datasets
    if choix == "4":    
      trier_datasets                        ### Trier les datasets
    if choix == "5":                       #### Modifier les datasets
       modifier_datasets() 
    if choix == "6":                                   ##### Supprimer les datasets
     supprimer_datasets()
    if choix == "7":    
       statistiques()                                        ### Statistiques des dataset 
    if choix == "8":      
       sauvegarder()                                    #### Sauvegarder les datasets
    if choix == "9":    
        recharger                               #### Recharger et Afficher les datasets
    if choix == "10":
       print("Quitter")
       break
   
 