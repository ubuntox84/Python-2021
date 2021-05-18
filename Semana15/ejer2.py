
"""Programa para mostrar la utilidad de comentar un codigo dentro de un modulo"""

__author__ = "Christian"
__copyright__ = "Curso de programacion Basica"
__credits__ = ["Alumno 2021"]
__license__ = "GPL"
__version__ = "1.0"
__email__ = "christian.garcia@unas.edu.pe"
__status__ = "Development"


def cubo(x):
    """Calcula el cubo de un numero"""
    y = x**3
    return y

if __name__ == "__main__":
    x = int( input("Dame un numero: ") )
    y = cubo(x)
    print("El cubo de %.2f es %.2f" % (x, y))