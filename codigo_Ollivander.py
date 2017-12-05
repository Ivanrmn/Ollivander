def intAString(matrizCasosTest):
    """Habíamos pasado unos valores de la lista a integer y ahora 
    los volvemos a pasar a string, para meterlos en el fichero de texto"""

    for linea in fichero:
        if not linea.find("day") != -1 and not linea == "\n" and linea.find("name") != -1:
            str(matrizCasosTest[1])
            str(matrizCasosTest[2])
            return matrizCasosTest


def crearFicheroCasosTest(ficheroVolcadoCasosTest, matrizCasosTest):
    """Esta función crea el fichero stdout con los datos de la tienda de Ollivander.
    matrizCasosTest es una lista con los datos de los casos test"""

    try:
        if not isinstance(ficheroVolcadoCasosTest, str):
            raise ValueError
        stdout = open(ficheroVolcadoCasosTest, 'w')
    except ValueError:
            print("La ruta de acceso al fichero ha de ser un string")
    else:
        for (offset, casosTestDia) in enumerate(matrizCasosTest):
            stdout.write('-' * 5 + " Dia %d: " % offset + '-' * 5 + '\n')
            for item in casosTestDia:
                stdout.write(','.join(item) + '\n')
        stdout.close()


def mostrarCasosTest(matrizCasosTest):
    """Esta función nos muestra los items que tiene la tienda"""

    for (offset, casosTestDia) in enumerate(matrizCasosTest):
        print('-' * 5 + " Dia %d: " % offset + '-' * 5)
        for item in casosTestDia:
            print(item)
