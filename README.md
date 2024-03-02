# OilyGiant: Where to invest in wells?

## Contact
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/andres946/)
[![Correo Electrónico](https://img.shields.io/badge/Correo%20Electrónico-andresgvelasquez8@gmail.com-red?style=for-the-badge&logo=mail.ru)](mailto:andresgvelasquez8@gmail.com) 

## Description of the project

You work for the mining company OilyGiant. The task is to find the best location for a new oil well.
Steps to choose the location:

- Collect parameters of oil wells in the selected region: oil quality and reserve volume.
- Build a model to predict reserve volume in new wells.
- Select oil wells with the highest estimated values.
- Choose the region with the highest total profit for the selected oil wells.

Data on crude oil samples from three regions are available. Parameters of each oil well in the region are already known. Create a model to help choose the region with the highest profit margin. Analyze potential benefits and risks using the bootstrapping technique.

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
