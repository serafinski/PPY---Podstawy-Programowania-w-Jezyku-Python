# TOMASZ SERAFIŃSKI s24353, Grupa: 12c
import os
import time


def zad1():
    # KALKULATOR
    def kalkulator():
        try:
            a = float(input("Wprowadź pierwszą liczbę: "))
            dzialanie = input("Wprowadź: \n + - jeżeli chcesz dodać do siebie liczby"
                              "\n - - jeżeli chcesz odjąć liczby"
                              "\n * - jeżeli chcesz pomnożyć liczby"
                              "\n / - jeżeli chcesz podzielić liczby"
                              "\n\nTwój wybór:")
            b = float(input("Wprowadź drugą liczbę: "))

            if dzialanie == '+':
                return a + b
            elif dzialanie == '-':
                return a - b
            elif dzialanie == '*':
                return a * b
            elif dzialanie == '/':
                if b == 0:
                    print("Nie można dzielić przez 0!")
                    return float('inf')
                else:
                    return a / b
            else:
                return "Wprowadzono nieprawidłowy znak!"

        except ValueError:
            print("Proszę wprowadzić liczby!")

    rownanie = kalkulator()
    print(f"Wynik: {rownanie}")

    # UŁAMEK
    class Ulamek:
        def __init__(self, licznik, mianownik):
            self.licznik = licznik

            if mianownik == 0:
                print("Nie można dzielić przez 0!")
                self.mianownik = float("inf")

            else:
                self.mianownik = mianownik

    # HIERARCHIA OPERACJI

    class Operacja:
        def wykonaj(self):
            pass

    class Dodawanie(Operacja):
        def wykonaj(self, a, b):
            return a + b

    class Odejmowanie(Operacja):
        def wykonaj(self, a, b):
            return a - b

    class Mnozenie(Operacja):
        def wykonaj(self, a, b):
            return a * b

    class Dzielenie(Operacja):
        def wykonaj(self, a, b):
            if b == 0:
                print("Nie można dzielić przez 0!")
                return float('inf')
            else:
                return a / b


# ZAD 2
def zad2():
    wejsciowy = input("Wprowadź ścieżkę do pliku wejściowego: ")
    wyjsciowy = input("Wprowadź ścieżkę do pliku wyjściowego: ")

    try:
        with open(wejsciowy, 'r') as file:
            linie = file.readlines()
            ilosc = len(linie)

        print(f"Liczba plików w pliku: {wejsciowy} to: {ilosc}")

        with open(wyjsciowy, 'w') as file:
            file.write(f"Nazwa pliku: {wejsciowy}.\nLiczba linii: {ilosc}")
    except FileNotFoundError:
        print("Nie można było znaleźć podanej ścieżki do pliku!")

# ZAD 3
def zad3():
    folder = input("Wprowadź ścieżkę do folderu: ")

    # Czas w sekundach, *60 - minuty, *60 - godziny, *24 - dni, *365 - lata
    czas = time.time() - (60 * 60 * 24 * 365)

    # Rozmiar w bajtach, *1024 - kilobajty, *1024 - megabajty
    rozmiar = 1 * 1024 * 1024

    try:
        for plik in os.listdir(folder):
            sciezka_plik = os.path.join(folder, plik)

            if os.path.getmtime(sciezka_plik) < czas and os.path.getsize(sciezka_plik) > rozmiar:
                os.remove(plik)
                print(f"Usunięto: {plik}")
    except FileNotFoundError:
        print("Nie można było znaleźć podanego folderu!")


if __name__ == "__main__":
    zad1()
    zad2()
    zad3()
