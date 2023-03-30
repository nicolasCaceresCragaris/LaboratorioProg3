def determinarEdad(dia,mes,anio):
    if 2023-anio>=18 and mes<4:
        edad=2023-anio
    elif 2023-anio==18 and mes==4:
        if dia<5:
            edad=18
        if dia>5:
            edad=17
    
    return edad


def main():

    dia=int(input("Ingrese el dia de nacimiento: "))
    mes=int(input("Ingrese el mes de nacimiento: "))
    anio=int(input("Ingrese el anio de nacimiento"))
    edad=determinarEdad(dia,mes,anio)
    print(f"Edad:{edad}")

if __name__=='__main__':
    main()