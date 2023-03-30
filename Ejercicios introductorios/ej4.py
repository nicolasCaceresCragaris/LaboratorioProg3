def validar(hipotenusa,catetoUno,catetoDos):

    if pow(catetoUno,2)+pow(catetoDos,2)==pow(hipotenusa,2):
        print("Es un triangulo rectangulo")
    else:
        print("No es un triangulo rectangulo")



def main():
    hipotenusa=float(input("Ingrese hipotenusa: "))
    catetoUno=float(input("Ingrese cateto uno: "))
    catetoDos=float(input("Ingrese cateto dos: "))
    validar(hipotenusa,catetoUno,catetoDos)

if __name__=='__main__':
    main()