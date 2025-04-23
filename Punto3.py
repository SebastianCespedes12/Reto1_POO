def reconocer_primo(lista: list):
    lista_primos = []
    for i in lista: 
        if i < 2: # Los números menores que 2 no son primos
            continue
        es_primo = True # Suponemos que el número es primo
        for j in range(2, int(i //2) + 1): # Verificamos hasta la mitad del número
            if i % j == 0: # Si el número es divisible por j, no es primo
                es_primo = False 
                break
        if es_primo: 
            lista_primos.append(i)
    return lista_primos

if __name__ == "__main__":
    numeros=[1,2,4,6,3,9,17,14]
    primos = reconocer_primo(numeros)
    print(primos) # [2, 3, 17]