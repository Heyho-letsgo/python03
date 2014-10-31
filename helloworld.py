__author__ = 'andrew'

# test de la fonction input

annee = input("Saisissez l'année :")
annee = int(annee)
if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 !=0):
    print("L'année est bisextile")
else:
    print("L'année n'estpas bisextile")

