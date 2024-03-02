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

## Data Description

Geological exploration data for the three regions are stored in files:

- `../datasets/ggeo_data_0.csv`.
- `../datasets/ggeo_data_1.csv`.
- `../datasets/ggeo_data_2.csv`.

The files contain the following columns:

- `id` — unique identifier of the oil well.
- `f0`, `f1`, `f2` — three features of the points (their specific meaning is not important, but the features themselves are significant).
- `product` — volume of reserves in the oil well (thousands of barrels).

## Virtual Environment Setup

To run this project, it is recommended to create a Python virtual environment. You can do this by executing the following commands in your terminal:

```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
# or
.\venv\Scripts\activate   # For Windows
```

Then, you need to install the dependencies:

```bash
pip install -r requirements.txt
```
Once you have set up the virtual environment and installed the dependencies, you can run the project.

