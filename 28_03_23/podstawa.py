# ZAD 1
def zad1():
    liczba = int(input("Wprowadź liczbę: "))
    odwrocona = 0

    while liczba > 0:
        digit = liczba % 10
        odwrocona = (odwrocona * 10) + digit
        liczba = liczba // 10

    print("Odwrócona liczba:", odwrocona)


# ZAD 2
def zad2():
    for i in range(1, 16):
        print(i * 3)


# ZAD 3
def zad3():
    liczba = int(input("Wprowadź liczbę: "))
    for i in range(1, liczba + 1):
        if liczba % i == 0:
            print(i)


# ZAD 4
def zad4():
    bok_n = int(input("Wprowadź bok n: "))
    bok_m = int(input("Wprowadź bok m: "))
    print()
    for i in range(bok_n):
        for j in range(bok_m):
            print("*", end="")
        print()


# WYWOŁANIA
zad1()
zad2()
zad3()
zad4()
