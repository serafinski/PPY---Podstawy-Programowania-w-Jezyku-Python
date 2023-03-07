#TOMASZ SERAFINSKI s24353, Grupa: 12c

#ZADANIE1
#test 1 -kalkulator
liczba1 = input("Wprowadz pierwsza liczbe: \n")
operacja = input("Wprowadz znak operacji: \n")
liczba2 =input("Wprowadz druga liczbe: \n")
print()

if operacja == "+":
    print(int(liczba1)+int(liczba2))
elif operacja == "-":
    print(int(liczba1)-int(liczba2))
elif operacja == "*":
    print(int(liczba1)*int(liczba2))
elif operacja == "/":
    print(int(liczba1)/int(liczba2))
else:
    print("Wprowadzono nieprawidlowa operacje!")

#ZADANIE 2
imie = input("Wprowadz imie:\n")
while not imie.isalpha():
    print("Prosze wprowadzic ciag znakow!")
    imie = input("Wprowadz imie:\n")

wzrost = input("Wprowadz wzrost:\n")
while not wzrost.isdigit():
    print("Prosze wprowadzic liczbe!")
    wzrost = input("Wprowadz wzrost:\n")

wiek = input("Wprowadz wiek:\n")
while not wiek.isdigit():
    print("Prosze wprowadzic liczbe!")
    wiek = input("Wprowadz wiek:\n")

kolor_oczu = input("Wprowadz kolor oczu:\n")
while not kolor_oczu.isalpha():
    print("Prosze wprowadzic ciag znakow!")
    kolor_oczu = input("Wprowadz kolor oczu:\n")

kolor_wlosow = input("Wprowadz kolor wlosow:\n")
while not kolor_wlosow.isalpha():
    print("Prosze wprowadzic ciag znakow!")
    kolor_wlosow = input("Wprowadz kolor wlosow:\n")

print()
print("TWOJ KWESTIONARIUSZ")
print("Imie: " + imie)
print("Wzrost: " + wzrost)
print("Wiek: " + wiek)
print("Kolor oczu: " + kolor_oczu)
print("Kolor wlosow: " + kolor_wlosow)