__author__ = 'andrew'

i = 1
nombre = input("Saississedez un nombre :")
nombre = int(nombre)
print(type(nombre))
while i < nombre:
                if i % 3 == 0:
                    i += 4
                    print("On incrémente i de 4. i est a présent égal à", i)
                    continue
                print("la variable i = ", i)
                i +=1
