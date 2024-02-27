# OilyGiant ¿Dondé invertir los pozos?

## Contacto
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/andres946/)
[![Correo Electrónico](https://img.shields.io/badge/Correo%20Electrónico-andresgvelasquez8@gmail.com-red?style=for-the-badge&logo=mail.ru)](mailto:andresgvelasquez8@gmail.com) 

## Descripción del proyecto

Trabajas para la compañía minera OilyGiant. La tarea es encontrar el mejor lugar para un nuevo pozo.
Pasos para elegir la ubicación:
- Recolectar los parámetros del pozo de petróleo en la región seleccionada: calidad
del petróleo y volumen de reservas.
- Construir un modelo para predecir el volumen de reservas en los nuevos pozos.
- Seleccionar los pozos de petróleo con los valores estimados más altos.
- Elegir la región con el mayor beneficio total para los pozos de petróleo
seleccionados.

Se tienen datos sobre muestras de crudo de tres regiones. Ya se conocen los parámetros de cada pozo petrolero de la región. Crear un modelo que ayude a elegir la región con el mayor margen de beneficio. Analiza los beneficios y riesgos potenciales utilizando la técnica bootstrapping.

## Descripción de los datos

Los datos de exploración geológica de las tres regiones se almacenan en archivos:
- `../datasets/ggeo_data_0.csv`. 
- `../datasets/ggeo_data_1.csv`. 
- `../datasets/ggeo_data_2.csv`. 
  
Los archivos contienen las siguientes columnas:
- `id` — identificador único de pozo de petróleo
- `f0`, `f1`, `f2` — tres características de los puntos (su significado específico no es importante, pero las características en sí son significativas)
- product — volumen de reservas en el pozo de petróleo (miles de barriles).

## Instalación de dependencias

Para instalar las dependencias necesarias para este proyecto, puedes ejecutar el siguiente comando:

```bash
pip install -r requirements.txt
```