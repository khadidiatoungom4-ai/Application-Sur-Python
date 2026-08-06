# ############### Partie 1: Types de base, variables, Entrées et sortie ###############

# print("=====Ajout  d'un dataset=====")
# nom  = input("Nom du dataset :  ")
# domaine = input("Domaine : ")
# lignes = int(input("Nombre de lignes : "))
# colonnes = int(input("Nombre de colonnes : "))
# Mo = float(input("Taille en Mo : "))
# format = input("Format (csv/json) : ")
# public = input("Public True/False : ").lower() == "true"

# print("=====Résumé=====")
# print("Nom du dataset : ",nom) 
# print("Domaine",domaine) 
# print("Nombre de lignes : ",lignes) 
# print("Nombre de colonnes : " ,colonnes) 
# print("Taille du dataset :",Mo) 
# print("Format",format) 
# print("Public",public) 


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
while True:                          #### Afficher le menu 
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
    choix = input("Votre choix : ")


    if choix == "1":                         #Ajouter un dataset
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
        

    if choix == "2":              # Afficher les datatsets
        print("Afficher les datasets")
        print("Nom du dataset : ",nom) 
        print("Domaine",domaine) 
        print("Nombre de lignes : ",lignes) 
        print("Nombre de colonnes : " ,colonnes) 
        print("Taille du dataset :",Mo) 
        print("Format",format) 
        print("Public",public) 

    if choix == "3":                              ### Rechercher les datasets
        nom_recherche = input("Nom du dataset à rechercher : ")
        trouve = False
        for d in datasets:
         if d["nom"].lower() == nom_recherche.lower():
            print(d)
            trouve = True
            break
         if not trouve:
            print("Dataset introuvable.")

    if choix == "4":                            ### Trier les datasets
        datasets.sort(key=lambda d: d["nom"])
        print("Liste triée :")
        for d in datasets:
         print(d)
    if choix == "5":                             #### Modifier les datasets
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

    if choix == "6":                                   ##### Supprimer les datasets
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
    if choix == "7":                                            ### Statistiques des dataset 
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
    if choix == "8":                                            #### Sauvegarder les datasets
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
     
    if choix == "9":                                       #### Recharger et Afficher les datasets
     try:      ### Cette commande permet de rechercher que le dataset n'existe pas#### 
      with open("datasets.csv", "r", encoding="utf-8") as fichier:  
       reader = csv.DictReader(fichier)
       for ligne in reader:
         print(ligne)
     except FileNotFoundError:
       print("Le fichier datasets.csv n'existe pas")

    if choix == "10":
       print("Quitter")
       break
   
                    #### Partie 9: LES FONCTIONS ########
import csv
datasets = []
def afficher_menu(): 
  while True:                          #### Afficher le menu 
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
def ajouter_dataset():
  if choix == "1":                         #Ajouter un dataset
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
   if choix == "2":              # Afficher les datatsets
           print("Afficher les datasets")
           print("Nom du dataset : ",nom) 
           print("Domaine",domaine) 
           print("Nombre de lignes : ",lignes) 
           print("Nombre de colonnes : " ,colonnes) 
           print("Taille du dataset :",Mo) 
           print("Format",format) 
           print("Public",public) 

def recherche_datasets():
  if choix == "3":                              ### Rechercher les datasets
          nom_recherche = input("Nom du dataset à rechercher : ")
          trouve = False
          for d in datasets:
           if d["nom"].lower() == nom_recherche.lower():
              print(d)
              trouve = True
              break
           if not trouve:
              print("Dataset introuvable.")
def trier_dataset():
  if choix == "4":                            ### Trier les datasets
          datasets.sort(key=lambda d: d["nom"])
          print("Liste triée :")
          for d in datasets:
           print(d) 
def modifier_dataset():
 if choix == "5":                             #### Modifier les datasets
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
def Supprimer_dataset():
       if choix == "6":                                   ##### Supprimer les datasets
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
def statistiques():
     if choix == "7":                                            ### Statistiques des dataset 
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
def sauvegarder(): 
    if choix == "8":                            #### Sauvegarder les datasets
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
def recharger ():
   if choix == "9":         #### Recharger et Afficher les datasets
     try:                   ### Cette commande permet de rechercher que le dataset n'existe pas#### 
      with open("datasets.csv", "r", encoding="utf-8") as fichier:  
       reader = csv.DictReader(fichier)
       for ligne in reader:
         print(ligne)
     except FileNotFoundError:   
       print("Le fichier datasets.csv n'existe pas")           
