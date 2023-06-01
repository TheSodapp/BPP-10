
# Control de errores, pruebas y validacion de datos

"""
2.  Abre un fichero .txt y controla mediante excepciones las 
    diferentes casuisticas para que el programa no termine de
    forma inesperada. Utiliza el finally para cerrar el fichero.
"""

# 2.

try:
    with open("fichero.txt", "r") as fichero:
        lineas = fichero.readlines()
        for linea in lineas:
            print(linea)
except FileNotFoundError:
    print("Error: El fichero no se ha encontrado.")
except Exception as e:
    print(f"Error: {e}")
except:
    print("Ha ocurrido un error inesperado.")
finally:
    fichero.close()
