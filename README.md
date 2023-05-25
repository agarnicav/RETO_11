# RETO_11

## Primer punto 
Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

### Codigo: 

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
        
        
    def Suma_matrices(matriz_1, matriz2_) -> list: # Se define una función para la suma de matrices
        filas = len(matriz_1)  # Obtiene la cantidad de filas de la matriz 1
        columnas = len(matriz_1[0])  # Obtiene la cantidad de columnas de la matriz 1 
        resultado = []  # Se crea una lista vacía para almacenar el resultado de la suma de matrices
    
        for i in range(filas):  # Se itera sobre las filas de las matrices
            fila = []  # Se crea una lista vacía para almacenar los valores de la fila actual del resultado
            for j in range(columnas):  # Se itera sobre las columnas de las matrices
                suma = matriz_1[i][j] + matriz2_[i][j]  # Se realiza la suma de los valore de las dos matrices
                fila.append(suma)  # Se agrega el valor de la suma a la lista de la fila
            resultado.append(fila)  # Se agrega la lista fila  a la matriz resultado de la suma de matrices

        return resultado  # Devuelve la matriz resultado de la suma


    def Resta_matrices(matriz_1, matriz2_) -> list:  # Se define una función para la resta de matrices
        filas = len(matriz_1)  # Obtiene la cantidad de filas de la matriz 1
        columnas = len(matriz_1[0])  # Obtiene la cantidad de columnas de la matriz 1 
        resultado2 = []  # Se crea una lista vacía para almacenar el resultado de la resta de matrices
    
        for i in range(filas):  # Itera sobre las filas de las matrices
            fila = []  # Crea una lista vacía para almacenar los valores de la fila actual del resultado
            for j in range(columnas):  #  Se itera sobre las columnas de las matrices
                resta = matriz_1[i][j] - matriz2_[i][j]  # Se realiza la resta de los valores correspondientes de las dos matrices
                fila.append(resta)  # Se agrega el valor de la resta a la fila
           resultado2.append(fila)  # # Se agrega la lista fila  a la matriz resultado de la  resta de matrices
    
       return resultado2  # Devuelve la matriz resultado de la resta


    if __name__ == "__main__":
        filas = int(input("Ingrese la cantidad de filas: "))  # Se solicita ingresar el numero de filas de las matrices
        columnas = int(input("Ingrese la cantidad de columnas: "))  # Se solicita ingresar el numero de  columnas de las matrices
        matriz_1 = crear_matriz(filas, columnas)  # Se crea la matriz 1 con la función crear_matriz
        print("La matriz 1 es: " + str(matriz_1))  # Se imprime la matriz 1
    
        matriz2_ = crear_matriz2(filas, columnas)  # Se crea la matriz 2 con la función crear_matriz2
        print("La matriz 2 es: " + str(matriz2_))  # Se imprime la matriz 2
    
        suma_matrices = Suma_matrices(matriz_1, matriz2_)  # Se realiza la suma de las matrices con la función Suma_matrices
    
        print("La suma de las matrices es : " + str(suma_matrices))  # Se imprime la suma de las matrices
    
        resta_matrices = Resta_matrices(matriz_1, matriz2_)  # Se realiza la resta de las matrices con la función Resta_matrices
    
        print("La resta de las matrices es: " + str(resta_matrices))  # Se imprime la resta de las matrices

        
   ## Segundo Punto
   Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación
   
   ### Codigo: 
     
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
        
        
        
## Tercer Punto: 
Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.

    def crear_matriz(filas, columnas) -> list: # Se define la función para crear una matriz dando los agumentos de filas y columnas 
        matriz = []  # Se crea una lista vacía para almacenar los valores de la matriz
        for i in range(filas):  # Se itera sobre el rango de filas
            fila = []  # Se crea una lista vacía para almacenar los valores de la fila actual
            for j in range(columnas):  # Se itera sobre el rango de columnas
               valor = float(input("Insertar valor para la posición: "))  # Se solicita ingresar un valor para la posición en la que se encuentra 
                fila.append(valor)  # Agrega el valor ingresado a la fila
            matriz.append(fila)  # Agrega la fila a la matriz
        return matriz  # Devuelve la matriz completa como una lista de listas



    def matriz_transpuesta(matriz):
        filas = len(matriz)  # Se obtiene la cantidad de filas de la matriz con la función len
        columnas = len(matriz[0])  # Se obtiene la cantidad de columnas de la matriz con la función len(
    
        if columnas != filas:  # Verifica si las matriz tiene la misma cantidad de filas y columnas si son difenrentes no se puede realizar la matriz transpuesta 
            print("No es posible realizar la matriz transpuesta.") # se impre el mensaje si es diferente 
    
        else: # sino son valores distintos : 
            matriz_trans = []  # Se creara una lista vacía para almacenar la matriz transpuesta
        
            for j in range(columnas):  # Se itera sobre las columnas de la matriz 
                fila = []  # Se crea una lista vacía para almacenar los valores de la fila actual de la matriz transpuesta
                for i in range(filas):  # Se itera sobre las filas de la matriz 
                    fila.append(matriz[i][j])  # Se agrega el valor transpuesto a la fila
               matriz_trans.append(fila)  # Se agrega la fila a la matriz transpuesta
        
            return matriz_trans  # Se devuelve la matriz transpuesta 


    if __name__ == "__main__":
        filas = int(input("Ingrese la cantidad de filas: "))  # Se solicita ingresar el numero de filas de las matrices
        columnas = int(input("Ingrese la cantidad de columnas: "))  # Se solicita ingresar el numero de  columnas de las matrices
        matriz_1 = crear_matriz(filas, columnas)  # Se crea la matriz con la función crear_matriz
        print("La matriz 1 es: " + str(matriz_1))  # Se imprime la matriz 
        matriz_transpuesta_ = matriz_transpuesta(matriz_1) # Se crea la matriz transpuesta llmando a la función natriz transpuesta
        print("La matriz transpuesta es:", str(matriz_transpuesta_))  # Se imprime la matriz transpuesta
        
        
# Cuaarto Punto 
Desarrollar un programa que sume los elementos de una columna dada de una matriz.
