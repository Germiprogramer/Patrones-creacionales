# Importa la biblioteca pandas para manejar datos en forma de DataFrames
import pandas as pd

# Importa las clases y funciones necesarias del módulo abstract_factory y conversion_datos
from abstract_factory import *
from conversion_datos import conversion_datos

# Verifica si el script está siendo ejecutado directamente
if __name__ == "__main__":
    # Lee el archivo CSV 'activaciones_samur_2022.csv' y carga los datos en un DataFrame llamado df
    df = pd.read_csv('ejercicio1/datos/activaciones_samur_2022.csv', delimiter=';')
    
    # Llama a la función conversion_datos para realizar alguna operación de procesamiento en el DataFrame df
    conversion_datos(df)

    # Crea instancias de las clases concretas para las fábricas de análisis estadístico
    factory_hora_solicitud = ConcreteFactory_HoraSolicitud(df)
    factory_hora_intervencion = ConcreteFactory_HoraIntervencion(df)
    factory_mes = ConcreteFactory_Mes(df)

    # Realiza análisis estadístico y muestra los resultados para la variable 'Hora Solicitud'
    print('Hora Solicitud')
    client_code_moda(factory_hora_solicitud)  # Calcula y muestra la moda
    client_code_media(factory_hora_solicitud)  # Calcula y muestra la media
    
    # Realiza análisis estadístico y muestra los resultados para la variable 'Hora Intervención'
    print('\nHora Intervención')
    client_code_moda(factory_hora_intervencion)  # Calcula y muestra la moda
    client_code_media(factory_hora_intervencion)  # Calcula y muestra la media
    
    # Realiza análisis estadístico y muestra los resultados para la variable 'Mes'
    print('\nMes')
    client_code_moda(factory_mes)  # Calcula y muestra la moda
    client_code_media(factory_mes)  # Calcula y muestra la media
    
    # Genera y muestra gráficos para la variable 'Hora Solicitud', 'Hora Intervención' y 'Mes'
    print('\nGráfico Hora Solicitud')
    client_code_grafico(factory_hora_solicitud)  # Genera y muestra el histograma para 'Hora Solicitud'
    print('\nGráfico Hora Intervención')
    client_code_grafico(factory_hora_intervencion)  # Genera y muestra el histograma para 'Hora Intervención'
    print('\nGráfico Mes')
    client_code_grafico(factory_mes)  # Genera y muestra el gráfico de barras para 'Mes'
