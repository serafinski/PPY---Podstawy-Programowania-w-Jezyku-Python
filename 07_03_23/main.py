#TOMASZ SERAFINSKI s24353

#test 1 -kalkulator
# liczba1 = input("Wprowadz pierwsza liczbe: \n")
# operacja = input("Wprowadz znak operacji: \n")
# liczba2 =input("Wprowadz druga liczbe: \n")
# print()
#
# if operacja == "+":
#     print(int(liczba1)+int(liczba2))
# elif operacja == "-":
#     print(int(liczba1)-int(liczba2))
# elif operacja == "*":
#     print(int(liczba1)*int(liczba2))
# elif operacja == "/":
#     print(int(liczba1)/int(liczba2))
# else:
#     print("Wprowadzono nieprawidlowa operacje!")

#
#imie
imie = input("Wprowadz imie:\n")
if not imie.isalpha():
    print("Prosze wprowadzic ciag znakow!")
#wzrost
wzrost = input("Wprowadz wzrost:\n")
if not wzrost.isdigit():
    print("Prosze wprowadzic liczbe!")
#wiek
wiek = input("Wprowadz wiek:\n")
if not wiek.isdigit():
    print("Prosze wprowadzic liczbe!")
#kolor_oczu
kolor_oczu = input("Wprowadz kolor oczu:\n")
if not kolor_oczu.isalpha():
    print("Prosze wprowadzic ciag znakow!")
#kolor_wlosow
kolor_wlosow = input("Wprowadz kolor wlosow:\n")
if not kolor_wlosow.isalpha():
    print("Prosze wprowadzic ciag znakow!")

print()
print("TWOJ KWESTIONARIUSZ")
print("Imie: " + imie)
print("Wzrost: " + wzrost)
print("Wiek: " + wiek)
print("Kolor oczu: " + kolor_oczu)
print("Kolor wlosow: " + kolor_wlosow)