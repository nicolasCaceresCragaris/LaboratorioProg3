def mostrarLeyenda(edad):
    if edad>0 and edad<=12:
        print("Menor")
    if edad>12 and edad<=18:
        print("Cadete")
    if edad>18 and edad<26:
        print("Juvenil")
    if edad>=26:
        print("Mayor")


def main():

    edad=int(input("Ingrese la edad: "))
    mostrarLeyenda(edad)
   

if __name__=='__main__':
    main()