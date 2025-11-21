from os import path, listdir
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu

dataset = pd.read_csv("online_shoppers_intention.csv")
dataset.drop_duplicates(keep="first", inplace=True)
dataset["SpecialDay"] = dataset["SpecialDay"] > 0

# Hipótesis:
# H0: Los días especiales NO tienen mayor cantidad de visitas en productos que los días normales.
# H1: Los días especiales tienen mayor cantidad de visitas en productos que los días normales.

grupo_sd1 = dataset[dataset["SpecialDay"] == True]["ProductRelated"]
grupo_sd0 = dataset[dataset["SpecialDay"] == False]["ProductRelated"]

# Prueba Mann-Whitney U (cola derecha: sd1 > sd0)
stat, p_valor = mannwhitneyu(grupo_sd1, grupo_sd0, alternative='greater')

print("Estadístico U:", stat)
print("p-valor:", p_valor)

alpha = 0.05

if p_valor < alpha:
    print("Se rechaza H0: los días especiales tienen MÁS visitas a productos que los días normales.")
else:
    print("No se rechaza H0: no hay evidencia de que los días especiales tengan más visitas a productos que los días normales.")

plt.figure(figsize=(7,5))
plt.hist(grupo_sd0, bins=20, alpha=0.5, label="SpecialDay = False")
plt.hist(grupo_sd1, bins=20, alpha=0.5, label="SpecialDay = True")
plt.title("Distribución de ProductRelated por tipo de día")
plt.xlabel("ProductRelated")
plt.ylabel("Frecuencia")
plt.legend()
plt.show()
