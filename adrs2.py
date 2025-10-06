import yfinance as yf
import requests
import pandas as pd
import numpy as np
from datetime import timedelta
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.patches as mpatches
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib.lines import Line2D
from datetime import datetime
import re
from matplotlib.dates import date2num
from matplotlib.ticker import FixedLocator

# Definir la fecha de hoy automáticamente
hoy = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')

tickers_adrs = ['BBAR', 'BMA', 'CEPU', 'CRESY', 'EDN', 'GGAL', 'IRS','LOMA',
                'PAM', 'SUPV', 'TEO', 'TGS', 'TS', 'TX', 'YPF']

# Descargar datos históricos de los ADRs y el Merval
adrs = yf.download(tickers_adrs, start='2010-01-01', end=hoy)['Close']
adrs.columns.name = None  # Correcto
adrs.index.name = 'fecha'  # Correcto
print(adrs)

adrs_var = adrs.pct_change() * 100  # en %
print(adrs_var)