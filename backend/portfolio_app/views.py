# import csv
from django.shortcuts import render, redirect
from .forms import UploadFileForm
# from .models import Dataset
from .src.utils.functions import calc_corr_to_json
from .serializers import CorrelationMatrixSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view

# import pandas as pd

from .src.preprocessing.upload_data import upload_data
from .src.preprocessing.p00_cleaning import cleaning

# Variables globales
# correlation_region_1_global = {}

def upload_files(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Procesamiento de archivos CSV
            df_region_1, df_region_2, df_region_3 = upload_data(request)

            # Verifica los datos cargados
            if df_region_1.empty:
                print("df_region_1 está vacío.")
            else:
                print(f"Datos en df_region_1:\n{df_region_1.head()}")

            # Calcular la matriz de correlación en JSON
            correlation_data = calc_corr_to_json(df_region_1)
            print(f"Datos de correlación calculados:\n{correlation_data}")

            request.session['correlation_data'] = correlation_data
            request.session.save()  # Asegúrate de que la sesión se guarda

            return render(request, 'upload_success.html')
    else:
        form = UploadFileForm()
    
    return render(request, 'upload.html', {'form': form})

@api_view(['GET'])
def get_correlation_matrix(request):
    correlation_data = request.session.get('correlation_data', {})
    print('SESSION CORRELATION DATA:', correlation_data)
    if not correlation_data:
        return Response({'error': 'No correlation data available'}, status=404)
    serializer = CorrelationMatrixSerializer({'correlation_matrix': correlation_data})
    return Response(serializer.data)

# #@api_view(['POST'])
# def upload_files(request):
#     if request.method == 'POST':                                                                
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             # Carga de los datos csv
#             df_region_1, df_region_2, df_region_3 = upload_data(request)

#             # Calcular la matriz de correlación en JSON
#             correlation_data = calc_corr_to_json(df_region_1)

#             # Preprocesamiento de prueba
#             # print(cleaning(region_1_file))
#             # print(cleaning(region_2_file))
#             # print(cleaning(region_3_file))

#             # region_1_file = request.FILES['region_1']
#             # region_2_file = request.FILES['region_2']
#             # region_3_file = request.FILES['region_3']
            
#             # Aquí puedes procesar los archivos como lo necesites
#             # Por ejemplo, guardarlos en el sistema de archivos, procesarlos, etc.
            
#             return render(request, 'upload_success.html', {'correlation_data': correlation_data})  # Renderiza una página de éxito o redirige a otra vista
#     #else:
#     #    form = Response(form.errors, status=status.HTTP_400_BAD_REQUEST)    
    
#     return render(request, 'upload.html')

# def handle_uploaded_file(file):
#     reader = csv.reader(file.read().decode('utf-8').splitlines())
#     for row in reader:
#         Dataset.objects.create(
#             id=row[0],
#             f0=row[1],
#             f1=row[2],
#             f2=row[3],
#             product=row[4]
#         )

def success(request):
    return render(request, 'success.html')

#def home(request):
#    # Aquí puedes agregar lógica para procesar datos antes de mostrar la página
#    return render(request, 'home.html')

# Endpoint para la matriz de correlación
# @api_view(['GET'])
# def correlation_matrix(request):
#     # Cargar los datasets a partir de csv
#     df_region_1, df_region_2, df_region_3 = upload_data(request)

#     # Calcular la matriz de correlación en JSON
#     correlation_data = calc_corr_to_json(df_region_1)
#     return Response(correlation_data)