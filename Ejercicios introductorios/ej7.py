
def determinarSigno(dia,mes):
    match mes:
        case 1:
            if(dia<=19):
                print("Capricornio")
            if(dia>=20):
                print("Aquario")
           
        
        case 2:
            if(dia<=18):
                print("Aquario")
            if(dia>=19):
                print("Piscis")
        
        case 3:
            if(dia<=20):
                print("Piscis")
            if(dia>=21):
                print("Aries")

        case 4:
            if(dia<=19):
                print("Aries")
            if(dia>=20):
                print("Tauro")
        
        case 5:
            if(dia<=20):
                print("Tauro")
            if(dia>=21):
                print("Geminis")
        
        case 6:
            if(dia<=20):
                print("Geminis")
            if(dia>=21):
                print("Cancer")
        
        case 7:
            if(dia<=22):
                print("Cancer")
            if(dia>=23):
                print("Leo")
        
        case 8:
            if(dia<=22):
                print("Leo")
            if(dia>=23):
                print("Virgo")
        
        case 9:
            if(dia<=22):
                print("Virgo")
            if(dia>=23):
                print("Libra")

        case 10:
            if(dia<=22):
                print("Libra")
            if(dia>=23):
                print("Escorpio")
            
        case 11:
            if(dia<=21):
                print("Escorpio")
            if(dia>=22):
                print("Sagitario")
        
        case 12:
            if(dia<=21):
                print("Sagitario")
            if(dia>=22):
                print("Capricornio")


def main():

    dia=int(input("Ingrese el dia de nacimiento: "))
    mes=int(input("Ingrese el mes de nacimiento: "))
    determinarSigno(dia,mes)


if __name__=='__main__':
    main()