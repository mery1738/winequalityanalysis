# functions.py
import csv
import math

#Ejercicio 2
def read_data(filename):
    """Esta funcion lee un fichero csv y devuelve un diccionario con los datos del fichero.

    Args:
        filename (text): nombre del fichero csv

    Raises:
        ValueError: Si el fichero tiene menos de 10 muestras con todos los atributos.

    Returns:
        diccionario: los datos del fichero csv
    """
    
    with open(filename, 'r') as file:
        
        reader = csv.DictReader(file)
        data = {}
        
        for row in reader:
            
            if all(row.values()):
                
                data[f'dato{len(data)+1}'] = {
                    'type': row['type'],
                    'fixed acidity': row['fixed acidity'],
                    'volatile acidity': row['volatile acidity'],
                    'citric acid': row['citric acid'],
                    'residual sugar': row['residual sugar'],
                    'chlorides': row['chlorides'],
                    'free sulfur dioxide': row['free sulfur dioxide'],
                    'total sulfur dioxide': row['total sulfur dioxide'],
                    'density': row['density'],
                    'pH': row['pH'],
                    'sulphates': row['sulphates'],
                    'alcohol': row['alcohol'],
                    'quality': row['quality']
                }
                
        if len(data) < 10:
            raise ValueError('donde se indica que el fichero tiene menos de 10 muestras con todos los atributos.')
        
        return data
#Ejercicio 3 
def split(data):
    """Esta funcion recibe un diccionario con los datos del fichero csv y devuelve dos diccionarios, uno con los datos del tipo white y otro con los datos del tipo red.

    Args:
        data (diccionario): diccionario con los datos del fichero csv

    Returns:
        diccionario: diccionario con los datos del tipo white
        diccionario: diccionario con los datos del tipo red
    """
    white = {}
    red = {}
    
    for i in data:

        nuevo = data[i].copy()
        del nuevo['type']
        
        if data[i]['type'] == 'white':
            white[i] = nuevo
        
        elif data[i]['type'] == 'red':
            red[i] = nuevo
            
    if not white:
        raise ValueError('donde se indica que no hay datos del tipo white.')
    if not red:
        raise ValueError('donde se indica que no hay datos del tipo red.')
            
    return white, red
#Ejercicio 4 
def reduce(data, atributo):
    """Esta funcion recibe un diccionario y un atributo y devuelve una lista con los valores de ese atributo.
    
    Args:
        data (diccionario): diccionario con los datos del fichero csv
        atributo (str): nombre del atributo
    
    Returns:
        lista: lista con los valores del atributo
    """
    resultado = []

    for v in data.values():
        
        if atributo not in v:
            raise ValueError
        
        resultado.append(float(v[atributo]))

    return resultado
#Ejercico 5 

import math

def silhouette(lista1, lista2):
    """Esta funcion recibe dos listas y devuelve el coeficiente de Silhouette de la primera lista.

    Args:
        lista1 (lista): lista con los valores del atributo
        lista2 (lista): lista con los valores del atributo

    Returns:
        float: coeficiente de Silhouette de la primera lista
    """
    if len(lista1) < 2:
        raise ValueError("La lista1 debe tener al menos 2 elementos.")
    
    if len(lista2) == 0:
        raise ValueError("La lista2 no puede estar vacía.")

    s_values = []

    for x in lista1:
        a = sum(math.sqrt((x - y)**2) for y in lista1 if y != x) / (len(lista1) - 1)
        b = sum(math.sqrt((x - y)**2) for y in lista2) / len(lista2)

        s = (b - a) / max(a, b)
        s_values.append(s)

    if len(s_values) == 0:
        raise ValueError("No se pudieron calcular los valores de Silhouette.")

    return sum(s_values) / len(s_values)
