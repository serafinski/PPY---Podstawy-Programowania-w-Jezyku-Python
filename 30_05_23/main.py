# TOMASZ SERAFIŃSKI s24353, Grupa: 12c
import random as rnd


# ZAD 1
def zad1():
    wynik = rnd.randint(1, 6)
    print(f"Wyrzucono: {wynik}")


# ZAD 2
def zad2():
    haslo = "test1234"

    haslo_user = input("Wprowadź hasło: ")

    if haslo_user != haslo:
        print("Wprowadzono nieprawidłowe hasło! ")
        zad2()
    else:
        print("Wprowadzono prawidłowe hasło! Witamy!")


# ZAD 3
def zad3():
    class User:
        def __init__(self, username, password, lvl):
            self.username = username
            self.password = password
            self.lvl = lvl

        def check_password(self, inputed_password):
            return self.password == inputed_password

    def loggin_in(users):
        login_user = input("Wprowadź login: ")
        haslo_user = input("Wprowadź hasło: ")

        for user in users:
            if user.username == login_user:
                if user.check_password(haslo_user):
                    return user

        return None

    admin = User("admin", "safepassword1234", 3)
    user1 = User("usr1", "password1", 2)
    user2 = User("usr2", "password2", 1)
    user3 = User("usr3", "password3", 1)

    users = [admin, user1, user2, user3]

    logged_in_user = loggin_in(users)

    if logged_in_user is None:
        print("Wprowadzono nieprawidłowe hasło! ")
        zad3()
    else:
        print(
            f"Wprowadzono prawidłowe hasło! Witamy \"{logged_in_user.username}\"! Twój poziom uprawnień to {logged_in_user.lvl}!")


# ZAD 4
def zad4():
    nr = rnd.randint(1, 4)

    match nr:
        case 1:
            print("Twoja determinacja otworzy przed Tobą nowe możliwości i osiągniesz wielki sukces.")
        case 2:
            print("Nadchodzi okres zmian. Bądź gotowy na wyzwania, które przyniosą Ci ostateczne spełnienie.")
        case 3:
            print("Twoja intuicja będzie Twoim przewodnikiem w najbliższych dniach. Słuchaj jej uważnie.")
        case 4:
            print("Za chmurami słońce zawsze świeci. Niezależnie od trudności, twoje szczęście jest na horyzoncie.")


# ZAD 5
def zad5():
    orzel_counter = 0
    reszka_counter = 0

    for i in range(100):
        nr = rnd.randint(1, 2)

        if nr == 1:
            orzel_counter += 1
        else:
            reszka_counter += 1

    print(f"Liczba orłów: {orzel_counter}")
    print(f"Liczba reszek: {reszka_counter}")


# ZAD 6
def zad6():
    class TV:
        def __init__(self):
            self.chanel = 1
            self.volume = 50

        def chanel_change(self, nr):
            self.chanel = nr

            if nr < 0:
                self.chanel = 1

        def volume_up(self):
            if self.volume < 100:
                self.volume += 1
            else:
                print(f"Głośność: {100}")

        def volume_down(self):
            if self.volume > 0:
                self.volume -= 1
            else:
                print(f"Głośność: {0}")

    tv = TV()

    while True:
        print("Kanał:", tv.chanel)
        print("Głośność:", tv.volume)
        print("\n0. Zmień kanał")
        print("+. Zwiększ głośność")
        print("-. Zmniejsz głośność")
        print("X. Wyłącz telewizor")

        opcja = input("\nOpcja: ")

        if opcja == "0":
            nr = int(input("Wprowadź numer kanału: "))
            tv.chanel_change(nr)
        elif opcja == "+":
            tv.volume_up()
        elif opcja == "-":
            tv.volume_down()
        elif opcja == "X":
            break
        else:
            print("Nieprawidłowa opcja. Wybierz ponownie.")


# WYWOŁANIA
if __name__ == "__main__":
    zad1()
    zad2()
    zad3()
    zad4()
    zad5()
    zad6()
