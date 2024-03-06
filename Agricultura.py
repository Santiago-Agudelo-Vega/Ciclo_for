def main():
    # Paso 1: Definir los requisitos de riego para cada cultivo
    riego_cultivos = {}

    # Paso 2: Solicitar al usuario que ingrese la cantidad de riego requerida para cada cultivo
    cultivos = ['papa', 'yuca', 'zanahoria']
    for cultivo in cultivos:
        riego = float(input(f"Ingrese el requerimiento de riego (en litros) para {cultivo}: "))
        riego_cultivos[cultivo] = riego
    
    # Paso 3: Mostrar los requisitos de riego para cada cultivo
    print("\nRequisitos de Riego para cada Cultivo:")
    for cultivo, riego in riego_cultivos.items():
        print(f"{cultivo.capitalize()}: {riego} litros por semana")

if __name__ == "__main__":
    main()