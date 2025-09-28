# Dataset Sintético: Abandono Universitario

## Descripción

Este dataset sintético simula información de 500 estudiantes universitarios y su probabilidad de abandono durante el primer año. El conjunto de datos incluye variables demográficas, académicas, financieras y la variable objetivo de abandono.

## Variables

### Variables Demográficas

| Variable | Tipo | Descripción | Rango/Valores |
|----------|------|-------------|---------------|
| edad | Numérica entera | Edad del estudiante | 17-45 años |
| genero | Categórica | Género del estudiante | Masculino, Femenino, No binario |
| lugar_origen | Categórica | Lugar de procedencia | Ciudad capital, Area metropolitana, Ciudad intermedia, Zona rural, Extranjero |

### Variables Académicas

| Variable | Tipo | Descripción | Rango/Valores |
|----------|------|-------------|---------------|
| promedio_bachillerato | Numérica decimal | Promedio de notas en bachillerato | 40-100 puntos |
| examen_admision | Numérica entera | Puntaje en examen de admisión | 400-1200 puntos |
| nota_primer_semestre | Numérica decimal | Promedio del primer semestre | 1.0-5.0 |

### Variables Financieras

| Variable | Tipo | Descripción | Rango/Valores |
|----------|------|-------------|---------------|
| nivel_socioeconomico | Categórica | Nivel socioeconómico | Bajo, Medio-bajo, Medio, Medio-alto, Alto |
| beca | Categórica | Tipo de beca recibida | Ninguna, Parcial, Completa |
| credito_educativo | Categórica | Tiene crédito educativo | Sí, No |

### Variable Objetivo

| Variable | Tipo | Descripción | Valores |
|----------|------|-------------|---------|
| abandono | Categórica | Indica si el estudiante abandonó | Sí, No |

## Tratamiento de Datos

### Valores Nulos

Se introdujeron valores nulos en aproximadamente el 5% de las celdas del dataset, excluyendo la variable de género para mantener el balance demográfico. Los nulos se distribuyeron aleatoriamente en todas las columnas.

### Valores Atípicos

Se introdujeron valores atípicos de la siguiente manera:

1. **Edad**: 8 registros con edades entre 30-45 años (estudiantes atípicamente mayores)
2. **Promedio bachillerato**: 10 registros con promedios entre 40-55 puntos (valores extremadamente bajos)
3. **Examen admisión**: 7 registros con puntajes entre 1050-1200 puntos (valores extremadamente altos)

## Metodología de Generación

El dataset fue generado usando distribuciones normales para variables continuas y distribuciones categóricas balanceadas para variables nominales. La variable objetivo "abandono" se calculó considerando múltiples factores de riesgo:

- Factores demográficos (origen rural, edad avanzada)
- Factores académicos (bajo rendimiento)
- Factores financieros (bajo nivel socioeconómico, falta de becas)

## Uso Previsto

Este dataset puede utilizarse para:
- Análisis exploratorio de datos
- Modelos predictivos de abandono estudiantil
- Pruebas de técnicas de imputación de valores nulos
- Detección y tratamiento de valores atípicos
- Ejercicios de machine learning para clasificación binaria

## Estructura del Dataset

- **Filas**: 500 registros de estudiantes
- **Columnas**: 10 variables (9 features + 1 target)
- **Formato**: CSV con encoding UTF-8

## Notas Importantes

- Este es un dataset sintético generado para fines educativos
- Las correlaciones y patrones son artificiales pero representativos
- No representa datos reales de estudiantes