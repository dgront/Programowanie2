# x = 12
#
# def kwadratuj():
#     return x * x
# x = 4
# kwadratuj()

# --------- Programowanie obiektowe
class NaszaKlasa:

    def __init__(self):
        self.x = 12

    def kwadratuj(self):
        return self.x * self.x

if __name__ == "__main__":
    o1 = NaszaKlasa()
    o1.x += 4.5
    o2 = NaszaKlasa()
    o2.x = 8
    print(o1.kwadratuj())
    print(o2.kwadratuj())

