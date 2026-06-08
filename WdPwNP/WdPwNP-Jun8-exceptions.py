from typing import List

class ProblematicValue(Exception):
    """Exception raised for custom error scenarios.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, line_number, value):
        self.line_number = line_number
        self.value = value
        super().__init__(f"{line_number} : {value}")


def divide(x, y):
    return x/y


def analizuj_dane(lista: List[float]):
    suma_odwrotna = 0
    # try:
    for line_no, wartosc in enumerate(lista):
        try:
            val =  divide(1.0, wartosc)
        except:
            raise ProblematicValue(line_no, wartosc)
        suma_odwrotna += val
    # except:
    #     print(f"nie udało się podzielić przez {wartosc}")
    return suma_odwrotna


moje_liczby_wczytane_z_pliku = {
    "dane1.txt": [1, 45, 32, 5, 2, 0, 3, 5],
    "dane2.txt": [4.5, 3.2, 5, 2, 10, 3, 5]
}

if __name__ == "__main__":
    for plik, dane in moje_liczby_wczytane_z_pliku.items():
        try:
            analizuj_dane(dane)
        except ProblematicValue as e:
            print("dzielenie przez zero w danych z pliku:", plik)
            print(f"problematyczna wartosc: {e.value} w linii {e.line_number}")


    # ---- wersja ze sprawdzeniem
    # lista = [1, 2, 0, 4, 3]
    # suma_odwrotna = 0
    # for wartosc in lista:
    #     val =  divide(1.0, wartosc)
    #     if val == None:
    #         print(f"nie udało się podzielić przez {wartosc}")
    #     else:
    #         suma_odwrotna += val
    # print(suma_odwrotna)
    #
    # # ---- wersja z wyjątkiem
    # lista = [1, 2, 0, 4, 3]
    # suma_odwrotna = 0
    # for wartosc in lista:
    #     try:
    #         val =  divide(1.0, wartosc)
    #         suma_odwrotna += val
    #     except:
    #         print(f"nie udało się podzielić przez {wartosc}")
    # print(suma_odwrotna)

    # ---- wersja z kaskadą wyjątków