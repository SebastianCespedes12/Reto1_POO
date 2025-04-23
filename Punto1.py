def operaciones(x:float, y:float, simb:str) -> float: 
    if simb == "+":
        return x + y
    elif simb == "-":
        return x - y
    elif simb == "*":
        return x * y
    elif simb == "/":
        return x/y
if __name__ == "__main__":
    opcion = input("Desea sumar(+), restar(-), multiplicar(*) o dividir(/)? \ningrese el simbolo: ")
    entrada = float(input(f"¿Cuál es el primer numero desea operar? "))
    seg_entrada = float(input(f"¿Cuál es el segundo numero desea operar? "))
    resultado = operaciones(entrada, seg_entrada, opcion)
    print(resultado)