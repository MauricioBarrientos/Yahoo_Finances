import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

simbolo = input("Ingresa el símbolo de la empresa: ")
tesla = yf.Ticker(simbolo)

# Obtener datos históricos
historial = tesla.history(period="max")

# Visualizar los datos históricos
historial['Close'].plot()
plt.title('Precio de cierre ajustado de ' + simbolo)
plt.xlabel('Fecha')
plt.ylabel('Precio')
plt.show()

# Calcular estadísticas básicas
media = historial['Close'].mean()
desviacion_estandar = historial['Close'].std()
precio_maximo = historial['Close'].max()
precio_minimo = historial['Close'].min()

print("Media:", media)
print("Desviación estándar:", desviacion_estandar)
print("Precio máximo:", precio_maximo)
print("Precio mínimo:", precio_minimo)

# Obtener información adicional sobre la empresa
nombre_empresa = tesla.info['longName']
descripcion = tesla.info['longBusinessSummary']
sector = tesla.info['sector']

print("Nombre de la empresa:", nombre_empresa)
print("Descripción:", descripcion)
print("Sector:", sector)