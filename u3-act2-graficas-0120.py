import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Listas con los datos de cada país
# Estructura: [País, Capital, Pertenece a la UE, Población en millones]
esp = ["España", "Madrid", True, 47.4]
mex = ["México", "CDMX", False, 126.7]
fra = ["Francia", "París", True, 67.7]
arg = ["Argentina", "Buenos Aires", False, 45.8]
jap = ["Japón", "Tokio", False, 125.7]

# Creamos una lista de listas (conformando la tabla)
lista_paises = [esp, mex, fra, arg, jap]

# Utilizar pandas para organizar la tabla (DataFrame)
df_paises = pd.DataFrame(
    lista_paises, columns=["País", "Capital", "Pertenece_UE", "Población"]
)
print(df_paises)

# Creamos el archivo CSV y lo guardamos
df_paises.to_csv("paises.csv", index=False)

# 1. Gráfica de líneas
plt.plot(df_paises["País"], df_paises["Población"])
plt.title("Gráfica de población por país 0120")
plt.xlabel("Países")
plt.ylabel("Población (millones)")
plt.show()

# 2. Gráfica de puntos
plt.plot(df_paises["País"], df_paises["Población"], "o")
plt.title("Gráfica de población por país (puntos) 0120")
plt.xlabel("Países")
plt.ylabel("Población (millones)")
plt.show()

# 3. Gráfica de barras
plt.bar(df_paises["País"], df_paises["Población"])
plt.title("Población por país 0120")
plt.xlabel("Países")
plt.ylabel("Población (millones)")
plt.show()

# 4. Gráfica de barras ordenada de manera descendente (con colores)
df_paises_ordenar = df_paises.sort_values("Población", ascending=False)
plt.bar(
    df_paises_ordenar["País"],
    df_paises_ordenar["Población"],
    color=["b", "g", "c", "m", "y"],
)
plt.title("Países ordenados por población de mayor a menor 0120")
plt.xlabel("Países")
plt.ylabel("Población (millones)")
plt.show()

# 5. Gráfica de pastel
plt.pie(df_paises["Población"], labels=df_paises["País"])
plt.title("Distribución porcentual de la población 0120")
plt.show()