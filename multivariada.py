#py -m pip install scikit-learn
#py -m pip install seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
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

# --- 3. Dividir y Entrenar ---
# Dividimos para entrenar el calculador y luego validar
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)
modelo = LogisticRegression()
modelo.fit(X_train, y_train)

# --- 4. LOS RESULTADOS (Los Coeficientes) ---
coefs = pd.DataFrame(
    modelo.coef_[0],
    index=independientes,
    columns=['Coeficiente (Peso Estadístico)']
)
print("--- VALIDACIÓN DE LA HIPÓTESIS ---")
print(coefs)

# --- 5. Validación del Test ---
y_pred = modelo.predict(X_test)
print(f"\nPrecisión de la Validación: {accuracy_score(y_test, y_pred):.3f}")