def determinarCapicua(valor):
    aux=valor/1000
    auxDos=valor%100
    valorUno=int(aux/10)
    valorDos=int(aux%10)
    valorTres=int(auxDos/10)
    valorCuatro=int(auxDos%10)

    if(valorUno==valorCuatro and valorDos==valorTres):
        print("Es un numero capicua")
    else:
        print("No es un numero capicua")


def main():
    valor=int(input("Ingrese un numero de 5 digitos: "))
    determinarCapicua(valor)


if __name__=='__main__':
    main()