import os
#contenu = sorted(os.listdir("bac-a-sable"))
#contenu = os.path.join("C:\Users\danon\Python\python-semaine_0511206", ("bac-a-sable"))
#contenu = (os.path.isdir("C:\Users\danon\Python\python-semaine_0511206"))
chemin = "."
#contenu = (os.path.isdir("chemin"))
contenu = (os.listdir("bac-a-sable"))
#print(os.path.isdir(chemin))
for nom in contenu:
#    print(nom)
#print("Est-ce un dossier?", os.path.isdir("chemin"))
#chemin = "/chemin/vers/dossier"
 
    if os.path.isdir(nom):
        print(f"{nom} est un répertoire")
    elif os.path.isfile(chemin):
        print(f"{nom} est un fichier")
    else:
        print(f"{nom} n'existe pas ou n'est ni un fichier ni un répertoire")
