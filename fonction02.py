__author__ = 'andrew'

def table(nb):
    i = 0
    while i < 10:
        print(i + 1, " * ", nb, " = ",(i+1)*nb  )
        i +=1



def tablemax(nb,max):
    i = 0
    while i < max:
        print(i + 1, " * ", nb, " = ",(i+1)*nb  )
        i +=1


def tablemax10(nb,max=10):# affichage par défaut de 10 lignes de calcul.
    i = 0
    while i < max:
        print(i + 1, " * ", nb, " = ",(i+1)*nb  )
        i +=1


def tablemax20(nb,max=20): # affichage par défaut de 20 lignes de calcul.
    i = 0
    while i < max:
        print(i + 1, " * ", nb, " = ",(i+1)*nb  )
        i +=1