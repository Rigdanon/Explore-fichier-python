import os
contenu = sorted(os.listdir("bac-a-sable"))
#contenu = (os.path.isdir("bac-a-sable"))

for nom in contenu:
    print(nom)

