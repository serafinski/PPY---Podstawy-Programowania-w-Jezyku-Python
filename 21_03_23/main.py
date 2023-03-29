# TOMASZ SERAFINSKI s24353, Grupa: 12c


# BEZ używania pętli wyznaczyć element listy, który powtarza się najczęściej.
lista = [4, 4, 4, 2, 2, 3, 5, 6, 7, 8, 7, 5, 4, 3, 2, 4]
najczestrzy_element = max(set(lista), key=lista.count)
print("Najczęstszy element: " + str(najczestrzy_element))

# Napisz program w Pythonie, aby utworzyć krotkę.
krotka = ("Tomasz", "Jan", "Mateusz")

#  Napisz program w Pythonie, aby utworzyć krotkę z różnymi typami danych.
zlozona = ("Tomasz", 24, "Jan", [17, 15, 16])

# Napisz program w Pythonie, który utworzy krotkę liczb i wyświetli tylko jeden element.
liczby = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
wybrana_liczba = 7
print("Indeks liczby " + str(wybrana_liczba) + " to: " + str(liczby.index(7)))

# Napisz program w Pythonie, aby przekonwertować krotkę na słownik.
przekonwertowana = dict(zip(range(len(liczby)), liczby))
print(przekonwertowana)

# Napisz program, w którym będą wykonywanie operacje dodawania i odejmowania na liczbach całkowitych.
pierwsza = input("Wprowadź pierwszą liczbę: ")
decyzja = input("Wybierz czy chcesz odjąć (wpisz: 'o') lub dodać (wpisz: 'd'): ")
druga = input("Wprowadź drugą liczbę: ")

if str(decyzja).lower() == 'o':
    wynik = int(pierwsza) - int(druga)
    print("Wynik: " + str(wynik))
elif str(decyzja).lower() == 'd':
    wynik = int(pierwsza) + int(druga)
    print("Wynik: " + str(wynik))
else:
    print("Nie wprowadzono prawidłowej opcji!")

# Napisz program imitujący dialog dwóch postaci.
print("\nWpisz 'STOP' by zakończyć konwersacje")

while True:
    osoba1 = input("[OSOBA 1]: ")
    if osoba1.upper() == "STOP":
        print("Koniec konwersacji!")
        break
    osoba2 = input("[OSOBA 2]: ")
    if osoba2.upper() == "STOP":
        print("Koniec konwersacji!")
        break
