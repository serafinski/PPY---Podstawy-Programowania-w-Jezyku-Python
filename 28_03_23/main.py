# TOMASZ SERAFINSKI s24353, Grupa: 12c

# ZAD 1
def zad1():
    for i in range(1, 21):
        print(i)


# ZAD 2
def zad2():
    print()
    for i in range(5, 46, 5):
        print(i)


# ZAD 3
def zad3():
    print()
    for i in range(100, 49, -1):
        print(i)


# ZAD 4
def zad4():
    print()
    liczba_x = int(input("Wprowadź początek przedziału: "))
    liczba_y = int(input("Wprowadź koniec zakresu: "))

    for i in range(liczba_x, liczba_y + 1):
        print(i)


# ZAD 5
def zad5():
    liczba = int(input("Wprowadź liczbę: "))

    if liczba < 0 or liczba == 0:
        print("Prosze podać liczbę większą od 0!")
        zad5()
    else:
        print(f"Wprowadzono poprawną liczbę: {liczba}")


# ZAD 6
def zad6():
    x = int(input("Podaj początkową liczbę: "))
    y = int(input("Podaj końcową liczbę: "))
    suma = 0

    if x % 2 == 0:  # jeśli x jest parzyste, zwiększamy je o 1
        x += 1

    for i in range(x, y + 1, 2):  # iterujemy po liczbach nieparzystych od x do y
        suma += i

    print("Suma liczb nieparzystych od", x, "do", y, "wynosi", suma)


# WYWOŁANIA
zad1()
zad2()
zad3()
zad4()
zad5()
zad6()

