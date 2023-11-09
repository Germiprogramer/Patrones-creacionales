from __future__ import annotations
from abc import ABC, abstractmethod
import pandas as pd
import matplotlib.pyplot as plt
import os

# Define una clase abstracta para las fábricas de análisis estadístico
class AbstractFactory(ABC):

    def __init__(self, datos):
        self.datos = datos

    @abstractmethod
    def moda(self) -> AbstractModa:
        pass

    @abstractmethod
    def media(self) -> AbstractMedia:
        pass

    @abstractmethod
    def grafico(self) -> AbstractGrafico:
        pass

# Define clases concretas para las fábricas de análisis estadístico de 'Hora Solicitud', 'Hora Intervención' y 'Mes'
class ConcreteFactory_HoraSolicitud(AbstractFactory):

    def moda(self) -> AbstractModa:
        return ConcreteModa_HoraSolicitud(self.datos)

    def media(self) -> AbstractMedia:
        return ConcreteMedia_HoraSolicitud(self.datos)
    
    def grafico(self) -> AbstractGrafico:
        return ConcreteGrafico_HoraSolicitud(self.datos)

class ConcreteFactory_HoraIntervencion(AbstractFactory):

    def moda(self) -> AbstractModa:
        return ConcreteModa_HoraIntervencion(self.datos)

    def media(self) -> AbstractMedia:
        return ConcreteMedia_HoraIntervencion(self.datos)
    
    def grafico(self) -> AbstractGrafico:
        return ConcreteGrafico_HoraIntervencion(self.datos)

class ConcreteFactory_Mes(AbstractFactory):

    def moda(self) -> AbstractModa:
        return ConcreteModa_Mes(self.datos)

    def media(self) -> AbstractMedia:
        return ConcreteMedia_Mes(self.datos)
    
    def grafico(self) -> AbstractGrafico:
        return ConcreteGrafico_Mes(self.datos)

# Define clases abstractas para calcular la moda
class AbstractModa(ABC):
    @abstractmethod
    def calcular(self) -> pd.Series:
        pass

# Define clases concretas para calcular la moda de 'Hora Solicitud', 'Hora Intervención' y 'Mes'
class ConcreteModa_HoraSolicitud(AbstractModa):
    def __init__(self, datos):
        self.datos = datos

    def calcular(self) -> pd.Series:
        return self.datos['Hora Solicitud'].mode()

class ConcreteModa_HoraIntervencion(AbstractModa):
    def __init__(self, datos):
        self.datos = datos

    def calcular(self) -> pd.Series:
        return self.datos['Hora Intervención'].mode()

class ConcreteModa_Mes(AbstractModa):
    def __init__(self, datos):
        self.datos = datos

    def calcular(self) -> pd.Series:
        return self.datos['Mes'].mode()

# Define clases abstractas para calcular la media
class AbstractMedia(ABC):
    @abstractmethod
    def calcular(self) -> pd.Series:
        pass

# Define clases concretas para calcular la media de 'Hora Solicitud', 'Hora Intervención' y 'Mes'
class ConcreteMedia_HoraSolicitud(AbstractMedia):
    def __init__(self, datos):
        self.datos = datos

    def calcular(self) -> pd.Series:
        return self.datos['Hora Solicitud'].mean()

class ConcreteMedia_HoraIntervencion(AbstractMedia):
    def __init__(self, datos):
        self.datos = datos

    def calcular(self) -> pd.Series:
        return self.datos['Hora Intervención'].mean()

class ConcreteMedia_Mes(AbstractMedia):
    def __init__(self, datos):
        self.datos = datos

    def calcular(self) -> pd.Series:
        return self.datos['Mes'].mean()

# Define clases abstractas para generar gráficos
class AbstractGrafico(ABC):
    @abstractmethod
    def generar_grafico(self) -> None:
        pass


# Define clases concretas para generar gráficos de 'Hora Solicitud', 'Hora Intervención' y 'Mes'
class ConcreteGrafico_HoraSolicitud(AbstractGrafico):
    def __init__(self, datos):
        self.datos = datos

    def generar_grafico(self) -> None:
        plt.hist(self.datos['Hora Solicitud'], bins=30, alpha=0.7, color='b', label='Hora Solicitud')
        plt.xlabel('Hora (en minutos)')
        plt.ylabel('Frecuencia')
        plt.title('Histograma - Hora Solicitud')
        plt.legend(loc='upper right')
        plt.show()
        plt.savefig(os.path.join('ejercicio1/graficos', 'grafico_hora_solicitud.png'))  # Guarda el gráfico en la carpeta "grafos"
        plt.close()

class ConcreteGrafico_HoraIntervencion(AbstractGrafico):
    def __init__(self, datos):
        self.datos = datos

    def generar_grafico(self) -> None:
        plt.hist(self.datos['Hora Intervención'], bins=30, alpha=0.7, color='g', label='Hora Intervención')
        plt.xlabel('Hora (en minutos)')
        plt.ylabel('Frecuencia')
        plt.title('Histograma - Hora Intervención')
        plt.legend(loc='upper right')
        plt.show()
        plt.savefig(os.path.join('ejercicio1/graficos', 'grafico_hora_intervencion.png'))  # Guarda el gráfico en la carpeta "grafos"
        plt.close()

class ConcreteGrafico_Mes(AbstractGrafico):
    def __init__(self, datos):
        self.datos = datos

    def generar_grafico(self) -> None:
        counts = self.datos['Mes'].value_counts()
        counts.plot(kind='bar', color='orange')
        plt.xlabel('Mes')
        plt.ylabel('Frecuencia')
        plt.title('Gráfico de Barras - Mes')
        plt.show()
        plt.savefig(os.path.join('ejercicio1/graficos', 'grafico_mes.png'))  # Guarda el gráfico en la carpeta "grafos"
        plt.close()

# Define una clase cliente para construir objetos complejos paso a paso
def client_code_moda(factory: AbstractFactory) -> None:
    moda = factory.moda()
    
    print(f'Moda: {moda.calcular()}')
    
def client_code_media(factory: AbstractFactory) -> None:
    media = factory.media()
    
    print(f'Media: {media.calcular()}')

def client_code_grafico(factory: AbstractFactory) -> None:
    grafico = factory.grafico()
    
    grafico.generar_grafico()
