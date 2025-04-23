def suma_consecutiva(lista):
    sumas=[]
    suma_alta = 0 
    for i in range(len(lista)-1): # Iteramos hasta el penúltimo elemento para evitar un índice fuera de rango
        sum = lista[i] + lista[i+1] # Sumar el elemento actual con el siguiente
        sumas.append(sum) # Guardamos la suma en la lista de sumas
    for i in range(len(sumas)): 
        if sumas[i] > suma_alta: # Comparamos cada suma con la suma más alta encontrada hasta ahora
            suma_alta = sumas[i] # Actualizamos la suma más alta si encontramos una mayor
    return suma_alta

if __name__ == "__main__":
    max_suma = suma_consecutiva([1,2,3,4,5])
    print(max_suma) # 9