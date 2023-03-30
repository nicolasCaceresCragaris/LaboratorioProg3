
def main():

    edad=int(input("Ingrese la edad: "))
    genero=input("Ingrese si es hombre o mujer: ")
    aniosAporte=int(input("Ingrese los anios de aporte: "))

    if aniosAporte>=30:
        if genero=="hombre":
            if edad>=65:
                print("Usted puede jubilarse")
            else:
                print("Usted no puede jubilarse")
        
        if genero=="mujer":
            if edad>=60:
                print("Usted puede jubilarse")
            else:
                print("Usted no puede jubilarse")

    
    else:
        print("No puede jubilarse")


if __name__=='__main__':
    main()