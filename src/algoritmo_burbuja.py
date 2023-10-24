def ordenacion_burbuja(lista):
    longitud = len(lista)
    for indice_externo in range(longitud):
        for indice_interno in range(0, longitud - indice_externo - 1):
            if lista[indice_interno] > lista[indice_interno + 1]:
                lista[indice_interno], lista[indice_interno + 1] = lista[indice_interno + 1], lista[indice_interno]
    return lista

if __name__ == "__main__":
    # Entrada
    lista = [8, 3, 1, 19, 14]
    # Proceso
    ordenacion_burbuja(lista)
    # Salida
    print("Lista ordenada: ", lista)