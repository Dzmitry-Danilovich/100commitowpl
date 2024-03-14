import tkinter as tk
from PIL import ImageGrab

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Prosta aplikacja do rysowania")

        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        self.last_x = None
        self.last_y = None

        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        clear_button = tk.Button(root, text="Wyczyść", command=self.clear_canvas)
        clear_button.pack()

        save_button = tk.Button(root, text="Zapisz", command=self.save_canvas)
        save_button.pack()

    def draw(self, event):
        x, y = event.x, event.y
        if self.last_x and self.last_y:
            self.canvas.create_line(self.last_x, self.last_y, x, y, fill="black", width=2)
        self.last_x = x
        self.last_y = y

    def reset(self, event):
        self.last_x = None
        self.last_y = None

    def clear_canvas(self):
        self.canvas.delete("all")

    def save_canvas(self):
        x = self.root.winfo_rootx() + self.canvas.winfo_rootx()
        y = self.root.winfo_rooty() + self.canvas.winfo_rooty()
        x1 = x + self.canvas.winfo_width() - 10
        y1 = y + self.canvas.winfo_height() - 55
        ImageGrab.grab(bbox=(x, y, x1, y1)).save("imag.png")

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
