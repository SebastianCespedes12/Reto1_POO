# Reto1_POO
>1.Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).

Dependiendo del simbolo que el usuario elija se suma, resta, multiplica o divide.
```python
def operaciones(x:float, y:float, simb:str) -> float:
    if simb == "+":
        return x + y
    elif simb == "-":
        return x - y
    elif simb == "*":
        return x * y
    elif simb == "/":
        return x/y
```
ejemplo de uso:
```python
if __name__ == "__main__":
    opcion = input("Desea sumar(+), restar(-), multiplicar(*) o dividir(/)? \ningrese el simbolo: ")
    entrada = float(input(f"¿Cuál es el primer numero desea operar? "))
    seg_entrada = float(input(f"¿Cuál es el segundo numero desea operar? "))
    resultado = operaciones(entrada, seg_entrada, opcion)
    print(resultado)
```
>2.Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.

Se recorre la palabra desde el primer caracter hasta la mitad (no es necesario iterar todos los caracteres) se compara con el ultimo caracter hasta llegar a la mitad, es decir, se compara el primer caracter con el ultimo, el segundo con el penultimo, etc. Si alguno no coincide no es un palindromo.
```python
def palindromo(palabra: str) -> bool:
    longitud = len(palabra) 
    for i in range(longitud // 2): # Dividir entre 2 para evitar comparaciones innecesarias
        if palabra[i] != palabra[longitud - 1 - i]: # Comparar el primer y el último carácter, luego el segundo y el penúltimo, etc.
            return False  # Si alguna comparación no coincide, no es un palíndromo
    return True
```
Ejemplo de uso:
```python
if __name__ == "__main__":
    primera = palindromo("reconocer")
    print(primera) # True
    segunda = palindromo("hola")
    print(segunda) # False
```
>3.Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.

Se recorre la lista, cada numero se divide por un rango de numeros entre 2 y la mitad de este, si el modulo de alguna division es 0 signfica que tiene un divisor distinto a 1 y a si mismo.
```python
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
```
Ejemplo de uso.
```python
if __name__ == "__main__":
    numeros=[1,2,4,6,3,9,17,14]
    primos = reconocer_primo(numeros)
    print(primos) # [2, 3, 17]
```
>4.Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.

Se recorre la lista y se guardan todas las sumas posibles en una lista, dicha lista se recorre para retornar la suma mas alta.
```python
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
```
Ejemplo de uso.
```python
if __name__ == "__main__":
    max_suma = suma_consecutiva([1,2,3,4,5])
    print(max_suma) # 9
```
>5.Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres. e.g. entrada: ["amor", "roma", "perro"], salida ["amor", "roma"]

Se recorre la lista y a cada string se cuenta su caracter y las veces que aparece, esto se añade a un diccionario. Despues se recorre el diccionario y si hay dos palabras con la misma cuenta se agregan a la lista final.
```python
def mismos_caracteres(lista:list):
    todas_palabras = {}
    lista_final = []
    for i in lista:
        todas_palabras[f"{i}"] = [] # Inicializa la lista para cada palabra
        for j in range(97,123): # Itera sobre los caracteres de 'a' a 'z'
            if i.count(chr(j)) > 0: # Cuenta cuántas veces aparece el carácter en la palabra                               
                todas_palabras[f"{i}"].append(f"{i.count(chr(j))} , {chr(j)}") # Agrega el carácter y su conteo a la lista de la palabra
    for i in  todas_palabras.items(): 
        for j in todas_palabras.items():
            if i[0] != j[0] and i[1] == j[1] and i[0] not in lista_final: # Compara las listas de caracteres de diferentes palabras
                lista_final.extend([i[0]]) # Agrega la palabra a la lista final si tiene los mismos caracteres que otra
    return lista_final 

```
Ejemplo de uso.
```python
if __name__ == "__main__":
    lista = ["amor", "roma", "perro"]
    lista_iguales = mismos_caracteres(lista) 
    print(mismos_caracteres(lista_iguales))# ['amor', 'roma']
```
