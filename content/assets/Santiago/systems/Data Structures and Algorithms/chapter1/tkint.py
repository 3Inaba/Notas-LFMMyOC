"""
Simple Drawing Program
-----------------------
A paint-style drawing app built with Tkinter.

Features:
- Freehand drawing with adjustable brush size
- Color picker
- Eraser tool
- Clear canvas
- Save drawing as PNG (requires Pillow)
- Undo last stroke

Run with: python drawing_app.py
"""

import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox

# Pillow is used to export the canvas to an image file.
# If it's not installed, saving will be disabled gracefully.
try:
    from PIL import Image, ImageDraw
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False


class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Drawing Program")
        self.root.geometry("900x650")
        self.root.resizable(True, True)

        # State
        self.pen_color = "black"
        self.prev_color = "black"  # remembers last non-eraser color
        self.brush_size = 4
        self.eraser_on = False
        self.last_x = None
        self.last_y = None
        self.canvas_bg = "white"

        # Keep track of strokes for undo: each stroke is a list of line-ids
        self.strokes = []
        self.current_stroke = []

        self._build_toolbar()
        self._build_canvas()
        self._bind_events()

    # ---------- UI construction ----------

    def _build_toolbar(self):
        toolbar = tk.Frame(self.root, bd=2, relief=tk.RAISED, bg="#e8e8e8")
        toolbar.pack(side=tk.TOP, fill=tk.X)

        # Color picker button
        self.color_btn = tk.Button(
            toolbar, text="Color", command=self.choose_color,
            bg=self.pen_color, fg="white", width=8
        )
        self.color_btn.pack(side=tk.LEFT, padx=5, pady=5)

        # Quick color swatches
        swatch_colors = ["black", "red", "orange", "yellow",
                          "green", "blue", "purple", "brown"]
        for c in swatch_colors:
            b = tk.Button(toolbar, bg=c, width=2, relief=tk.RIDGE,
                           command=lambda col=c: self.set_color(col))
            b.pack(side=tk.LEFT, padx=1, pady=5)

        # Brush size slider
        tk.Label(toolbar, text="Brush Size:", bg="#e8e8e8").pack(side=tk.LEFT, padx=(15, 2))
        self.size_slider = tk.Scale(
            toolbar, from_=1, to=50, orient=tk.HORIZONTAL,
            command=self.change_size, length=120
        )
        self.size_slider.set(self.brush_size)
        self.size_slider.pack(side=tk.LEFT, padx=5)

        # Eraser toggle
        self.eraser_btn = tk.Button(
            toolbar, text="Eraser", command=self.toggle_eraser, width=8
        )
        self.eraser_btn.pack(side=tk.LEFT, padx=10)

        # Undo
        tk.Button(toolbar, text="Undo", command=self.undo, width=8).pack(side=tk.LEFT, padx=5)

        # Clear
        tk.Button(toolbar, text="Clear", command=self.clear_canvas, width=8).pack(side=tk.LEFT, padx=5)

        # Save
        save_state = tk.NORMAL if PIL_AVAILABLE else tk.DISABLED
        self.save_btn = tk.Button(
            toolbar, text="Save PNG", command=self.save_canvas,
            width=10, state=save_state
        )
        self.save_btn.pack(side=tk.LEFT, padx=5)
        if not PIL_AVAILABLE:
            self.save_btn.config(text="Save (needs Pillow)")

        # Current size label
        self.status_label = tk.Label(toolbar, text=f"Size: {self.brush_size}px", bg="#e8e8e8")
        self.status_label.pack(side=tk.RIGHT, padx=10)

    def _build_canvas(self):
        self.canvas = tk.Canvas(self.root, bg=self.canvas_bg, cursor="cross")
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def _bind_events(self):
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)

    # ---------- Drawing logic ----------

    def start_draw(self, event):
        self.last_x, self.last_y = event.x, event.y
        self.current_stroke = []

    def draw(self, event):
        if self.last_x is None or self.last_y is None:
            self.last_x, self.last_y = event.x, event.y
            return

        color = self.canvas_bg if self.eraser_on else self.pen_color
        line_id = self.canvas.create_line(
            self.last_x, self.last_y, event.x, event.y,
            fill=color, width=self.brush_size,
            capstyle=tk.ROUND, smooth=True, splinesteps=36
        )
        self.current_stroke.append(line_id)
        self.last_x, self.last_y = event.x, event.y

    def stop_draw(self, event):
        if self.current_stroke:
            self.strokes.append(self.current_stroke)
        self.last_x, self.last_y = None, None
        self.current_stroke = []

    # ---------- Toolbar actions ----------

    def choose_color(self):
        color_code = colorchooser.askcolor(title="Choose pen color")
        if color_code and color_code[1]:
            self.set_color(color_code[1])

    def set_color(self, color):
        self.pen_color = color
        self.prev_color = color
        self.eraser_on = False
        self.color_btn.config(bg=color)
        self.eraser_btn.config(relief=tk.RAISED)

    def change_size(self, value):
        self.brush_size = int(value)
        self.status_label.config(text=f"Size: {self.brush_size}px")

    def toggle_eraser(self):
        self.eraser_on = not self.eraser_on
        if self.eraser_on:
            self.eraser_btn.config(relief=tk.SUNKEN)
        else:
            self.eraser_btn.config(relief=tk.RAISED)
            self.pen_color = self.prev_color
            self.color_btn.config(bg=self.pen_color)

    def undo(self):
        if not self.strokes:
            return
        last_stroke = self.strokes.pop()
        for line_id in last_stroke:
            self.canvas.delete(line_id)

    def clear_canvas(self):
        self.canvas.delete("all")
        self.strokes = []

    def save_canvas(self):
        if not PIL_AVAILABLE:
            messagebox.showwarning(
                "Pillow required",
                "Install Pillow to enable saving:\n\npip install Pillow"
            )
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG image", "*.png"), ("All files", "*.*")]
        )
        if not file_path:
            return

        # Recreate the canvas drawing onto a Pillow image by reading
        # canvas item coordinates (works without needing a screenshot).
        self.canvas.update()
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        image = Image.new("RGB", (width, height), self.canvas_bg)
        draw = ImageDraw.Draw(image)

        for item in self.canvas.find_all():
            coords = self.canvas.coords(item)
            fill = self.canvas.itemcget(item, "fill") or self.canvas_bg
            width_px = self.canvas.itemcget(item, "width")
            try:
                line_width = int(float(width_px))
            except ValueError:
                line_width = 1
            if len(coords) >= 4:
                draw.line(coords, fill=fill, width=line_width, joint="curve")

        try:
            image.save(file_path)
            messagebox.showinfo("Saved", f"Drawing saved to:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file:\n{e}")


def main():
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()