# Importuj moduł tkinter jako tk do GUI
import tkinter as tk


# Funkcja tworzącą suwak do wyboru liczby komórek
def create_slider_setting(parent, text, variable, min_value, max_value):
    # Stwórz etykietę z podanym tekstem
    label = tk.Label(parent, text=text)
    # Wyświetl etykietę
    label.pack()
    # Stwórz suwak z podanymi parametrami
    slider = tk.Scale(parent, from_=min_value, to=max_value, orient=tk.HORIZONTAL, variable=variable)
    # Wyświetl suwak
    slider.pack()


# Funkcję tworzącą ustawienia dla umierania i przeżycia
def create_setting(parent, text, variable):
    # Stwórz etykietę z podanym tekstem
    label = tk.Label(parent, text=text)
    # Wyświetl etykietę
    label.pack()
    # Stwórz pole wprowadzania tekstu z podanym parametrem
    entry = tk.Entry(parent, textvariable=variable)
    # Wyświetl pole wprowadzania tekstu
    entry.pack()


# Zdefiniuj klasę GameSettings
class GameSettings:
    # Zdefiniuj konstruktor klasy
    def __init__(self, parent):
        # Przypisz wartość argumentu do atrybutu klasy
        self.parent = parent
        # Zdefiniuj zmienną typu integer
        self.board_width = tk.IntVar()
        # Zdefiniuj zmienną typu integer
        self.board_height = tk.IntVar()
        # Zdefiniuj zmienną typu integer
        self.update_speed = tk.IntVar()
        # Zdefiniuj zmienną typu string
        self.birth_rule = tk.StringVar()
        # Zdefiniuj zmienną typu string
        self.survival_rule = tk.StringVar()

        # Ustaw default wartość zmiennej na 50
        self.board_width.set(50)
        # Ustaw default wartość zmiennej na 50
        self.board_height.set(50)
        # Ustaw default wartość zmiennej na 100
        self.update_speed.set(100)
        # Ustaw default wartość zmiennej na "3"
        self.birth_rule.set("3")
        # Ustaw default wartość zmiennej na "2,3"
        self.survival_rule.set("2,3")

        # Wywołaj funkcję inicjalizującą ustawienia
        self.initialize_settings()

    # Funkcja inicjalizującą ustawienia
    def initialize_settings(self):
        # Stwórz suwaki z podanymi parametrami
        create_slider_setting(self.parent, "Number of cells horizontally:", self.board_width, 10, 150)
        create_slider_setting(self.parent, "Number of cells vertically:", self.board_height, 10, 150)
        create_slider_setting(self.parent, "Update Speed (ms):", self.update_speed, 1, 2000)

        # Stwórz ustawienia z podanymi parametrami
        create_setting(self.parent, "Birth Rule:", self.birth_rule)
        create_setting(self.parent, "Survival Rule:", self.survival_rule)

    # Zdefiniuj funkcję zwracającą ustawienia
    def get_settings(self):
        return (
            # Zwróć wartość zmiennej
            self.board_width.get(),
            # Zwróć wartość zmiennej
            self.board_height.get(),
            # Zwróć wartość zmiennej
            self.update_speed.get(),
            # Lista birth rules
            [int(rule) for rule in self.birth_rule.get().split(",")],
            # Lista survival rules
            [int(rule) for rule in self.survival_rule.get().split(",")],
        )
