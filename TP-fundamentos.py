import pandas as pd

from wget import download
from os import path, listdir

#Descargamos csv
if not path.exists("online_shoppers_intention.csv"):
  download("https://raw.githubusercontent.com/Naay-Arenaza/TPE-Fundamentos-de-la-Ciencia-de-Datos/main/online_shoppers_intention.csv")
else:
  print("No vamos a bajar el archivo de casas porque ya existe!")

#chequeamos si los archivos están en el directorio donde estamos parados
lista_archivos = listdir("./")
print(f"El contenido de la carpeta es: {lista_archivos}")

# abrimos el archivo usando una función específica de pandas
raw_dataset = pd.read_csv("online_shoppers_intention.csv")
#print(raw_dataset)
print(raw_dataset.describe())
print(raw_dataset.describe(include='object'))
print(raw_dataset.info())
print(raw_dataset.isna().sum())


#DUPLICADOS:
# Contamos los duplicados, daba 125, los mostramos para ver que onda y desp los eliminamos, para ello debemos sacar a todos menos uno, con lo cual necesitamos pasar keep="first".
#  Vamos a usar el método drop_duplicates():
# contamos la cantidad de duplicados
print(raw_dataset.duplicated().sum())
# imprimimos las filas duplicadas
print(raw_dataset[raw_dataset.duplicated(keep=False)])
# eliminamos los duplicados
print(raw_dataset.drop_duplicates(keep="first", inplace=True))
# contamos la cantidad de duplicados
print(raw_dataset.duplicated().sum())
#La probabilidad de que dos sesiones diferentes (dos usuarios distintos) hayan generado por "coincidencia" 18 valores exactamente idénticos (hasta el último decimal de tiempo y tasas) es matemáticamente imposible.
#Conclusión: Los 125 duplicados no son casualidades, son 100% errores de registro (el sistema guardó la misma sesión varias veces).





# Revisa la columna 'Region'
#print("Valores únicos en Region:")
#print(raw_dataset['Region'].value_counts())

# Revisa la columna 'Browser'
#print("\nValores únicos en Browser:")
print(raw_dataset['TrafficType'].value_counts())

#print(raw_dataset['VisitorType'])

#print(raw_dataset['VisitorType'].value_counts())
#print("\n",raw_dataset['SpecialDay'].value_counts())
#print("\n",raw_dataset['TrafficType'])
#print(raw_dataset['TrafficType'].value_counts())
#print(raw_dataset['Month'].value_counts())

#print("")
#print("ProductsRelated")
#print(raw_dataset['ProductRelated'])
#print(raw_dataset['ProductRelated'].value_counts)

#print("")
#print("PageValues")
#print(raw_dataset['PageValues'])
#print(raw_dataset['PageValues'].value_counts)
# Asumiendo que tu DataFrame se llama 'df'

# 1. Creamos categorías simples: ¿El usuario vio este tipo de página?
#raw_dataset['vio_informativa'] = raw_dataset['Informational'] > 0
#raw_dataset['vio_administrativa'] = raw_dataset['Administrative'] > 0
#raw_dataset['vio_producto'] = raw_dataset['ProductRelated'] > 0

# 2. Ahora, agrupamos por esa categoría y calculamos la media de 'PageValues'

#print("Valor promedio de página si VIO (True) o NO VIO (False) Informativas:")
#print(raw_dataset.groupby('vio_informativa')['PageValues'].mean())

#print("\nValor promedio de página si VIO (True) o NO VIO (False) Administrativas:")
#print(raw_dataset.groupby('vio_administrativa')['PageValues'].mean())