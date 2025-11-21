#py -m pip install scikit-learn
#py -m pip install seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler
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


# --- Gráfico 1: ProductRelated_Duration ---
plt.figure(figsize=(8, 5))
sns.boxplot(x='Revenue', y='ProductRelated_Duration', data=raw_dataset)
plt.title('Duración en Productos vs. Compra')
plt.xlabel('Generó Compra (Revenue)')
plt.ylabel('Duración en Productos (segundos)')
plt.show()

# --- Gráfico 2: BounceRates ---
plt.figure(figsize=(8, 5))
sns.boxplot(x='Revenue', y='BounceRates', data=raw_dataset)
plt.title('Tasa de Rebote vs. Compra')
plt.xlabel('Generó Compra (Revenue)')
plt.ylabel('Tasa de Rebote')
plt.show()

plt.figure(figsize=(10, 6))

# --- Creación del Gráfico de Dispersión ---
sns.scatterplot(x='BounceRates', 
                y='ProductRelated_Duration', 
                hue='Revenue', 
                data=raw_dataset,
                alpha=0.3) #  Para poder visualizar mejor la densidad

plt.title('Hipótesis: Duración vs. Tasa de Rebote (Coloreado por Compra)')
plt.xlabel('Tasa de Rebote (BounceRates)')
plt.ylabel('Duración en Productos (segundos)')
plt.legend(title='¿Compró? (Revenue)')
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()

calculo_hipotesis = raw_dataset.groupby('Revenue')[['ProductRelated_Duration', 'BounceRates']].mean()
print(calculo_hipotesis)

#Etapa de validacion

# --- 1. Definir X e Y ---
independientes = ['ProductRelated_Duration', 'BounceRates']
dependiente = 'Revenue'
X = raw_dataset[independientes]
y = raw_dataset[dependiente]

# --- 2. Escalar los datos ---
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled_const = sm.add_constant(X_scaled)

# Entrenar regresión con todo el dataset
modelo = sm.Logit(y,X_scaled_const)
resultado = modelo.fit()

# --- 4. RESULTADOS---
tabla = pd.DataFrame({
    "Coeficiente": resultado.params,
    "P-Value": resultado.pvalues
})

tabla.index = ['c', 'ProductRelated_Duration', 'BounceRates']
print(tabla)

