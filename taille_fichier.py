import os

dossier = "bac-a-sable"

contenu = sorted(os.listdir(dossier))

for nom in contenu:
    chemin = os.path.join(dossier, nom)
    #print({chemin})
    size = os.path.getsize(chemin)
    if os.path.isdir(chemin):
    #    print(f"[D] {nom}")
        print(f"[D] size of {nom:15} : {size} bytes")
    else:
    #    print(f"[F] {nom}")
        print(f"[F] size of {nom:15} : {size} bytes")   
    #    print(f"[F] size of {nom} '{chemin}': {size} bytes")