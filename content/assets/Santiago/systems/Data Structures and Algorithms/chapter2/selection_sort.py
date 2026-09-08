"""
Selection Sort Visualizer
--------------------------
A Tkinter GUI that animates the selection sort algorithm step by step.

Controls:
- New Array: generate a new random array of bars
- Start: begin sorting the current array
- Speed slider: controls animation delay

Color legend:
- Blue    : unsorted / default
- Orange  : current position being filled (i)
- Red     : element currently being compared (j)
- Yellow  : current minimum found so far
- Green   : sorted portion of the array
"""

import tkinter as tk
from tkinter import ttk
import random

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 450
ARRAY_SIZE = 30
MAX_VALUE = 400
PADDING = 10

COLOR_DEFAULT = "#4C6EF5"   # blue
COLOR_CURRENT = "#F76707"   # orange (i)
COLOR_COMPARE = "#E03131"   # red (j)
COLOR_MIN = "#FCC419"       # yellow (current min)
COLOR_SORTED = "#2F9E44"    # green


class SelectionSortVisualizer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Selection Sort Visualizer")
        self.resizable(False, False)

        self.array = []
        self.bar_ids = []
        self.text_ids = []
        self.sorting = False
        self.delay_ms = tk.IntVar(value=150)

        self._build_ui()
        self.generate_array()

    # ---------- UI setup ----------
    def _build_ui(self):
        control_frame = ttk.Frame(self, padding=10)
        control_frame.pack(side=tk.TOP, fill=tk.X)

        self.new_array_btn = ttk.Button(
            control_frame, text="New Array", command=self.generate_array
        )
        self.new_array_btn.pack(side=tk.LEFT, padx=5)

        self.start_btn = ttk.Button(
            control_frame, text="Start", command=self.start_sort
        )
        self.start_btn.pack(side=tk.LEFT, padx=5)

        ttk.Label(control_frame, text="Speed:").pack(side=tk.LEFT, padx=(20, 5))
        speed_scale = ttk.Scale(
            control_frame,
            from_=400,
            to=5,
            orient=tk.HORIZONTAL,
            variable=self.delay_ms,
            length=180,
        )
        speed_scale.pack(side=tk.LEFT)

        self.status_var = tk.StringVar(value="Ready")
        status_label = ttk.Label(control_frame, textvariable=self.status_var)
        status_label.pack(side=tk.RIGHT, padx=5)

        self.canvas = tk.Canvas(
            self, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white"
        )
        self.canvas.pack(side=tk.TOP, padx=10, pady=10)

    # ---------- Array / drawing ----------
    def generate_array(self):
        if self.sorting:
            return
        self.array = [random.randint(10, MAX_VALUE) for _ in range(ARRAY_SIZE)]
        self.draw_array()
        self.status_var.set("Ready")

    def draw_array(self, highlight=None):
        """Redraw all bars. `highlight` is a dict {index: color}."""
        highlight = highlight or {}
        self.canvas.delete("all")
        self.bar_ids = []
        self.text_ids = []

        n = len(self.array)
        bar_width = (CANVAS_WIDTH - 2 * PADDING) / n

        for idx, value in enumerate(self.array):
            x0 = PADDING + idx * bar_width
            x1 = x0 + bar_width - 2
            y1 = CANVAS_HEIGHT - PADDING
            y0 = y1 - (value / MAX_VALUE) * (CANVAS_HEIGHT - 2 * PADDING)

            color = highlight.get(idx, COLOR_DEFAULT)
            bar_id = self.canvas.create_rectangle(
                x0, y0, x1, y1, fill=color, outline=""
            )
            self.bar_ids.append(bar_id)

        self.canvas.update_idletasks()

    # ---------- Sorting logic ----------
    def start_sort(self):
        if self.sorting:
            return
        self.sorting = True
        self.start_btn.config(state=tk.DISABLED)
        self.new_array_btn.config(state=tk.DISABLED)
        self.status_var.set("Sorting...")
        self._selection_sort_generator = self._selection_sort()
        self._run_step()

    def _run_step(self):
        try:
            next(self._selection_sort_generator)
            self.after(self.delay_ms.get(), self._run_step)
        except StopIteration:
            self.sorting = False
            self.start_btn.config(state=tk.NORMAL)
            self.new_array_btn.config(state=tk.NORMAL)
            self.status_var.set("Done!")
            self.draw_array({i: COLOR_SORTED for i in range(len(self.array))})

    def _selection_sort(self):
        """Generator that yields after every visual-worthy step."""
        arr = self.array
        n = len(arr)
        sorted_indices = set()

        for i in range(n):
            min_idx = i
            highlight = {k: COLOR_SORTED for k in sorted_indices}
            highlight[i] = COLOR_CURRENT
            highlight[min_idx] = COLOR_MIN
            self.status_var.set(f"Finding minimum for position {i}")
            self.draw_array(highlight)
            yield

            for j in range(i + 1, n):
                highlight = {k: COLOR_SORTED for k in sorted_indices}
                highlight[i] = COLOR_CURRENT
                highlight[j] = COLOR_COMPARE
                highlight[min_idx] = COLOR_MIN
                self.draw_array(highlight)
                yield

                if arr[j] < arr[min_idx]:
                    min_idx = j
                    highlight = {k: COLOR_SORTED for k in sorted_indices}
                    highlight[i] = COLOR_CURRENT
                    highlight[min_idx] = COLOR_MIN
                    self.status_var.set(f"New minimum found at index {min_idx}")
                    self.draw_array(highlight)
                    yield

            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            sorted_indices.add(i)

            highlight = {k: COLOR_SORTED for k in sorted_indices}
            self.draw_array(highlight)
            yield


if __name__ == "__main__":
    app = SelectionSortVisualizer()
    app.mainloop()