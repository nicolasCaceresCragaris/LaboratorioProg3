from clases.persona import Persona

def main():

    persona=Persona("Ricardo","Gutierres")

    print(f"{persona.nombre} {persona.apellido}")
    
    persona.nombre="Pedro"
    persona.apellido="Alfa"

    print(f"{persona.nombre} {persona.apellido}")


if __name__=='__main__':
    main()