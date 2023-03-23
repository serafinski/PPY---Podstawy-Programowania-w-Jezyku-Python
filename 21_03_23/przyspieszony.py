# TOMASZ SERAFIŃSKI s24353, Grupa: 12c


# ZAD 1
def zad1():
    imie = input("Wprowadź imię: ")
    data_urodzenia = input("Wprowadź datę urodzenia: ")
    email = input("Wprowadź adres e-mail: ")
    telefon = input("Wprowadź numer telefonu: ")

    lista = [imie, data_urodzenia, email, telefon]
    print(lista)
    krotka = (imie, data_urodzenia, email, telefon)
    print(krotka)
    slownik = {
        "Imie": imie,
        "Data urodzenia": data_urodzenia,
        "E-mail": email,
        "Telefon": telefon
    }
    print(slownik)


# ZAD 2
def zad2():
    def czy_jest_pierwsza(liczba):
        # mniej niż 1 lub 1
        if liczba <= 1:
            return False
        # mniejsze równe 3
        elif liczba <= 3:
            return True
        # podzielne przez 2 i przez 3
        elif liczba % 2 == 0 or liczba % 3 == 0:
            return False
        # każda liczba pierwsza to 6k+1 lub 6k-1 - twierdzenie Dirichleta
        i = 5
        while i * i <= liczba:
            if liczba % i == 0 or liczba % (i + 2) == 0:
                return False
            i += 6
        return True

    # 20 liczb między -20 i 20
    liczby = []
    counter = 0
    while counter < 20:
        liczba = int(input("Wprowadź liczbę między -20 i 20: "))
        if -20 <= liczba <= 20:
            liczby.append(liczba)
            counter += 1

    # kopia
    liczby_kopia = liczby.copy()

    # Krotka z liczbami pierwszymi
    liczby_pierwsze = tuple(filter(czy_jest_pierwsza, liczby_kopia))

    # Kwadraty parzystych
    squares = tuple([n ** 2 for n in liczby if n % 2 == 0])

    def zamiana(lista):
        if not lista:
            return []
        else:
            liczba_w_liscie, *reszta_listy = lista
            if liczba_w_liscie % 2 == 0:
                return ['A'] + zamiana(reszta_listy)
            else:
                return [liczba_w_liscie] + zamiana(reszta_listy)

    # Zamiana
    zamianione = zamiana(liczby)

    print("Orginalna lista: ", liczby)
    print("Kopia listy: ", liczby_kopia)
    print("Liczby pierwsze: ", liczby_pierwsze)
    print("Kwadraty parzystych: ", squares)
    print("Parzyste zamieninione na 'A': ", zamianione)


# ZAD 3
def zad3():
    rozmiar_tabliczki = int(input("Wpisz rozmiar tabliczki: "))

    # Nagłówek
    print("  ", end="")
    for i in range(1, rozmiar_tabliczki + 1):
        # i:3 -> co 3 znaki (jak nie będzie 3 cyfrowej liczby to dopełni ją spacjami)
        print(f"{i:3}", end="")
    print()

    # Kreska
    print("--" + "---" * rozmiar_tabliczki)

    # Rzędy
    for i in range(1, rozmiar_tabliczki + 1):
        print(f"{i:2}|", end="")
        for j in range(1, rozmiar_tabliczki + 1):
            result = i * j
            print(f"{result:3}", end="")
        print()


# ZAD 4
def zad4():
    lista_liczb = []
    x = int(input("Wprowadź liczbę: "))
    n = 0

    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    while True:
        c_n = factorial(2 * n) / (factorial(n + 1) * factorial(n))
        if c_n > x:
            break

        lista_liczb.append(c_n)
        n += 1

    return print(lista_liczb)


# ZAD 5 - nie skończone!!!
def zad5():
    lista_produktow = []

    def dodaj_produkt():
        nazwa = input("Wprowadź nazwę produktu: ")
        ilosc = int(input("Wprowadź ilość produktu: "))
        cena = float(input("Wprowadź cenę produktu: "))
        produkt = {
            "Nazwa": nazwa,
            "Ilość": ilosc,
            "Cena": cena
        }
        lista_produktow.append(produkt)
        print("Dodano nowy produkt!")

    def usun_produkt():
        nazwa = input("Wprowadź nazwę produktu: ")
        for produkt in lista_produktow:
            if produkt["nazwa"] == nazwa:
                lista_produktow.remove(produkt)
                print("Usunięto produkt!")
                break
            else:
                print("Nie znaleziono podanego produktu!")
