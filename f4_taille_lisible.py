import os
from pathlib import Path
dossier = Path("C:/Users/danon/Python/python-semaine_0511206/bac-a-sable")
#dossier = "bac-a-sable"
contenu = sorted(os.listdir(dossier))

for nom in contenu:
    chemin = os.path.join(dossier, nom)
    #print(f"{chemin}")
    size = os.path.getsize(chemin)
    if os.path.isdir(chemin) is False:
        if size > 1024 and size < 1048576:
            print(f"{nom:15} : {size/1024:>10.2f} Ko")
        elif size < 1024:
            print(f"{nom:15} : {size/1024:>10.2f} octets")
        elif size >= 1048576:
            print(f"{nom:15} : {size/1048576:>10.2f} Mo")
        elif size > (2**30):
            print(f"{nom:15} : {size/(2**30):>10.2f} Go")
        

