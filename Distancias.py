def calcular_viaje():
    # Step 1:
    num_paradas = int(input("Ingrese el número de paradas: "))
    
    distancia_total = 0
    
    # Step 2:
    for i in range(num_paradas):
        distancia = float(input(f"Ingrese la distancia a recorrer en la parada {i+1}: "))
        distancia_total += distancia
    
    # Step 3:
    print(f"Distancia total recorrida: {distancia_total} kilómetros")
    
    # Step 4:
    print(f"Número de paradas hechas: {num_paradas}")

# Step 5:
calcular_viaje()
