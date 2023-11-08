from __future__ import annotations
from typing import Any
from builder.Pizza import Pizza
from abc import ABC, abstractmethod

class ConstructorPizzaPersonalizada(Pizza):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = PizzaPersonalizada()

    def nombre(self) -> None:
        nombre = input("Escribe el nombre de tu pizza: ")
        return nombre

    @property
    def product(self) -> PizzaPersonalizada:
        product = self._product
        self.reset()
        return product
    
    def pizza(self) -> PizzaPersonalizada:
        return self._product
    
    def masa(self) -> None:
        masa = input("Elige el tipo de masa (fina, normal, gruesa): ")
        self._product.add(f"Masa: {masa}")

    def salsa_base(self) -> None:
        salsa = input("Elige el tipo de salsa base (tomate, barbacoa, blanca): ")
        self._product.add(f"Salsa base: {salsa}")

    def ingredientes(self) -> None:
        while True:
            ingrediente = input("Agrega un ingrediente (o escribe 'fin' para terminar): ")
            if ingrediente.lower() == 'fin':
                break
            self._product.add(f"Ingrediente: {ingrediente}")

    def coccion(self) -> None:
        coccion = input("Elige el tipo de cocción (horno, parrilla, leña): ")
        self._product.add(f"Cocción: {coccion}")

    def presentacion(self) -> None:
        presentacion = input("Elige el tipo de presentación (tradicional, cuadrada, personalizada): ")
        self._product.add(f"Presentación: {presentacion}")

    def maridaje(self) -> None:
        maridaje = input("Elige el tipo de maridaje (vino, cerveza, refresco): ")
        self._product.add(f"Maridaje: {maridaje}")

    def extra(self) -> None:
        extra = input("Agrega un extra (o escribe 'ninguno' para omitir): ")
        if extra.lower() != 'ninguno':
            self._product.add(f"Extra: {extra}")


class PizzaPersonalizada():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)
    
    def list_parts(self) -> None:
        print(f"Pizza parts: {', '.join(self.parts)}", end="")
