from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Pizza(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @property
    @abstractmethod
    def pizza(self) -> None:
        pass

    @abstractmethod
    def masa(self) -> None:
        pass

    @abstractmethod
    def salsa_base(self) -> None:
        pass

    @abstractmethod
    def ingredientes(self) -> None:
        pass

    @abstractmethod
    def coccion(self) -> None:
        pass

    @abstractmethod
    def presentacion(self) -> None:
        pass

    @abstractmethod
    def maridaje(self) -> None:
        pass

    @abstractmethod
    def extra(self) -> None:
        pass

class ConstructorPizzaMargherita(Pizza):

    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self.reset()

    def reset(self) -> None:
        self._product = PizzaMargherita()

    @property
    def product(self) -> PizzaMargherita:
        """
        Concrete Builders are supposed to provide their own methods for
        retrieving results. That's because various types of builders may create
        entirely different products that don't follow the same interface.
        Therefore, such methods cannot be declared in the base Builder interface
        (at least in a statically typed programming language).

        Usually, after returning the end result to the client, a builder
        instance is expected to be ready to start producing another product.
        That's why it's a usual practice to call the reset method at the end of
        the `getProduct` method body. However, this behavior is not mandatory,
        and you can make your builders wait for an explicit reset call from the
        client code before disposing of the previous result.
        """
        product = self._product
        self.reset()
        return product
    
    def pizza(self) -> PizzaMargherita:
        return self._product
    
    def masa(self) -> None:
        self._product.add("Masa")
    
    def salsa_base(self) -> None:
        self._product.add("Salsa base")
    
    def ingredientes(self) -> None:
        self._product.add("Queso mozzarella")
        self._product.add("Albahaca")
    
    def coccion(self) -> None:
        self._product.add("Horno")
    
    def presentacion(self) -> None:
        self._product.add("Pizza Margherita")
    
    def maridaje(self) -> None:
        self._product.add("Vino tinto")
    
    def extra(self) -> None:
        self._product.add("Aceite de oliva")
    
class PizzaMargherita():
    """
    It makes sense to use the Builder pattern only when your products are quite
    complex and require extensive configuration.

    Unlike in other creational patterns, different concrete builders can produce
    unrelated products. In other words, results of various builders may not
    always follow the same interface.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)
    
    def list_parts(self) -> None:
        print(f"Pizza parts: {', '.join(self.parts)}", end="")

class Director:

        def __init__(self) -> None:
            self._builder = None

        @property
        def builder(self) -> Pizza:
            return self._builder
        
        @builder.setter
        def builder(self, builder: Pizza) -> None:
            """
            The Director works with any builder instance that the client code
            passes to it. This way, the client code may alter the final type of
            the newly assembled product.
            """
            self._builder = builder

        
        def build_margherita(self) -> None:
            self.builder.masa()
            self.builder.salsa_base()
            self.builder.ingredientes()
            self.builder.coccion()
            self.builder.presentacion()
            self.builder.maridaje()
            self.builder.extra()

if __name__ == "__main__":
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """
    director = Director()
    builder = ConstructorPizzaMargherita()
    director.builder = builder

    print("Pizza Margherita")
    director.build_margherita()
    builder.product.list_parts()



