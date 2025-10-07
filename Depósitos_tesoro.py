import requests
import pandas as pd
import numpy as np
from datetime import timedelta
from datetime import datetime
import datetime
from io import BytesIO
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib.lines import Line2D
from dateutil.relativedelta import relativedelta
from datetime import datetime
from pandas.tseries.offsets import MonthEnd
import matplotlib.lines as mlines
import matplotlib.image as mpimg

hasta = hasta = pd.Timestamp.today()
url = "https://www.bcra.gob.ar/Pdfs/PublicacionesEstadisticas/diar_bas.xls"
response = requests.get(url, verify=False)
diar_bas = pd.read_excel(BytesIO(response.content), 
                         sheet_name='Serie_diaria', 
                         skiprows=26, 
                         usecols='A,AF,AG,AI')
diar_bas.columns = ['fecha', 'Depósitos del tesoro en pesos', 'Depósitos_del_tesoro_en_usd', 
                    'TC']
diar_bas.set_index('fecha', inplace=True)
diar_bas = diar_bas.iloc[:-3]
diar_bas = diar_bas[(diar_bas.index > pd.Timestamp('2024-12-31')) & (diar_bas.index <= diar_bas.index[-1])]
diar_bas['Depósitos del tesoro en usd'] = diar_bas['Depósitos_del_tesoro_en_usd'] / diar_bas['TC']
diar_bas = diar_bas[['Depósitos del tesoro en pesos', 'Depósitos del tesoro en usd']]
diar_bas = diar_bas.round(2)

diar_bas_var = diar_bas.diff()
diar_bas_var = diar_bas_var.round(2)
diar_bas_var = diar_bas_var.iloc[1:]
diar_bas_var = diar_bas_var[::-1]
diar_bas_var.to_csv('Depósitos_tesoro_variación_diaria.csv', index=True)

diar_bas = diar_bas[::-1]
diar_bas.to_csv('Depósitos_tesoro.csv', index=True)







