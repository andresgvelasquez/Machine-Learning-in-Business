def calc_corr_to_json(df,drop_colsnames='id'):
    # Crea la matrix de correlación
    correlation_matrix = df.drop(drop_colsnames, axis=1).corr()

    #Convirte la matriz de correlación en formato JSON
    correlation_data  = {
        'variables': list(correlation_matrix.columns),
        'correlation_matrix': correlation_matrix.values.tolist()
    }

    return correlation_data