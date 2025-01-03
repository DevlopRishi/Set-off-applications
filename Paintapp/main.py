import tkinter as tk
from tkinter import colorchooser, filedialog
from PIL import Image, ImageDraw, ImageTk

class ModernPaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Paint Application")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

        self.brush_color = "#000000"
        self.brush_size = 5

        # Canvas setup
        self.canvas = tk.Canvas(root, bg="white", relief="ridge", bd=2, highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Bind mouse events
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        # Create an empty PIL image for saving
        self.image = Image.new("RGB", (800, 600), "white")
        self.draw = ImageDraw.Draw(self.image)

        # Toolbar setup
        self.create_toolbar()

        # Variable to track the last drawn point
        self.last_x, self.last_y = None, None

    def create_toolbar(self):
        toolbar = tk.Frame(self.root, bg="#d9d9d9", relief="flat")
        toolbar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        tk.Button(toolbar, text="Color", command=self.choose_color, bg="#ffffff", relief="flat", width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(toolbar, text="Save", command=self.save_image, bg="#ffffff", relief="flat", width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(toolbar, text="Clear", command=self.clear_canvas, bg="#ffffff", relief="flat", width=10).pack(side=tk.LEFT, padx=5)

        size_label = tk.Label(toolbar, text="Brush Size:", bg="#d9d9d9")
        size_label.pack(side=tk.LEFT, padx=5)

        self.brush_size_slider = tk.Scale(toolbar, from_=1, to=20, orient=tk.HORIZONTAL, bg="#d9d9d9", relief="flat")
        self.brush_size_slider.set(self.brush_size)
        self.brush_size_slider.pack(side=tk.LEFT, padx=5)

    def choose_color(self):
        color_code = colorchooser.askcolor(title="Choose Brush Color")
        if color_code:
            self.brush_color = color_code[1]

    def paint(self, event):
        x, y = event.x, event.y
        size = self.brush_size_slider.get()

        if self.last_x is not None and self.last_y is not None:
            self.canvas.create_oval(x-size, y-size, x+size, y+size, fill=self.brush_color, outline="")
            self.draw.ellipse([x-size, y-size, x+size, y+size], fill=self.brush_color, outline=None)

        self.last_x, self.last_y = x, y

    def reset(self, event):
        self.last_x, self.last_y = None, None

    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            self.image.save(file_path)

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("RGB", (800, 600), "white")
        self.draw = ImageDraw.Draw(self.image)

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernPaintApp(root)
    root.mainloop()