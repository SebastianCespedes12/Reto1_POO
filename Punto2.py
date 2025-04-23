def palindromo(palabra: str) -> bool:
    longitud = len(palabra) 
    for i in range(longitud // 2): # Dividir entre 2 para evitar comparaciones innecesarias
        if palabra[i] != palabra[longitud - 1 - i]: # Comparar el primer y el último carácter, luego el segundo y el penúltimo, etc.
            return False  # Si alguna comparación no coincide, no es un palíndromo
    return True

if __name__ == "__main__":
    primera = palindromo("reconocer")
    print(primera) # True
    segunda = palindromo("hola")
    print(segunda) # False