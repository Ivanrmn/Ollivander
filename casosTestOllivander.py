"""2. Concluye: ¿qué problemas presenta el código?
	Trataba las números de la lista como string, así que no podía calcular lo que necesitaba."""

"""4. Que es la deuda técnica.
	Es el coste a pagar por hacer rápido y mal las cosas. A medida que avanza el tiempo, la deuda aumenta, 
	porque cada vez que se trabaja más sobre un código mal hecho, más se deberá corregir hasta solucionar el problema."""

"""Importamos las funciones al archivo principal"""

from accesoCasosTexttest import accesoCasosTexttest
from codigo_Ollivander import crearFicheroCasosTest, mostrarCasosTest

if __name__ == "__main__":

    rutaAccesoFichero = "casos_test.txt"
    # rutaAccesoFichero = "stdout_bug_conjured.gr"

    matrizCasosTest = []

    matrizCasosTest = accesoCasosTexttest(matrizCasosTest, rutaAccesoFichero)

    mostrarCasosTest(matrizCasosTest)

    ficheroVolcadoCasosTest = "stdout.txt"

    crearFicheroCasosTest(ficheroVolcadoCasosTest, matrizCasosTest)