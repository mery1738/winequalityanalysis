# main.py

from functions import *

def main():
    try:
        # Ejercicio 2 
        data = read_data("winequality.csv")
        #print(data)
        # Ejercicio 3
        white, red = split(data)
        #print(red)
        #print(data['dato4870']['type'])
        #Ejercicio 4 
        lista = reduce(white, 'alcohol')
        #print(lista)
        #Ejercicio 5 
        lista1= reduce(white, "density")
        lista2= reduce(red, "density")
        print(silhouette(lista1, lista2))

    except Exception as e:
        print(f"Ha ocurrido la excepción {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()



