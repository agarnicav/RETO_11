
# Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

def crear_matriz(filas, columnas) -> list: # Se define la función para crear una matriz dando los agumentos de filas y columnas 
    matriz = []  # Se crea una lista vacía para almacenar los valores de la matriz
    for i in range(filas):  # Se itera sobre el rango de filas
        fila = []  # Se crea una lista vacía para almacenar los valores de la fila actual
        for j in range(columnas):  # Se itera sobre el rango de columnas
            valor = float(input("Insertar valor para la posición: "))  # Se solicita ingresar un valor para la posición en la que se encuentra 
            fila.append(valor)  # Agrega el valor ingresado a la fila
        matriz.append(fila)  # Agrega la fila a la matriz
    return matriz  # Devuelve la matriz completa como una lista de listas

def crear_matriz2(filas, columnas) -> list: # Se define la función para crear una segunda matriz dando los agumentos de filas y columnas 
    matriz2 = []  # Se crea una lista vacía para almacenar los valores de la segunda matriz
    for i in range(filas): # Se itera sobre el rango de filas
        fila = []  # Se crea una lista vacía para almacenar los valores de la fila actual 
        for j in range(columnas): # Se itera sobre el rango de columnas
            valor = float(input("Insertar valor para la posición: ")) # Solicita al usuario ingresar un valor para la posición actual
            fila.append(valor)  # Agrega el valor ingresado a la fila
        matriz2.append(fila)
    return matriz2 # Devuelve la segunda matriz completa como una lista de listas


def producto(matriz_1, matriz2_) -> list:   # Se define la función para hallar el producto
    filas_matriz1 = len(matriz_1)  # Se obtiene la cantidad de filas de la matriz 1
    columnas_matriz1 = len(matriz_1[0])  # Se obtiene la cantidad de columnas de la matriz 1 
    filas_matriz2 = len(matriz2_)  # Se obtiene la cantidad de filas de la matriz 2
    columnas_matriz2 = len(matriz2_[0])  # Se obtiene la cantidad de columnas de la matriz 2 

    resultado = []  # Se crea una lista vacía en la que se almacenara el resultado del producto de matrices

    for i in range(filas_matriz1):  # Se itera sobre las filas de la matriz 1
        fila = []  # Se crea una lista vacía para almacenar los valores de la fila actual del resultado
        for j in range(columnas_matriz2):  # Se itera sobre las columnas de la matriz 2
            elemento = 0  # Se inicia el valor del elemento en 0
            for k in range(columnas_matriz1):  # SE itera sobre las columnas de la matriz 1 o las filas de la matriz 2 (ambas tienen la misma longitud)
                elemento += matriz_1[i][k] * matriz2_[k][j]  # Se realiza la multiplicación y acumula el resultado en el elemento
            fila.append(elemento)  # Se agrega el valor del elemento a la fila
        resultado.append(fila)  # Se agrega la fila al resultado del producto de matrices

    return resultado  # Se devuelve la matriz resultado del producto


if __name__ == "__main__":
    filas = int(input("Ingrese la cantidad de filas: "))  # Se solicita ingresar el numero de filas de las matrices
    columnas = int(input("Ingrese la cantidad de columnas: "))  # Se solicita ingresar el numero de  columnas de las matrices
    matriz_1 = crear_matriz(filas, columnas)  # Se crea la matriz 1 con la función crear_matriz
    print("La matriz 1 es: " + str(matriz_1))  # Se imprime la matriz 1
    
    matriz2_ = crear_matriz2(filas, columnas)  # Se crea la matriz 2 con la función crear_matriz2
    print("La matriz 2 es: " + str(matriz2_))  # Se imprime la matriz 2
    

    matriz_producto = producto(matriz_1, matriz2_)  # Se crea la matriz producto con la función producto

    print("El producto de las matrices es:", str(matriz_producto))  # Se imprime la matriz producto

