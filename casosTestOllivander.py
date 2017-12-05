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