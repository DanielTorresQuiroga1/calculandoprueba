import pandas as pd
from datasets import load_dataset

# Cargar el dataset
dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]

# Convertir el dataset en un DataFrame de Pandas
df = pd.DataFrame(data)

# Verificar los tipos de datos de cada columna
print("Tipos de datos de cada columna:")
print(df.dtypes)
print("\n")

# Asegurarse de que los tipos de datos sean correctos
# Si es necesario, convertir los tipos de datos, por ejemplo:
# df['column_name'] = df['column_name'].astype('desired_type')

# Calcular la cantidad de hombres fumadores vs mujeres fumadoras
# Asumiendo que 'is_male' es 1 para hombres y 0 para mujeres
# y 'is_smoker' es 1 para fumadores y 0 para no fumadores

hombres_fumadores = df[(df['is_male'] == 1) & (df['is_smoker'] == 1)].shape[0]
mujeres_fumadoras = df[(df['is_male'] == 0) & (df['is_smoker'] == 1)].shape[0]

print(f"Hombres fumadores: {hombres_fumadores}")
print(f"Mujeres fumadoras: {mujeres_fumadoras}")