__author__ = 'andrew'

chaine = "Bonjour les zéros"
for lettre in chaine:
    if lettre in "AEIOUYaeiouyé":
        print(lettre, "Voyelle")
    elif lettre in " ":
        print(lettre, "")
    else:
        print(lettre, "Consonne")


