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
response = requests.get(url, verify=False)

Tasas = pd.read_excel(BytesIO(response.content), sheet_name='TASAS DE MERCADO', skiprows=8, usecols='A,I,R,S,V,X')

Tasas.columns = ['fecha','TAMAR','Préstamos personales','Adelantos en cuenta corriente','Call en Pesos','Repo a 1 día (excl. BCRA)']
Tasas.set_index('fecha', inplace=True)
Tasas = Tasas[Tasas.index>'2024-05-31']
Tasas.to_excel('Tasas.xlsx', index=True)

meses = [
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
]
mes_nombre = meses[Tasas.index[-1].month - 1]

ultimo = Tasas.index[-1].date()
mes = ultimo.month
fin_mes = (ultimo + pd.offsets.MonthEnd(0)).date()
ultimo = ultimo.strftime('%d-%m-%Y')

# Establecer el estilo
sns.set(style='white')
plt.figure(figsize=(12,8))
#colors = ["#004F95", "#34984F", "#F39425", "#B25DA1", "#62A0B6", "#08754F"] 
#colors = ["#004F95", "#37AAAA", "#F39425", "#B25DA1", "#7E8FC1", "#08754F"] 
colors = ['#37AAAA',"#004F95","#F39425","#B25DA1","#08754F"] 

# Crear una lista de patches
patches = []
for i, columna in enumerate(Tasas.columns):
    # Graficar cada línea
    plt.plot(Tasas.index, Tasas[columna], 
             linewidth=2, label=columna, color=colors[i])
    last_val = Tasas[columna].iloc[-1]
    # Crear un patch para la leyenda con el color de la línea
    patches.append(mpatches.Patch(color=colors[i], label=f"{columna} ({last_val:,.1f})"))
    # Obtener el último valor y la última fecha
    last_value = Tasas[columna].iloc[-1]
    last_date = Tasas.index[-1]
    # Mover el último valor 10 días a la derecha (ajustar la fecha)
    adjusted_date = last_date + pd.Timedelta(days=2)
    # Graficar el valor ajustado en el gráfico (con 1 decimal) solo si no es uno de los casos anteriores
    #if columna == 'Call Total':
    # plt.text(adjusted_date, last_value-1, f'{last_value:.1f}', 
    #         color=colors[i], fontsize=15, ha='left', va='bottom', weight='bold')
    #elif columna == 'Call entre Bancos Privados (BAIBAR)':
    # plt.text(adjusted_date, last_value-1, f'{last_value:.1f}', 
    #         color=colors[i], fontsize=15, ha='left', va='bottom', weight='bold')
    #elif columna == 'Adelantos en cuenta corriente':
    # plt.text(adjusted_date, last_value, f'{last_value:.1f}', 
    #         color=colors[i], fontsize=15, ha='left', va='bottom', weight='bold')
    #elif columna == 'TAMAR Total':
    # plt.text(adjusted_date, last_value-1.3, f'{last_value:.1f}', 
    #         color=colors[i], fontsize=15, ha='left', va='bottom', weight='bold')
    #elif columna == 'TAMAR Bancos Privados':
    # plt.text(adjusted_date, last_value+0.4, f'{last_value:.1f}', 
    #         color=colors[i], fontsize=15, ha='left', va='bottom', weight='bold')
    #else:
    # plt.text(adjusted_date, last_value, f'{last_value:.1f}', 
    #         color=colors[i], fontsize=15, ha='left', va='bottom', weight='bold')
plt.suptitle('Tasas de interés', fontsize=28, color='#004F95', weight='bold', x=0.175, y=0.966)
plt.title(f'TNA (%) de las principales tasas de mercado. Período junio 2024 a {mes_nombre} 2025.', fontsize=16, color='black', alpha=0.75, pad=80, x=0.44)
plt.gca().set_xticks([])
plt.xlabel(f'Fuente: Jesús Robles en base a BCRA. En paréntesis TNA (%) al {ultimo}.', labelpad=30, fontsize=11.5, x=0.25)
plt.xlim(pd.Timestamp('2024-06-01'), fin_mes)
for year in range(2024,2026):
 plt.vlines(pd.Timestamp(f'{year}-12-31'), 10,113, color='gray', linestyle='-', linewidth=0.7)
 if year == 2024:
     plt.text(pd.Timestamp('2024-09-15'), 109.5, 2024, alpha=0.9, ha='center', va='center_baseline', fontsize=14)
 if year == 2025:
     plt.text(pd.Timestamp('2025-05-15'), 109.5, 2025, alpha=0.9, ha='center', va='center_baseline', fontsize=14)
 meses = ['ENE', 'FEB', 'MAR', 'ABR', 'MAY', 'JUN', 'JUL', 'AGO', 'SEP', 'OCT', 'NOV', 'DIC']
 for month, letra in enumerate(meses, start=1): 
       # Obtener el primer día del mes
       fecha = pd.Timestamp(year, month, 15) 
       if year == 2024 and month < 6:
        continue 
       if year == 2025 and month>mes:
        break
       plt.text(fecha, 103, letra, color='black', alpha=0.9, ha='center', va='center_baseline', fontsize=11)
       last_day = pd.Timestamp(year, month, 1) + pd.offsets.MonthEnd(0)  # Último día del mes
       if not (year == 2025 and month == mes):
         plt.vlines(last_day, 100, 106, color='gray', linestyle='-', linewidth=0.7) 
y_values = list(range(10,101,10))
for y in y_values:
    if y==100:
       plt.gca().hlines(y, pd.Timestamp('2024-06-01'), fin_mes, color='gray', linestyle='-', linewidth=1)
    else:
       plt.gca().hlines(y, pd.Timestamp('2024-06-01'), fin_mes, color='gray', linestyle='--', linewidth=0, alpha=0.8)
plt.ylabel('TNA (%)', color='black', labelpad=10)
plt.yticks(y_values)  
plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, _: f"{int(x):,}".replace(",", ".")))
plt.gca().tick_params(axis='y', labelsize='14')
plt.gca().hlines(113, pd.Timestamp('2024-06-01'), fin_mes, color='gray', linestyle='-', linewidth=1)
plt.gca().hlines(106, pd.Timestamp('2024-06-01'), fin_mes, color='gray', linestyle='-', linewidth=1)
plt.ylim(10, 115)
# Agregar la leyenda usando los patches
plt.legend(handles=patches, loc="upper center", frameon=False, handlelength=0.8, handleheight=0.8, ncol=3, bbox_to_anchor=(0.49,1.16), columnspacing=1.8, fontsize=13)
#plt.text(1, 1.18, '@JesusRobles824', fontsize=14, color='black', weight='bold', transform=plt.gca().transAxes, ha='right')
# Ajustar el diseño y mostrar el gráfico
plt.tight_layout()
sns.despine(left=True, bottom=False)
plt.gca().spines['bottom'].set_color('gray')
plt.savefig('Principales tasas de interés de mercado. TNA (%).png', bbox_inches='tight', pad_inches=0.4, dpi=150)
plt.show()
print(Tasas)









