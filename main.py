from PIL import Image
import numpy as np
import tkinter as tk
from PIL import ImageGrab
from study import study

class DrawingApp:
    #coments
    def __init__(self, root):
        self.root = root
        self.root.title("Prosta aplikacja do rysowania")

        # Utwórz płótno do rysowania na interfejsie użytkownika
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        # Zmienne do śledzenia ostatniej pozycji myszki
        self.last_x = None
        self.last_y = None
        self.line_width = 2

        # Przypisanie funkcji rysowania i resetowania do odpowiednich zdarzeń myszki
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        # Przyciski do czyszczenia płótna i zapisywania rysunku
        clear_button = tk.Button(root, text="Wyczyść", command=self.clear_canvas)
        clear_button.pack()

        save_button = tk.Button(root, text="Zapisz", command=self.save_canvas)
        save_button.pack()

        # Suwak do regulacji grubości linii
        self.line_width_slider = tk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, label="Grubość linii", command=self.set_line_width)
        self.line_width_slider.pack()

    def draw(self, event):
        # Funkcja rysowania linii na płótnie
        x, y = event.x, event.y
        if self.last_x and self.last_y:
            self.canvas.create_line(self.last_x, self.last_y, x, y, fill="black", width=self.line_width)
        self.last_x = x
        self.last_y = y

    def reset(self, event):
        # Funkcja resetowania ostatniej pozycji myszki
        self.last_x = None
        self.last_y = None

    def clear_canvas(self):
        # Funkcja czyszczenia płótna
        self.canvas.delete("all")

    def save_canvas(self):
        # Funkcja zapisywania rysunku jako obrazu
        x = self.root.winfo_rootx() + self.canvas.winfo_rootx()
        y = self.root.winfo_rooty() + self.canvas.winfo_rooty()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()
        ImageGrab.grab(bbox=(x - 20, y - 20, x1 - 40, y1 -100)).save("imag.png")

    def set_line_width(self, value):
        # Funkcja ustawiania grubości linii
        self.line_width = int(value)

if __name__ == "__main__":
    # Tworzenie głównego okna aplikacji
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()

    # Otwieranie zapisanego obrazu
    image = Image.open('imag.png')
    image = image.convert('L')
    image_array = np.array(image)

    # Tworzenie nowej tablicy bez wszystkich białych linii
    new_array = []
    for i in image_array:
        if np.all(i == 255):
            pass
        else:
            new_array.append(i)

    # Konwersja tablicy na obraz i zapisanie go
    image_arrays = np.array(new_array, dtype=np.uint8)
    image = Image.fromarray(image_arrays)
    image.save("gfg_dummy_pic.png")

    # Pobieranie wprowadzonej liczby od użytkownika i wywołanie funkcji study
    x = input("Jaką liczbę wprowadziłeś? ")
    study(new_array, x)
