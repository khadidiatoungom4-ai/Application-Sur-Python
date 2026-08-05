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
  
             ##### Partie 5 : Listes ####

datasets = []

while True:
    print("\n====================")
    print("1. Ajouter un dataset")
    print("2. Afficher les datasets")
    print("3. Rechercher")
    print("4. Trier")
    print("5. Modifier")
    print("6. Supprimer")
    print("7. Quitter")
    print("====================")

    choix = input("Votre choix : ")

    if choix == "1":
        print(" Ajouter un dataset")       
        nom = input("Nom du dataset : ")
        domaine = input("Domaine : ")
        lignes = int(input("Nombre de lignes : "))
        colonnes = int(input("Nombre de colonnes : "))
        Mo = float(input("Taille du dataset : "))
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
        

    if choix == "2":
        print("Afficher les datasets")
        print("Nom du dataset : ",nom) 
        print("Domaine",domaine) 
        print("Nombre de lignes : ",lignes) 
        print("Nombre de colonnes : " ,colonnes) 
        print("Taille du dataset :",Mo) 
        print("Format",format) 
        print("Public",public) 

    if choix == "3":
        nom_recherche = input("Nom du dataset à rechercher : ")
        trouve = False
        for d in datasets:
         if d["nom"].lower() == nom_recherche.lower():
            print(d)
            trouve = True
            break
         if not trouve:
            print("Dataset introuvable.")

    if choix == "4":
        datasets.sort(key=lambda d: d["nom"])
        print("Liste triée :")
        for d in datasets:
         print(d)
    if choix == "5":
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

    if choix == "6":
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
    if choix == "7": 
         print("Quitter")   
         break   
   
    else:
        print("Choix invalide")


       


            