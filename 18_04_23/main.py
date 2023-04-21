# TOMASZ SERAFINSKI s24353, Grupa: 12c

import math
import random


# ZAD 1
class Prostokat:
    def __init__(self):
        self.a = 0.0
        self.b = 0.0
        self.pole = 0.0

    def czytaj_dane(self):
        self.a = float(input("Wprowadź długość boku 'a': "))
        self.b = float(input("Wprowadź długość boku 'b': "))

    def przetworz_dane(self):
        self.pole = self.a * self.b

    def wyswietl_wynik(self):
        print(f"Bok 'a': {self.a}\nBok 'b': {self.b}\nPole: {self.pole}")


# ZAD 2
class Rownanie_Kwadratowe:
    def __init__(self):
        self.a = 0.0
        self.b = 0.0
        self.c = 0.0

    def czytaj_zmienne(self):
        self.a = float(input("Wprowadź wartość dla 'a': "))
        self.b = float(input("Wprowadź wartość dla 'b': "))
        self.c = float(input("Wprowadź wartość dla 'c': "))

    def policz_pierwiastki(self):
        delta = self.b ** 2 - 4 * self.a * self.c

        if delta < 0:
            return None

        if delta == 0:
            pierwiastek = -self.b / (2 * self.a)
            return round(pierwiastek, 2)

        pierwiastek1 = (-self.b + math.sqrt(delta)) / (2 * self.a)
        pierwiastek2 = (-self.b - math.sqrt(delta)) / (2 * self.a)

        return round(pierwiastek1, 2), round(pierwiastek2, 2)

    def wyswietl_wyniki(self, pierwiastki):
        if pierwiastki is None:
            print("Równanie nie posiada pierwiastków")
        elif isinstance(pierwiastki, tuple):
            print(f"Równanie posiada 2 pierwiastki: {pierwiastki[0]} i {pierwiastki[1]}")
        else:
            print(f"Równanie posiada 1 pierwiastek: {pierwiastki}")


# ZAD 3
class Macierz_Diagonalna:
    def __init__(self, rozmiar=10):
        self.rozmiar = rozmiar
        self.macierz = [[0 for _ in range(rozmiar)] for _ in range(rozmiar)]
        self.suma_diagonalna = 0

    def wypelnij_tabele(self):
        for i in range(self.rozmiar):
            self.macierz[i][i] = random.randint(0, 9)

    def wylicz_sume(self):
        for i in range(self.rozmiar):
            self.suma_diagonalna += self.macierz[i][i]

    def wyswietl_macierz(self):
        for rzad in self.macierz:
            print(" ".join(map(str, rzad)))
        print(f"Suma elementów diagonalnych to: {self.suma_diagonalna}")


# ZAD 4
class BubbleSort:
    def __init__(self, numery):
        self.numery = numery

    def posortuj_dane(self):
        n = len(self.numery)

        for i in range(n):
            for j in range(0, n - i - 1):
                if self.numery[j] > self.numery[j + 1]:
                    self.numery[j], self.numery[j + 1] = self.numery[j + 1], self.numery[j]

    def wyswietl_posortowane_dane(self):
        print("Posortowane numery:", self.numery)


if __name__ == "__main__":
    # ZAD 1
    prostokat = Prostokat()
    prostokat.czytaj_dane()
    prostokat.przetworz_dane()
    print()
    prostokat.wyswietl_wynik()

    # ZAD 2
    rownanie = Rownanie_Kwadratowe()
    rownanie.czytaj_zmienne()
    pierwiastki = rownanie.policz_pierwiastki()
    rownanie.wyswietl_wyniki(pierwiastki)

    # ZAD 3
    macierz_diagonalna = Macierz_Diagonalna()
    macierz_diagonalna.wypelnij_tabele()
    macierz_diagonalna.wylicz_sume()
    macierz_diagonalna.wyswietl_macierz()

    # ZAD 4
    numery = [547, 303, -134, 125, 80, 236]
    bubble_sort = BubbleSort(numery)
    bubble_sort.posortuj_dane()
    bubble_sort.wyswietl_posortowane_dane()
