__author__ = 'andrew'

nb = input("saisissez un nombre : ")
nb = int(nb)
i = 0

while i < 10:
    print(i + 1, " * ", nb, " = ",(i+1)*nb  )
    i +=1