
def verificar(ladoUno, ladoDos, ladoTres):

    if ladoUno+ladoDos>ladoTres and ladoDos+ladoTres>ladoUno and ladoTres+ladoUno>ladoDos:
        print("Forma un triangulo")
    else:
        print("No forma un triangulo")


def main():
    ladoUno=float(input("Ingrese lado uno: "))
    ladoDos=float(input("Ingrese lado dos: "))
    ladoTres=float(input("Ingrese lado tres: "))

    verificar(ladoUno,ladoDos,ladoTres)


if __name__=='__main__':
    main()