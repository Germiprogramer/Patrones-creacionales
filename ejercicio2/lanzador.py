from builder.Director import *

if __name__ == "__main__":
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """
    director = Director()
    builder = ConstructorPizzaBarbacoa()
    director.builder = builder

    
    director.build()
    builder.product.list_parts()