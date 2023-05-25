# Desarrollar un programa que sume los elementos de una fila dada de una matriz.

def crear_matriz(filas, columnas) -> list: # Se define la función para crear una matriz dando los agumentos de filas y columnas 
    matriz = []  # Se crea una lista vacía para almacenar los valores de la matriz
    for i in range(filas):  # Se itera sobre el rango de filas
        fila = []  # Se crea una lista vacía para almacenar los valores de la fila actual
        for j in range(columnas):  # Se itera sobre el rango de columnas
            valor = float(input("Insertar valor para la posición: "))  # Se solicita ingresar un valor para la posición en la que se encuentra 
            fila.append(valor)  # Agrega el valor ingresado a la fila
        matriz.append(fila)  # Agrega la fila a la matriz
    return matriz  # Devuelve la matriz completa como una lista de listas


def suma_matriz(matriz): # Se crea la funcion para sumar matrices 
    filas = len(matriz)  # Se obtiene la cantidad de filas de la matriz usando la función len
    
    matriz_suma = []  # Se crea una lista vacía para almacenar la suma de cada fila
    
    for i in range(filas):  # Se itera sobre las filas de la matriz
        suma = 0  # Se inicia la suma en 0 para cada fila
        for j in range(len(matriz[i])):  # Se itera sobre los elementos de la fila
            suma += matriz[i][j]  # Se suma los valores de la fila
        matriz_suma.append(suma)  # Se agrega la suma al resultado de la matriz
    
    return matriz_suma  # Se devuelve la lista con la suma de cada fila de la matriz



if __name__ == "__main__":
    filas = int(input("Ingrese la cantidad de filas: "))  # Se solicita ingresar el numero de filas de las matrices
    columnas = int(input("Ingrese la cantidad de columnas: "))  # Se solicita ingresar el numero de  columnas de las matrices
    matriz_1 = crear_matriz(filas, columnas)  # Se crea la matriz con la función crear_matriz
    print("La matriz 1 es: " + str(matriz_1))  # Se imprime la matriz 

    matriz_suma_ = suma_matriz(matriz_1)   # se crea la matriz suma llamando a la función suma matriz
    print("La suma de cada fila es:", str(matriz_suma_))  # Se imprime la suma de cada fila