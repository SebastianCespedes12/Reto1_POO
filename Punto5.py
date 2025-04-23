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
if __name__ == "__main__":
    lista = ["amor", "roma", "perro"]
    lista_iguales = mismos_caracteres(lista) 
    print(mismos_caracteres(lista_iguales))# ['amor', 'roma']