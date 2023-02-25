import unittest
import math


def addDrink(drink):
    if len(drink) == 0:
        return "String vacio"

    parsed = drink.split(",")

    name = parsed[0]
    sizes = parsed[1:]
    
    if len(name) < 2:
        return "El nombre de la bebida tiene menos de 2 caracteres"
    
    if not name.replace(" ", "").isalpha():
        return "El nombre de la bebida no es alfabetico"
    
    if len(name) > 15:
        return "El nombre de la bebida tiene mas de 15 caracteres"
    
    if len(sizes) == 0:
        return "No se proporcionaron tamanos"
    
    if len(sizes) > 5:
        return "Se proporcionaron mas de 5 tamanos"

    for i in range(len(sizes)):
        size = sizes[i]
        size.replace(" ", "")
        try:
            val = float(size)

        except:
            if size == " ":
                return "Se ingreso un valor vacio entre comas"
            else:
                return "Se ingreso un valor no numerico"

        else:
            if math.floor(val) != val:
                return "Se ingreso un valor decimal"
            
            if val < 1:
                return "Se ingreso un tamano menor a 1"
            
            if val > 48:
                return "Se ingreso un tamano mayor a 48"
            
            sizes[i] = val
            
    if sizes != sorted(sizes):
        return "Los tamanos no estan ordenados"


    return "Bebida agregada con exito"


class TestAddDrink(unittest.TestCase):

    def test_valid(self):
        self.assertEqual(addDrink("Pepsi, 1, 3, 5"), "Bebida agregada con exito")
        self.assertEqual(addDrink("Fanta, 2, 10"), "Bebida agregada con exito")
        self.assertEqual(addDrink("Jarrito, 5, 12, 30, 45"), "Bebida agregada con exito")

    def test_nombreNoAlfabetico(self):
        self.assertEqual(addDrink("Chiva_cola, 5, 8, 12"), "El nombre de la bebida no es alfabetico")
        self.assertEqual(addDrink("Pepsi2.0, 2, 4, 8, 10, 12"), "El nombre de la bebida no es alfabetico")

    def test_nombreLongitudMenor(self):
        self.assertEqual(addDrink(", 1, 4, 8, 20"), "El nombre de la bebida tiene menos de 2 caracteres")
        self.assertEqual(addDrink("Q, 5, 12"), "El nombre de la bebida tiene menos de 2 caracteres")

    def test_nombreLongitudMayor(self):
        self.assertEqual(addDrink("Refresco super hyper mega refrescante, 1, 5, 8, 10, 14"), "El nombre de la bebida tiene mas de 15 caracteres")
        self.assertEqual(addDrink("Chescocacola mega plus limon menta, 2, 8, 20, 32"), "El nombre de la bebida tiene mas de 15 caracteres")

    def test_valorMenor(self):
        self.assertEqual(addDrink("Refrescola, -1, 3, 5, 8"), "Se ingreso un tamano menor a 1")
        self.assertEqual(addDrink("Cocofresco, 0, 1, 2"), "Se ingreso un tamano menor a 1")

    def test_valorMayor(self):
        self.assertEqual(addDrink("Refrescola, 2, 5, 8, 82"), "Se ingreso un tamano mayor a 48")
        self.assertEqual(addDrink("Cocofresco, 1, 2, 50"), "Se ingreso un tamano mayor a 48")

    def test_valorDecimal(self):
        self.assertEqual(addDrink("Mirinda, 5, 10, 12.5, 40"), "Se ingreso un valor decimal")
        self.assertEqual(addDrink("Agua, 2, 5.3, 20"), "Se ingreso un valor decimal")

    def test_valorNoNumerico(self):
        self.assertEqual(addDrink("Limonada, chica, grande"), "Se ingreso un valor no numerico")
        self.assertEqual(addDrink("Horchata, 5, jumbo, 10"), "Se ingreso un valor no numerico")

    def test_valoresNoDados(self):
        self.assertEqual(addDrink("Jamaica"), "No se proporcionaron tamanos")
        self.assertEqual(addDrink("Piña colada"), "No se proporcionaron tamanos")

    def test_valoresDeMas(self):
        self.assertEqual(addDrink("Mineral, 1, 2, 3, 4, 5, 6, 7"), "Se proporcionaron mas de 5 tamanos")
        self.assertEqual(addDrink("Vino, 2, 4, 8, 12, 20, 25, 30, 32"), "Se proporcionaron mas de 5 tamanos")

    def test_valoresNoEnOrden(self):
        self.assertEqual(addDrink("Naranjada, 10, 20, 5, 8"), "Los tamanos no estan ordenados")
        self.assertEqual(addDrink("Agua de coco, 30, 20, 25"), "Los tamanos no estan ordenados")

    def test_valorVacio(self):
        self.assertEqual(addDrink("Naranjada, , 5, 8"), "Se ingreso un valor vacio entre comas")
        self.assertEqual(addDrink("Agua de coco, , 12,"), "Se ingreso un valor vacio entre comas")

    def test_stringVacia(self):
        self.assertEqual(addDrink(""), "String vacio")

if __name__ == '__main__':
    unittest.main()