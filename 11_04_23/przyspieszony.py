# TOMASZ SERAFINSKI s24353, Grupa: 12c

from math import factorial


# ZAD 1
# Dowolna liczba arg wiec *args
def liczby_doskonale(*args):
    rezultat = {}

    for liczba in args:
        dzielniki = []

        # Znajdź dzielniki liczby -> // dzielenie z zaokrąglaniem w dół
        for i in range(1, liczba // 2 + 1):
            if liczba % i == 0:
                dzielniki.append(i)

        # Suma dzielników
        suma = sum(dzielniki)

        # Sprawdzenie, czy jest liczbą doskonałą
        rezultat[liczba] = suma == liczba

    return rezultat


# ZAD 2
def liczby_katalana(N, condition='a'):
    # Wzór: C_n = (2n)! / ((n + 1)! * n!)
    def policz(n):
        return factorial(2 * n) // (factorial(n + 1) * factorial(n))

    for i in range(N):
        katalan = policz(i)

        if condition == 'a':
            print(katalan)
        elif condition == 'p' and katalan % 2 == 0:
            print(katalan)
        elif condition == 'n' and katalan % 2 == 1:
            print(katalan)

# Wywołania
# ZAD 1
print(liczby_doskonale(6, 28, 15, 496))
# ZAD 2
liczby_katalana(10, 'n')  # nieparzyste
