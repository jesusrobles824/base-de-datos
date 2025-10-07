import pandas as pd
from datetime import timedelta
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.patches as mpatches
from datetime import datetime
import datetime             
import matplotlib.image as mpimg
import requests
import numpy as np
import requests
from io import BytesIO

url = "https://www.bcra.gob.ar/Pdfs/PublicacionesEstadisticas/series.xlsm"
response = requests.get(url, verify=False)
Variacion_Reservas = pd.read_excel(BytesIO(response.content), sheet_name='RESERVAS', skiprows=8, usecols='A,G,H,I,J,K,L,Q')
Variacion_Reservas.columns = ['fecha', 'Reservas Internacionales', 'Compra de Divisas', 'OOII', 'Otras Operaciones del SP', 'Efectivo Mínimo', 'Otros (incl. pases pasivos en USD con el exterior)', 'Tipo de serie']
Variacion_Reservas = Variacion_Reservas.loc[Variacion_Reservas["Tipo de serie"] == "D"]
Variacion_Reservas.set_index('fecha', inplace=True)
Variacion_Reservas = Variacion_Reservas.drop(columns=['Tipo de serie'])
Variacion_Reservas = Variacion_Reservas[Variacion_Reservas.index>'2023-12-10']
Variacion_Acumulada = Variacion_Reservas.cumsum()

Variacion_Reservas = Variacion_Reservas.round(1)
Variacion_Reservas = Variacion_Reservas[::-1]
Variacion_Reservas.to_csv('Variación_RRII_Factores_Explicación.csv',index=True)

Variacion_Acumulada = Variacion_Acumulada.round(1)
Variacion_Acumulada = Variacion_Acumulada[::-1]
Variacion_Acumulada.to_csv('Variación_Acumulada_RRII_Factores_Explicación')