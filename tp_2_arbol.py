#!/usr/bin/env python
# coding: utf-8

class Nodo:
    def __init__(self, valor):
        # Inicialización de un nodo con un valor y sin hijos
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        
class Arbol:
    def __init__(self):
        # Inicialización de un árbol vacío sin raíz
        self.raiz = None

    def esta_vacio(self):
        # Verifica si el árbol está vacío (sin raíz)
        return self.raiz is None
    
    def __agregar_raiz(self, valor):
        self.raiz = Nodo(valor)        
        
    def __agregar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self.__agregar_recursivo(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self.__agregar_recursivo(nodo.derecha, valor)

    def __inorden_recursivo(self, nodo):
        if nodo is not None:
            self.__inorden_recursivo(nodo.izquierda)
            print(nodo.valor, end=", ")
            self.__inorden_recursivo(nodo.derecha)

    def __preorden_recursivo(self, nodo):
        if nodo is not None:
            print(nodo.valor, end=", ")
            self.__preorden_recursivo(nodo.izquierda)
            self.__preorden_recursivo(nodo.derecha)

    def __postorden_recursivo(self, nodo):
        if nodo is not None:
            self.__postorden_recursivo(nodo.izquierda)
            self.__postorden_recursivo(nodo.derecha)
            print(nodo.valor, end=", ")
            

    def __buscar(self, nodo, valor):
        if nodo is None:
            return None
        if nodo.valor == valor:
            return nodo
        if busqueda < nodo.valor:
            return self.__buscar(nodo.izquierda, valor)
        else:
            return self.__buscar(nodo.derecha, valor)
    
    def agregar_raiz(self, valor):
        self.__agregar_raiz(valor)
        
    def agregar(self, valor):
        self.__agregar_recursivo(self.raiz, valor)

    def buscar(self, valor):
        return self.__buscar(self.raiz, valor)

    def inorden(self):
        print("hijo izquierdo — raíz — hijo derecho")
        self.__inorden_recursivo(self.raiz)

    def preorden(self):
        print("raíz — hijo izquierdo — hijo derecho")
        self.__preorden_recursivo(self.raiz)

    def postorden(self):
        print("hijo izquierdo– hijo derecho — raíz")
        self.__postorden_recursivo(self.raiz)


    
if __name__ == "__main__":
    arbol = Arbol()

    while True:
        print("\nMenú:")
        print("0. Agregar raíz")
        print("1. Insertar elemento")
        print("2. Mostrar elementos (inorden)")
        print("3. Mostrar elementos (preorden)")
        print("4. Mostrar elementos (postorden)")
        print("5. Buscar elemento")
        print("6. Salir")

        opcion = input("Ingrese una opción: ")
        if opcion == "0":
            elemento = int(input("Ingrese elemento raiz: "))
            arbol.agregar_raiz(elemento)
        elif opcion == "1":
            elemento = int(input("Ingrese un elemento: "))
            arbol.agregar(elemento)
        elif opcion == "2":
            print("Elementos (inorden):")
            arbol.inorden()
        elif opcion == "3":
            print("Elementos (preorden):")
            arbol.preorden()
        elif opcion == "4":
            print("Elementos (postorden):")
            arbol.postorden()
        elif opcion == "5":
            elemento = int(input("Ingrese el elemento a buscar: "))
            if arbol.buscar(elemento):
                print(f"El elemento {elemento} está en el árbol.")
            else:
                print(f"El elemento {elemento} no está en el árbol.")
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Intente nuevamente.")