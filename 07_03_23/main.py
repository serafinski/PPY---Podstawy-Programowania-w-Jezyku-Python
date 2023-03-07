#
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
