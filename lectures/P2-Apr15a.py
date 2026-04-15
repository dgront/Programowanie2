# ------ dekoratory w Pythonie

# --- przypomnienie o dekoratorach
import random

class K:
    @property
    def value(self):
        return random.random()

# k = K()
# print(k.value)

# --- Jak zrobić własny dekorator?
# funkcja (2) która przyjmuje funkcję (1) i zwraca funkcję (3)


# (2) - funkcja dekorująca
def capitalize_F2(func_F1):
    # (3) - dekorator właściwy
    def upercase_decorator_F3(name):
        text = func_F1(name)
        return text.upper()

    return upercase_decorator_F3

# (1) - funkcja która będzie udekorowana
@capitalize_F2
def powitaj_imie_F1(kogo: str):
    return "Witaj, "+kogo

def inna_f():
    pass

print(powitaj_imie_F1("Jan"))
print(powitaj_imie_F1("Anna"))