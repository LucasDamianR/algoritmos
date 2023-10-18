#!/usr/bin/env python
# coding: utf-8

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar(self):
        valores = []
        actual = self.cabeza
        while actual:
            valores.append(actual.valor)
            actual = actual.siguiente
        return valores
    
    def pedir_cantidad_elementos(self):
        """
        Pedir al usuario la cantidad de elementos y 
        luego vaya ingresando esos elementos en la lista.        
        """
        n = int(input("Ingrese la cantidad de elementos: "))
        # Solicitar al usuario ingresar los elementos y agregarlos a la lista
        for _ in range(n):
            valor = int(input("Ingrese un elemento: "))
            self.agregar(valor)

    def agregar_al_inicio(self):
        """
        Insertar un elemento al principio de la lista
        """
        valor = int(input("Ingrese un elemento al inicio de la lista: "))
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def agregar_al_final(self):
        """
        Insertar un elemento al final de la lista
        """
        valor = int(input("Ingrese un elemento al final de la lista: "))
        self.agregar(valor)

        
    def insertar_despues_de(self, valor_anterior, nuevo_valor):
        """
        Insertar un elemento después de uno indicado por el usuario
        """
        nuevo_nodo = Nodo(nuevo_valor)
        actual = self.cabeza
        while actual:
            if actual.valor == valor_anterior:
                nuevo_nodo.siguiente = actual.siguiente
                actual.siguiente = nuevo_nodo
                return
            actual = actual.siguiente

    def insertar_antes_de(self, valor_despues_de, nuevo_valor):
        """
        Insertar un elemento antes de uno indicado por el usuario
        """
        nuevo_nodo = Nodo(nuevo_valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        if self.cabeza.valor == valor_despues_de:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
            return
        previo = None
        actual = self.cabeza
        while actual and actual.valor != valor_despues_de:
            previo = actual
            actual = actual.siguiente
        if actual:
            previo.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = actual

    def insertar_en_posicion(self, posicion, nuevo_valor):
        """
        Insertar un elemento en una posición específica
        """
        nuevo_nodo = Nodo(nuevo_valor)
        if posicion == 0:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        contador = 0
        while actual and contador < posicion - 1:
            actual = actual.siguiente
            contador += 1
        if actual:
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo
        else:
            print("Posición fuera de rango.")
            
    def contar(self):
        """
        Contar los elementos de la lista
        """
        return len(self.mostrar())
    
    def buscar(self, valor):
        """
        Buscar un elemento de la lista
        """
        actual = self.cabeza
        posicion = 0
        while actual:
            if actual.valor == valor:
                return posicion
            actual = actual.siguiente
            posicion += 1
        return -1  # Valor no encontrado
    
    def eliminar_inicio(self):
        """
        Eliminar un elemento desde el principio de la lista
        """
        if self.cabeza:
            self.cabeza = self.cabeza.siguiente

    def eliminar_final(self):
        """
        Eliminar un elemento del final de la lista
        """
        if self.cabeza is None:
            return  # La lista está vacía
        if self.cabeza.siguiente is None:
            self.cabeza = None  # Hay solo un elemento en la lista
            return
        actual = self.cabeza
        while actual.siguiente.siguiente:
            actual = actual.siguiente
        actual.siguiente = None
   
    def eliminar_por_valor(self, valor):
        """
        Eliminar un elemento según el valor ingresado
        """
        if self.cabeza is None:
            return  # La lista está vacía
        if self.cabeza.valor == valor:
            self.cabeza = self.cabeza.siguiente
            return
        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.valor == valor:
                actual.siguiente = actual.siguiente.siguiente
                return
            actual = actual.siguiente
            
# Crear una lista enlazada vacía
mi_lista = ListaEnlazada()
mi_lista.pedir_cantidad_elementos()
mi_lista.agregar_al_inicio()
mi_lista.agregar_al_final()

# Solicitar al usuario el valor después del cual desea insertar un nuevo elemento
valor_anterior = int(input("Ingrese el valor después del cual desea insertar un nuevo elemento: "))
nuevo_valor = int(input("Ingrese el nuevo valor a insertar: "))
# Insertar el nuevo elemento después del valor indicado por el usuario
mi_lista.insertar_despues_de(valor_anterior, nuevo_valor)

# Solicitar al usuario el valor antes del cual desea insertar un nuevo elemento
valor_despues_de = int(input("Ingrese el valor antes del cual desea insertar un nuevo elemento: "))
nuevo_valor = int(input("Ingrese el nuevo valor a insertar: "))
# Insertar el nuevo elemento antes del valor indicado por el usuario
mi_lista.insertar_antes_de(valor_despues_de, nuevo_valor)

# Solicitar al usuario la posición en la que desea insertar un nuevo elemento
posicion = int(input("Ingrese la posición en la que desea insertar un nuevo elemento: "))
nuevo_valor = int(input("Ingrese el nuevo valor a insertar: "))
# Insertar el nuevo elemento en la posición indicada por el usuario
mi_lista.insertar_en_posicion(posicion, nuevo_valor)

# Mostrar los elementos de la lista
print("Elementos en la lista enlazada:", mi_lista.mostrar())
# Contar los elementos de la lista
print(f"Cantidad de elementos de la lista: {mi_lista.contar()}")
# Solicitar al usuario el valor que desea buscar
valor_a_buscar = int(input("Ingrese el valor que desea buscar: "))
# Buscar el valor en la lista
posicion = mi_lista.buscar(valor_a_buscar)
if posicion != -1:
    print(f"El valor {valor_a_buscar} se encuentra en la posición {posicion}.")
else:
    print(f"El valor {valor_a_buscar} no se encuentra en la lista.")
    

# Eliminar el primer elemento de la lista
mi_lista.eliminar_inicio()
# Eliminar el último elemento de la lista
mi_lista.eliminar_final()
# Solicitar al usuario el valor que desea eliminar
valor_a_eliminar = int(input("Ingrese el valor que desea eliminar: "))
# Eliminar el valor de la lista
mi_lista.eliminar_por_valor(valor_a_eliminar)
# Mostrar lista final
print("Elementos en la lista enlazada:", mi_lista.mostrar())