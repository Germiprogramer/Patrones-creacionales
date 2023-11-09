import pandas as pd
from abstract_factory import *
from conversion_datos import conversion_datos


if __name__ == "__main__":
    df = pd.read_csv('ejercicio1/datos/activaciones_samur_2022.csv', delimiter=';')
    conversion_datos(df)

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
    print('\nGráfico Hora Solicitud')
    client_code_grafico(factory_hora_solicitud)
    print('\nGráfico Hora Intervención')
    client_code_grafico(factory_hora_intervencion)
    print('\nGráfico Mes')
    client_code_grafico(factory_mes)
