# Importuj moduł sys do obsługi operacji systemowych
import sys
# Importuj moduł tkinter jako tk do GUI
import tkinter as tk
# Importy
from game_settings import GameSettings
from game_of_life_gui import GameOfLifeGUI


# Metoda statyczna — służąca do wyjścia z programu
def exit_program():
    sys.exit()


# Definiuj klasę StartScreen jako podklasę klasy Tk z modułu tkinter
class StartScreen(tk.Tk):
    # Definiuj konstruktor klasy
    def __init__(self):
        # Wywołaj konstruktor klasy bazowej
        super().__init__()
        # Ustaw tytuł okna
        self.title("Game of Life - Start Screen")
        # Inicjalizuj obiekt klasy GameSettings
        self.game_settings = GameSettings(self)

        # Utwórz zmienną logiczną
        self.randomize = tk.BooleanVar()
        # Ustaw wartość zmiennej mówiącej o randomizacji default'owo na True
        self.randomize.set(True)

        # Utwórz przycisk wyboru odpalający randomizacje
        self.randomize_checkbutton = tk.Checkbutton(self, text="Randomize cells", variable=self.randomize)
        # Dodaj przycisk do okna
        self.randomize_checkbutton.pack()

        # Utwórz przycisk startu
        self.start_button = tk.Button(self, text="Start", command=self.start_game)
        # Dodaj przycisk do okna
        self.start_button.pack()

        # Utwórz przycisk do zakończenia programu
        self.exit_button = tk.Button(self, text="Exit", command=exit_program)
        # Dodaj przycisk do okna
        self.exit_button.pack()

        # Inicjalizuj menu
        self.initialize_menu()
        # Wycentruj okno
        self.center_window()
        # Ustaw okno na nieskalowalne
        self.resizable(False, False)
        # Przypisz funkcję zakończenia programu do zdarzenia zamknięcia okna
        self.protocol("WM_DELETE_WINDOW", exit_program)

    # Definiuj funkcję do wycentrowania okna
    def center_window(self):
        # Pobierz wymagana szerokość okna
        window_width = self.winfo_reqwidth()
        # Pobierz wymagana wysokość okna
        window_height = self.winfo_reqheight()
        # Oblicz pozycję okna od prawej strony
        position_right = int(self.winfo_screenwidth() / 2 - window_width / 2)
        # Oblicz pozycję okna od dołu strony
        position_down = int(self.winfo_screenheight() / 2 - window_height / 2)
        # Ustaw pozycję okna
        self.geometry("+{}+{}".format(position_right, position_down))

    # Definiuj funkcję do inicjalizacji menu
    def initialize_menu(self):
        # Utwórz menu
        self.menu = tk.Menu(self)
        # Skonfiguruj menu
        self.configure(menu=self.menu)
        # Utwórz podmenu
        self.game_rules_menu = tk.Menu(self.menu)
        # Dodaj podmenu z zasadami gry do menu
        self.menu.add_cascade(label="Game Rules", menu=self.game_rules_menu)
        # Dodaj polecenie do podmenu pozwalające na wyjście z programu
        self.game_rules_menu.add_command(label="Exit", command=exit_program)

    # Definiuj funkcję do uruchomienia gry
    def start_game(self):
        # Pobierz ustawienia gry
        board_width, board_height, update_speed, birth_rule, survival_rule = self.game_settings.get_settings()
        # Ukryj okno startowe
        self.withdraw()
        # Inicjalizuj obiekt klasy GameOfLifeGUI
        game = GameOfLifeGUI(board_width, board_height, update_speed, birth_rule, survival_rule, self.randomize.get(),
                             self)
        # Uruchom główną pętlę gry
        game.mainloop()
