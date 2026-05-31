from __future__ import annotations
from typing import List
import copy

class Polynomial:

    def __init__(self, coefficients: List[float]):
        """Creates a new Polynomial"""
        self.__wsp = copy.deepcopy(coefficients)

    def order(self):
        return len(self.__wsp) - 1

    def __add__(self, other: Polynomial):
        other.__wsp.reverse()
        self.__wsp.reverse()
        (longer_w, shorter_w) = (other.__wsp, self.__wsp)
        if len(longer_w) < len(shorter_w):
            (longer_w, shorter_w) = (shorter_w, longer_w)

        wynik = copy.deepcopy(longer_w)
        for i in range(len(shorter_w)):
            wynik[i] += shorter_w[i]
        other.__wsp.reverse()
        self.__wsp.reverse()
        wynik.reverse()

        return Polynomial(wynik)

    def get_coeff(self, i) -> float:
        return self.__wsp[i]

    def __funkcja_pomocnicza(self):
        pass

    def __str__(self):
        o = self.order()
        napis = ""
        for w in self.__wsp:
            napis += format(f"{w} * x^{o} ")
            o -= 1
        return napis


if __name__ == "__main__":
    coeff = [1,-2, 3]
    p1 = Polynomial(coeff)
    print(p1)
    coeff.append(9)
    print(p1)
    p2 = Polynomial([2, 3])
    p3 = p1 + p2
    w = p3.get_coeff(0)
    print(w, p3)

