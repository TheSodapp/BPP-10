
# Control de errores, pruebas y validacion de datos

"""
1.  Crea una funcion que pida por pantalla un numero al
    usuario y que controle mediante excepciones lo siguiente:
        a. Solo se podra introducir numeros enteros
        b. Si el numero es mayor que 10 lanza una excepcion
           con raise la cual hayas creado previamente mediante
           'class Miexcepcion(Exception):'
"""

# 1.

class Miexcepcion(Exception):
    def __init__(self, numero):
        self.numero = numero
        self.mensaje = "El número {} es mayor que 10!".format(numero)

def funct1():
    try:
        num = int(input("Introduce un numero entero y menor que 10: "))
        assert isinstance(num, int)
        if num > 10:
            raise Miexcepcion(num)
    except ValueError:
        print("Error: Tienes que introducir un numero entero!")
    except AssertionError:
        print("Error: Tienes que introducir un numero entero!")
    except Miexcepcion as e:
        print("Error:", e.mensaje)
    else:
        print("El numero insertado es:", num)

funct1()





