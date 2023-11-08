from __future__ import annotations
from typing import Any
from builder.Pizza import Pizza
from abc import ABC, abstractmethod


class ConstructorPizzaCuatroQuesos(Pizza):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = PizzaCuatroQuesos()

    @property
    def product(self) -> PizzaCuatroQuesos:
        product = self._product
        self.reset()
        return product
    
    def pizza(self) -> PizzaCuatroQuesos:
        return self._product
    
    def nombre(self) -> None:
        return "Pizza Cuatro Quesos"
    
    def masa(self) -> None:
        self._product.add("Masa fina")

    def salsa_base(self) -> None:
        self._product.add("Salsa de tomate")

    def ingredientes(self) -> None:
        self._product.add("Queso mozzarella")
        self._product.add("Queso gorgonzola")
        self._product.add("Queso parmesano")
        self._product.add("Queso de cabra")

    def coccion(self) -> None:
        self._product.add("Horno")

    def presentacion(self) -> None:
        self._product.add("Pizza Cuatro Quesos")

    def maridaje(self) -> None:
        self._product.add("Vino tinto robusto")

    def extra(self) -> None:
        self._product.add("Aceitunas negras")


class PizzaCuatroQuesos():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)
    
    def list_parts(self) -> None:
        print(f"Pizza parts: {', '.join(self.parts)}", end="")
