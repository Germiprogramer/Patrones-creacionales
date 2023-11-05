import pandas as pd

# Cargamos el dataset

df = pd.read_csv('ejercicio1/datos/activaciones_samur_2022.csv', delimiter = ';')

# Convertir Meses a números
meses_dict = {
    'ENERO': 1, 'FEBRERO': 2, 'MARZO': 3, 'ABRIL': 4, 'MAYO': 5, 'JUNIO': 6,
    'JULIO': 7, 'AGOSTO': 8, 'SEPTIEMBRE': 9, 'OCTUBRE': 10, 'NOVIEMBRE': 11, 'DICIEMBRE': 12
}
df['Mes'] = df['Mes'].map(meses_dict)

# Convertir Hora Solicitud a valores numéricos
df['Hora Solicitud'] = pd.to_datetime(df['Hora Solicitud']).dt.hour * 60 + pd.to_datetime(df['Hora Solicitud']).dt.minute


