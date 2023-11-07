from __future__ import annotations
from typing import Any
from builder.Pizza import Pizza
from abc import ABC, abstractmethod


class ConstructorPizzaHawaiana(Pizza):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = PizzaHawaiana()



    @property
    def product(self) -> PizzaHawaiana:
        product = self._product
        self.reset()
        return product
    
    def pizza(self) -> PizzaHawaiana:
        return self._product
    
    def nombre(self) -> None:
        print("Pizza Hawaiana")

    def masa(self) -> None:
        self._product.add("Masa")

    def salsa_base(self) -> None:
        self._product.add("Salsa de tomate")

    def ingredientes(self) -> None:
        self._product.add("Queso mozzarella")
        self._product.add("Jamón")
        self._product.add("Piña")

    def coccion(self) -> None:
        self._product.add("Horno")

    def presentacion(self) -> None:
        self._product.add("Pizza Hawaiana")

    def maridaje(self) -> None:
        self._product.add("Vino blanco")

    def extra(self) -> None:
        self._product.add("Aceite de oliva")


class PizzaHawaiana():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)
    
    def list_parts(self) -> None:
        print(f"Pizza parts: {', '.join(self.parts)}", end="")
