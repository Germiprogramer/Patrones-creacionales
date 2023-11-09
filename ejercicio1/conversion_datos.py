import pandas as pd
from abstract_factory import *



def conversion_datos(datos):
    meses_dict = {
        'ENERO': 1, 'FEBRERO': 2, 'MARZO': 3, 'ABRIL': 4, 'MAYO': 5, 'JUNIO': 6,
        'JULIO': 7, 'AGOSTO': 8, 'SEPTIEMBRE': 9, 'OCTUBRE': 10, 'NOVIEMBRE': 11, 'DICIEMBRE': 12
    }
    datos['Mes'] = datos['Mes'].map(meses_dict)

    datos['Hora Solicitud'] = pd.to_datetime(datos['Hora Solicitud']).dt.hour * 60 + pd.to_datetime(datos['Hora Solicitud']).dt.minute
    datos['Hora Intervención'] = pd.to_datetime(datos['Hora Intervención']).dt.hour * 60 + pd.to_datetime(datos['Hora Intervención']).dt.minute




    


