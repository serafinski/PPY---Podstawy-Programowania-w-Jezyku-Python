def zad1(a, b):
    a = float(a)
    b = float(b)
    dzialanie = input("Wprowadź: \n + - jeżeli chcesz dodać do siebie liczby"
                      "\n - - jeżeli chcesz odjąć liczby"
                      "\n * - jeżeli chcesz pomnożyć liczby"
                      "\n / - jeżeli chcesz podzielić liczby"
                      "\n\nTwój wybór:")
    if b == 0:
        return "B nie może być 0"
    else:
        if dzialanie == '+':
            return a + b
        elif dzialanie == '-':
            return a - b
        elif dzialanie == '*':
            return a * b
        elif dzialanie == '/':
            return a / b
        else:
            return "Wprowadzono nieprawidłowy znak!"


def zad2(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)

    if a > b > c:
        return a
    elif a < b and b > c:
        return b
    else:
        return c


def zad3(ciag_znakow):
    lista = list(ciag_znakow)
    rev = lista.reverse()
    concat = ''.join(lista)
    print(concat)


def zad4(liczba):
    wynik = 0
    if liczba == 0:
        wynik = 1
    else:
        wynik = liczba * zad4(liczba - 1)
    return wynik


# WYWOŁANIA
print(f"{zad1(1, 2)}\n")
print(f"Największa liczba to: {zad2(1, 2, 3)}\n")
zad3("123abcdef14")
print(f"\nSilnia to: {zad4(5)}")
