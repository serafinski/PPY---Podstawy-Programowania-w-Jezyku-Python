# Importuj moduł sys do obsługi operacji systemowych
import sys
# Importuj moduł tkinter jako tk do GUI
import tkinter as tk
# Importuj moduł random do randomizowania komórek (generowania liczb losowych)
import random
# Importuj moduł copy do głębokich kopii struktur danych — potrzebne do obliczeń następnej generacji
import copy


# Funkcja tworząca przycisk
def create_button(parent, text, command):
    # Tworzenie przycisku o określonym tekście i komendzie, szerokość 10, wysokość 2
    button = tk.Button(parent, text=text, command=command, width=10, height=2)
    # Dodaj przycisk do interfejsu użytkownika
    button.pack(side="top", pady=5)
    # Zwróć stworzony przycisk
    return button


# Definicja klasy GameOfLifeGUI, która dziedziczy po klasie tk.Tk
class GameOfLifeGUI(tk.Tk):
    def __init__(self, BOARD_WIDTH, BOARD_HEIGHT, update_speed, birth_rule, survival_rule, randomize, start_screen):
        # Wywołaj konstruktor klasy nadrzędnej tk.Tk
        super().__init__()
        # Zmienna określająca, czy komórki mają być losowo ustawiane na planszy
        self.randomize = randomize
        # Rozmiar komórki
        self.cell_size = 10
        # Tytuł okna
        self.title("Game of Life")

        # Zasady narodzin komórek
        self.birth_rule = birth_rule
        # Zasady przetrwania komórek
        self.survival_rule = survival_rule
        # Okno startowe gry
        self.start_screen = start_screen
        # Szybkość aktualizacji planszy
        self.update_speed = update_speed

        # Inicjalizacja planszy i następnej planszy
        self.board = []
        self.next_board = []

        # Szerokość i wysokość planszy
        self.BOARD_WIDTH = BOARD_WIDTH
        self.BOARD_HEIGHT = BOARD_HEIGHT
        # Wyłączenie możliwości zmiany rozmiaru okna
        self.resizable(False, False)

        # Pobranie szerokości i wysokości ekranu
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Obliczenie rozmiaru komórki na podstawie rozmiaru ekranu
        self.cell_size = min(10, min(screen_width // BOARD_WIDTH, screen_height // BOARD_HEIGHT))

        # Tworzenie "płótna" do rysowania planszy
        self.canvas = tk.Canvas(self, width=self.BOARD_WIDTH * self.cell_size,
                                height=self.BOARD_HEIGHT * self.cell_size,
                                borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="right", fill=tk.BOTH, expand=True)

        # Przywiązanie funkcji do kliknięcia i przeciągnięcia myszką na płótnie
        self.canvas.bind("<Button-1>", self.click_cell)
        self.canvas.bind("<B1-Motion>", self.click_cell)

        # Inicjalizacja przycisków
        self.initialize_buttons()

        # Status gry
        self.is_running = False
        self.update_speed = update_speed
        self.game_running = False

        # Wycentrowanie okna na ekranie
        self.center_window()

        # Inicjalizacja planszy
        self.initialize_board()
        # Rysowanie planszy
        self.draw_board()
        # Przypisz funkcję zakończenia programu do zdarzenia zamknięcia okna
        self.protocol("WM_DELETE_WINDOW", self.exit_game)

    # Kliknięcie na komórkę
    def click_cell(self, event):
        # Jeżeli randomizacja jest wyłączona
        if not self.randomize:
            # Obliczenie indeksów komórki na podstawie pozycji kursora
            x = int(event.x / self.cell_size)
            y = int(event.y / self.cell_size)

            # Jeżeli kliknięcie jest w granicach planszy
            if 0 <= x < self.BOARD_WIDTH and 0 <= y < self.BOARD_HEIGHT:
                # Zmiana stanu komórki na żywą
                self.board[y][x] = 1
                # Przerysowanie planszy
                self.draw_board()

    # Inicjalizacja przycisków
    def initialize_buttons(self):
        # Tworzenie linii pionowej — oddzielenie przycisków od planszy, na której da się rysować
        vertical_line = tk.Frame(self, bg="red", width=1)
        vertical_line.pack(side="right", fill="y")

        # Tworzenie ramki dla przycisków
        button_frame = tk.Frame(self)
        button_frame.pack(side="right", fill="y")

        # Tworzenie przycisków i przypisywanie im odpowiednich funkcji
        self.start_button = create_button(button_frame, "Start", self.start_game)
        self.pause_button = create_button(button_frame, "Pause", self.pause_game)
        self.reset_button = create_button(button_frame, "Reset", self.reset_game)
        self.menu_button = create_button(button_frame, "Menu", self.return_to_menu)
        self.exit_button = create_button(button_frame, "Exit", self.exit_game)

    # Funkcja wyjścia z gry
    def exit_game(self):
        # Zniszczenie okna
        self.destroy()
        # Wyjście z programu
        sys.exit()

    # Rysowanie planszy
    def draw_board(self):
        # Usunięcie poprzedniego rysunku
        self.canvas.delete("all")
        # Przejście po wszystkich komórkach planszy
        for i in range(self.BOARD_WIDTH):
            for j in range(self.BOARD_HEIGHT):

                # Jeżeli komórka jest żywa
                if self.board[j][i] == 1:
                    # Narysuj kwadrat reprezentujący komórkę na płótnie
                    self.canvas.create_rectangle(i * self.cell_size, j * self.cell_size,
                                                 (i + 1) * self.cell_size, (j + 1) * self.cell_size,
                                                 fill="green")

    # Wycentrowanie okna na ekranie
    def center_window(self):
        # Aktualizacja zadań interfejsu użytkownika
        self.update_idletasks()
        # Pobranie szerokości i wysokości okna
        width = self.winfo_width()
        height = self.winfo_height()

        # Obliczenie pozycji okna, tak by było wyśrodkowane na ekranie
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        # Ustawienie pozycji okna
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    # Rozpoczęcie gry
    def start_game(self):
        # Jeżeli gra nie jest już uruchomiona
        if not self.game_running:
            # Zmiana statusu gry na uruchomioną
            self.is_running = True
            self.game_running = True

            # Wyłączenie przycisku startu
            self.start_button["state"] = "disabled"
            # Włączenie przycisku pauzy
            self.pause_button["state"] = "normal"
            # Wyłączenie przycisku resetu
            self.reset_button["state"] = "disabled"
            # Wyłączenie przycisku menu
            self.menu_button["state"] = "disabled"

            # Rozpoczęcie aktualizacji gry
            self.update_game()

    # Pauzowanie gry
    def pause_game(self):
        # Jeżeli gra jest uruchomiona
        if self.game_running:
            # Zmiana statusu gry na zatrzymaną
            self.is_running = False
            self.game_running = False
            # Włączenie przycisku startu
            self.start_button["state"] = "normal"
            # Wyłączenie przycisku pauzy
            self.pause_button["state"] = "disabled"
            # Włączenie przycisku resetu
            self.reset_button["state"] = "normal"
            # Włączenie przycisku menu
            self.menu_button["state"] = "normal"

    # Resetowanie gry
    def reset_game(self):
        # Jeżeli gra jest zatrzymana
        if not self.is_running:
            # Inicjalizacja (nowej) planszy
            self.initialize_board()
            # Rysowanie (nowej) planszy
            self.draw_board()

    # Powrót do menu
    def return_to_menu(self):
        # Jeżeli gra jest zatrzymana
        if not self.is_running:
            # Zniszczenie okna
            self.destroy()
            # Pokazanie okna startowego
            self.start_screen.deiconify()
            self.start_screen.update()

    # Aktualizacja gry
    def update_game(self):
        # Jeżeli gra jest uruchomiona
        if self.is_running:
            # Obliczenie następnego pokolenia
            self.calculate_next_generation()
            # Rysowanie planszy
            self.draw_board()
            # Jeżeli gra jest uruchomiona
            if self.game_running:
                # Wywołanie funkcji po upływie określonego czasu
                self.after(self.update_speed, self.update_game)

    # Inicjalizacja planszy
    def initialize_board(self):
        # Tworzenie pustej planszy
        self.board = [[0] * self.BOARD_WIDTH for _ in range(self.BOARD_HEIGHT)]

        # Jeżeli komórki mają być losowane
        if self.randomize:
            # Przejście po wszystkich komórkach planszy
            for i in range(self.BOARD_HEIGHT):
                for j in range(self.BOARD_WIDTH):
                    # Losowanie stanu komórki
                    self.board[i][j] = random.randint(0, 1)

    # Obliczanie następnego pokolenia
    def calculate_next_generation(self):
        # Głęboka kopia planszy do obliczeń — upewnienie się, że następna tablica jest kompletnie odrębny od oryginału.
        # Gdybyśmy zrobili "płytką" kopię — zmiany byłyby odzwierciedlane na oryginalnej tablicy.

        # Dostalibyśmy nieprawidłowe obliczenia — a tak:
        # aktualizacje dokonane w jednej komórce nie wpływają na aktualizację innej komórki w tym samym kroku!
        self.next_board = copy.deepcopy(self.board)
        # Przejście po wszystkich komórkach planszy
        for i in range(self.BOARD_WIDTH):
            for j in range(self.BOARD_HEIGHT):
                # Obliczenie liczby żywych sąsiadów
                alive_neighbors = self.count_alive_neighbors(i, j)

                # Jeżeli komórka jest żywa
                if self.board[j][i] == 1:
                    # Jeżeli komórka nie spełnia warunków przetrwania
                    if alive_neighbors not in self.survival_rule:
                        # Zmieniamy stan komórki na martwą
                        self.next_board[j][i] = 0
                else:
                    # Jeżeli liczba sąsiadów spełnia warunki narodzin
                    if alive_neighbors in self.birth_rule:
                        # Zmieniamy stan komórki na żywą
                        self.next_board[j][i] = 1

        # Zamiana aktualnej planszy na następną planszę
        self.board = copy.deepcopy(self.next_board)

    # Obliczanie żywych sąsiadów
    def count_alive_neighbors(self, x, y):
        # Inicjalizacja liczby żywych sąsiadów
        alive_neighbors = 0
        # Przeszukiwanie sąsiadujących komórek
        for i in range(-1, 2):
            for j in range(-1, 2):
                # Ustalamy pozycję sąsiada z uwzględnieniem granic planszy
                neighbor_x = (x + i + self.BOARD_WIDTH) % self.BOARD_WIDTH
                neighbor_y = (y + j + self.BOARD_HEIGHT) % self.BOARD_HEIGHT
                # Zwiększamy liczbę żywych sąsiadów o stan sąsiada
                alive_neighbors += self.board[neighbor_y][neighbor_x]
        # Odejmujemy od liczby żywych sąsiadów stan badanej komórki
        alive_neighbors -= self.board[y][x]

        # Zwracamy liczbę żywych sąsiadów
        return alive_neighbors
