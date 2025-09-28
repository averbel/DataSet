import pandas as pd
import numpy as np
import random

# Configurar semilla para reproducibilidad
np.random.seed(42)
random.seed(42)

# Número de registros
n_registros = 500

# Generar datos demográficos
edades = np.random.normal(19, 1.5, n_registros).astype(int)
edades = np.clip(edades, 17, 25)  # Rango razonable para estudiantes

generos = np.random.choice(['Masculino', 'Femenino', 'No binario'], 
                          n_registros, p=[0.48, 0.48, 0.04])

lugares_origen = np.random.choice([
    'Ciudad capital', 'Area metropolitana', 'Ciudad intermedia', 
    'Zona rural', 'Extranjero'
], n_registros, p=[0.3, 0.25, 0.25, 0.15, 0.05])

# Generar datos académicos
promedio_bachillerato = np.random.normal(75, 10, n_registros)
promedio_bachillerato = np.clip(promedio_bachillerato, 60, 100)

examen_admision = np.random.normal(700, 100, n_registros)
examen_admision = np.clip(examen_admision, 400, 1000)

nota_primer_semestre = np.random.normal(3.2, 0.8, n_registros)
nota_primer_semestre = np.clip(nota_primer_semestre, 1.0, 5.0)

# Generar datos financieros
nivel_socioeconomico = np.random.choice(['Bajo', 'Medio-bajo', 'Medio', 'Medio-alto', 'Alto'], 
                                       n_registros, p=[0.2, 0.3, 0.3, 0.15, 0.05])

becas = np.random.choice(['Ninguna', 'Parcial', 'Completa'], 
                        n_registros, p=[0.6, 0.3, 0.1])

creditos = np.random.choice(['Sí', 'No'], n_registros, p=[0.4, 0.6])

# Crear DataFrame
df = pd.DataFrame({
    'edad': edades,
    'genero': generos,
    'lugar_origen': lugares_origen,
    'promedio_bachillerato': promedio_bachillerato,
    'examen_admision': examen_admision,
    'nota_primer_semestre': nota_primer_semestre,
    'nivel_socioeconomico': nivel_socioeconomico,
    'beca': becas,
    'credito_educativo': creditos
})

# INTRODUCIR VALORES NULOS (aprox. 5% de los datos)
# Seleccionar aleatoriamente celdas para hacerlas nulas
for col in df.columns:
    if col != 'genero':  # Evitar género para mantener balance
        n_nulos = int(n_registros * 0.05)
        indices_nulos = np.random.choice(df.index, n_nulos, replace=False)
        df.loc[indices_nulos, col] = np.nan

# INTRODUCIR VALORES ATÍPICOS
# En edad (valores extremadamente altos)
indices_outlier_edad = np.random.choice(df.index, 8, replace=False)
df.loc[indices_outlier_edad, 'edad'] = np.random.randint(30, 45, 8)

# En promedio bachillerato (valores extremadamente bajos)
indices_outlier_promedio = np.random.choice(df.index, 10, replace=False)
df.loc[indices_outlier_promedio, 'promedio_bachillerato'] = np.random.uniform(40, 55, 10)

# En examen admisión (valores extremadamente altos)
indices_outlier_examen = np.random.choice(df.index, 7, replace=False)
df.loc[indices_outlier_examen, 'examen_admision'] = np.random.randint(1050, 1200, 7)

# CREAR VARIABLE OBJETIVO (abandono)
# Factores que influyen en el abandono
def calcular_probabilidad_abandono(row):
    prob = 0.0
    
    # Factores demográficos
    if row['lugar_origen'] == 'Zona rural':
        prob += 0.15
    if row['edad'] > 22:  # Estudiantes mayores
        prob += 0.1
    
    # Factores académicos
    if pd.notna(row['nota_primer_semestre']) and row['nota_primer_semestre'] < 2.5:
        prob += 0.25
    if pd.notna(row['promedio_bachillerato']) and row['promedio_bachillerato'] < 65:
        prob += 0.2
    if pd.notna(row['examen_admision']) and row['examen_admision'] < 500:
        prob += 0.15
    
    # Factores financieros
    if row['nivel_socioeconomico'] in ['Bajo', 'Medio-bajo']:
        prob += 0.2
    if row['beca'] == 'Ninguna':
        prob += 0.1
    
    # Ruido aleatorio
    prob += np.random.uniform(-0.1, 0.1)
    
    return min(max(prob, 0), 1)  # Asegurar entre 0 y 1

# Aplicar la función y determinar abandono
probabilidades = df.apply(calcular_probabilidad_abandono, axis=1)
df['abandono'] = np.random.binomial(1, probabilidades)

# Convertir a sí/no
df['abandono'] = df['abandono'].map({0: 'No', 1: 'Sí'})

# Mostrar información del dataset
print("Información del dataset:")
print(df.info())
print("\nPrimeras 10 filas:")
print(df.head(10))
print(f"\nTasa de abandono: {(df['abandono'] == 'Sí').mean():.2%}")

# Guardar dataset
df.to_csv('dataset_abandono_universitario.csv', index=False, encoding='utf-8')