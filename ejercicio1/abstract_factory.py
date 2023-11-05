from __future__ import annotations
from abc import ABC, abstractmethod
import pandas as pd

class AbstractFactory(ABC):

    def __init__(self, datos):
        self.datos = datos

    @abstractmethod
    def moda(self) -> AbstractModa:
        pass

    @abstractmethod
    def media(self) -> AbstractMedia:
        pass

class ConcreteFactory_HoraSolicitud(AbstractFactory):

    def moda(self) -> AbstractModa:
        return ConcreteModa_HoraSolicitud(self.datos)

    def media(self) -> AbstractMedia:
        return ConcreteMedia_HoraSolicitud(self.datos)

class ConcreteFactory_HoraIntervencion(AbstractFactory):

    def moda(self) -> AbstractModa:
        return ConcreteModa_HoraIntervencion(self.datos)

    def media(self) -> AbstractMedia:
        return ConcreteMedia_HoraIntervencion(self.datos)

class ConcreteFactory_Mes(AbstractFactory):

    def moda(self) -> AbstractModa:
        return ConcreteModa_Mes(self.datos)

    def media(self) -> AbstractMedia:
        return ConcreteMedia_Mes(self.datos)

class AbstractModa(ABC):
    @abstractmethod
    def calcular(self) -> pd.Series:
        pass

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

class AbstractMedia(ABC):
    @abstractmethod
    def calcular(self) -> pd.Series:
        pass

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

def client_code_moda(factory: AbstractFactory) -> None:
    moda = factory.moda()
    
    print(f'Moda: {moda.calcular()}')
    
def client_code_media(factory: AbstractFactory) -> None:
    media = factory.media()
    
    print(f'Moda: {media.calcular()}')
    


if __name__ == "__main__":
    df = pd.read_csv('ejercicio1/datos/activaciones_samur_2022.csv', delimiter=';')

    meses_dict = {
        'ENERO': 1, 'FEBRERO': 2, 'MARZO': 3, 'ABRIL': 4, 'MAYO': 5, 'JUNIO': 6,
        'JULIO': 7, 'AGOSTO': 8, 'SEPTIEMBRE': 9, 'OCTUBRE': 10, 'NOVIEMBRE': 11, 'DICIEMBRE': 12
    }
    df['Mes'] = df['Mes'].map(meses_dict)

    df['Hora Solicitud'] = pd.to_datetime(df['Hora Solicitud']).dt.hour * 60 + pd.to_datetime(df['Hora Solicitud']).dt.minute
    df['Hora Intervención'] = pd.to_datetime(df['Hora Intervención']).dt.hour * 60 + pd.to_datetime(df['Hora Intervención']).dt.minute

    factory_hora_solicitud = ConcreteFactory_HoraSolicitud(df)
    factory_hora_intervencion = ConcreteFactory_HoraIntervencion(df)
    factory_mes = ConcreteFactory_Mes(df)

    print('Hora Solicitud')
    client_code_moda(factory_hora_solicitud)
    client_code_media(factory_hora_solicitud)
    print('\nHora Intervención')
    client_code_moda(factory_hora_intervencion)
    client_code_media(factory_hora_intervencion)
    print('\nMes')
    client_code_moda(factory_mes)
    client_code_media(factory_mes)
