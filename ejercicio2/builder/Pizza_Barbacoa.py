from __future__ import annotations
from typing import Any
from builder.Pizza import Pizza
from abc import ABC, abstractmethod


class ConstructorPizzaBarbacoa(Pizza):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = PizzaBarbacoa()

    @property
    def product(self) -> PizzaBarbacoa:
        product = self._product
        self.reset()
        return product
    
    def pizza(self) -> PizzaBarbacoa:
        return self._product
    
    def nombre(self) -> None:
        print("Pizza Barbacoa")
    
    def masa(self) -> None:
        self._product.add("Masa con especias")

    def salsa_base(self) -> None:
        self._product.add("Salsa barbacoa")

    def ingredientes(self) -> None:
        self._product.add("Queso cheddar")
        self._product.add("Pollo a la barbacoa")
        self._product.add("Cebolla roja")
        self._product.add("Cilantro fresco")

    def coccion(self) -> None:
        self._product.add("Horno")

    def presentacion(self) -> None:
        self._product.add("Pizza Barbacoa")

    def maridaje(self) -> None:
        self._product.add("Cerveza artesanal")

    def extra(self) -> None:
        self._product.add("Chiles picantes")


class PizzaBarbacoa():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)
    
    def list_parts(self) -> None:
        print(f"Pizza parts: {', '.join(self.parts)}", end="")
