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
import seaborn as sns
import matplotlib.ticker as ticker
from matplotlib.lines import Line2D
from dateutil.relativedelta import relativedelta
from datetime import datetime
from pandas.tseries.offsets import MonthEnd
import matplotlib.lines as mlines
import matplotlib.image as mpimg
import matplotlib.colors as mcolors

url = "https://www.bcra.gob.ar/Pdfs/PublicacionesEstadisticas/series.xlsm"
response = requests.get(url)

#Tasas = pd.read_excel(BytesIO(response.content), sheet_name='TASAS DE MERCADO', skiprows=8, usecols='A,I,O,S,T,V,X')
#Tasas.columns = ['fecha','TAMAR','TM20','Adelantos en cuenta corriente','Call entre Bancos Privados (BAIBAR)','Call','Pases']
Tasas = pd.read_excel(BytesIO(response.content), sheet_name='TASAS DE MERCADO', skiprows=8, usecols='A,I,R,S,V,X')

Tasas.columns = ['fecha','TAMAR','Préstamos personales','Adelantos en cuenta corriente','Call en Pesos','Repo a 1 día (excl. BCRA)']
Tasas.set_index('fecha', inplace=True)
Tasas = Tasas[Tasas.index>'2024-05-31']
Tasas.to_excel('Tasas.xlsx', index=True)
