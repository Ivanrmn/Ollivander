def accesoCasosTexttest(matrizCasosTest, rutaAccesoFichero):
    """rutaAccesoFichero abre un fichero en modo lectura si lo encuentra, sino mostrará un mensaje.
    matrizCasosTest crea una lista vacía y al llegar al return, debería mostrar los datos del fichero casos_test"""

     try:
        if not isinstance(rutaAccesoFichero, str):
            raise ValueError
        fichero = open(rutaAccesoFichero, 'r')
    except FileNotFoundError:
        print("Fichero no encontrado")
        return []
    except ValueError:
        print("El nombre del fichero ha de ser un string")
        return []
   else:
        matrizCasosTest = []
        numeroPropiedadesItem = 0
        for linea in fichero:
            if linea.find("day") != -1:
                casosTestDia = []
            elif linea == "\n":
                matrizCasosTest.append(casosTestDia)
            elif linea.find("name") != -1:
                numeroPropiedadesItem = len(linea.split(','))
            else:
                int(matrizCasosTest[1])
                int(matrizCasosTest[2])
                item = linea.rstrip().rsplit(',', maxsplit=numeroPropiedadesItem - 1)
                casosTestDia.append(item)
        fichero.close()
        return matrizCasosTest