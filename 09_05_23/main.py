# TOMASZ SERAFIŃSKI s24353, Grupa: 12c

# ZAD 1
def wypisz_imie_i_wiek(imie, wiek):
    print("Imię:", imie)
    print("Wiek:", wiek)


# ZAD 2
def func1(*args):
    for arg in args:
        print("Wartość:", arg)


# ZAD 3
def obliczanie(x, y):
    dodawanie = x + y
    odejmowanie = x - y
    return dodawanie, odejmowanie


# ZAD 4
def show_employee(nazwisko, wynagrodzenie=9000):
    print("Nazwisko:", nazwisko)
    print("Wynagrodzenie:", wynagrodzenie)


# ZAD 5
def pole(a, b):
    pole = a * b
    return pole


# ZAD 6
def trojkapitagorejska(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False


if __name__ == "__main__":
    # ZAD 1
    wypisz_imie_i_wiek("Tomasz", 24)

    # ZAD 2
    func1("Test", 1999, True)

    # ZAD 3
    zad3 = obliczanie(4, 2)
    print("Dodawanie:", zad3[0])
    print("Odejmowanie:", zad3[1])

    # ZAD 4
    show_employee("Serafinski")

    # ZAD 5
    print(pole(2, 10))

    # ZAD 6
    a = float(input("Wprowadź a: "))
    b = float(input("Wprowadź b: "))
    c = float(input("Wprowadź c: "))
    zad6 = trojkapitagorejska(a,b,c)
    print(zad6)
