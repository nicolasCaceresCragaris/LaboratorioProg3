
def calcularPromedio(notaUno, notaDos, notaTres):
    return (notaUno+notaDos+notaTres)/3

def mostrarMensaje(promedio):

    if promedio<4:
        print("Insuficiente")
    elif promedio>=4 and promedio<6:
        print("Regular")
    elif promedio>=6 and promedio<8:
        print("Bien")
    elif promedio>=8 and promedio<9:
        print("Muy Bien")
    elif promedio>=9 and promedio<10:
        print("Sobresaliente")

    print(f"Su promedio fue {promedio}.")

    return

def main():

    notaUno=float(input("Ingrese una nota: "))
    notaDos=float(input("Ingrese nota dos: "))
    notaTres=float(input("Ingrese nota tres: "))

    promedio=calcularPromedio(notaUno,notaDos,notaTres)

    mostrarMensaje(promedio)

    


    #comentario
    


if __name__=='__main__':
    main()