def esBiciesto(anio):
    if(anio%4==0 and anio%400==0 and anio%100!=0):
        return True
    else:
        return False


def calcularDias(anio,mes):

    if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
        dias=31
    elif mes==4 or mes==6 or mes==9 or mes==11:
        dias=30
    elif mes==2:
        if esBiciesto(anio)==True:
            dias=29
        else:
            dias=28

    return dias




def main():
    anio=int(input("Ingrese anio: "))
    mes=int(input("Ingrese mes: "))

    dias=calcularDias(anio,mes)
    print(f"Dias:{dias}")


if __name__=='__main__':
    main()