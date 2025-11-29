import tkinter as tk
import random
from square import Square


class Main(tk.Tk):

    def __init__(self):
        super().__init__()

        # Config the window
        self.geometry("800x500")
        self.title("Algorithm Visualizer")
        self.canvas = tk.Canvas(self, bg="#2c2b3c")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Bubble Sort Button
        self.start_button = tk.Button(
            master=self,
            text="Press To Begin Bubble Sort",
            command=self.start_pressed
        )
        self.start_button.place(x=400, y=250, anchor="center")

        # Squares array
        self.squares = []

        # Variables
        self.sorted = False
        self.swapped = False

    def start_pressed(self):
        self.start_button.place_forget()
        self.draw_squares()
        self.BubbleSort()  # Start first pass

    def draw_squares(self):
        # Generate the squares with random values
        x1 = 10
        y1 = 220
        x2 = 70
        y2 = 280
        for i in range(10):
            # assume Square(canvas, x1,y1,x2,y2, value, index) creates and stores .center_x, .id or .tag
            s = Square(self.canvas, x1, y1, x2, y2, random.randint(1, 99), i)
            self.squares.append(s)
            print(s.val, end=" ")
            x1 += 80
            x2 += 80
        print()

    # Resets all variables and calls a single bubble sort pass
    def BubbleSort(self):
        self.curIndex = 0
        self.sorted = False
        self.single_pass()

    def single_pass(self):
        for i in self.squares:
            print(i.val, end=" ")
        print()

        if not self.sorted:
            if (self.curIndex == 0):  # Only run at the start of the pass
                self.swapped = False

            if self.curIndex >= len(self.squares) - 1:
                if self.swapped == False:
                    print("Bubble Sort Complete")
                    self.sorted = True
                    return
                else:
                    # Start another pass
                    self.curIndex = 0
                    self.after(100, self.single_pass)
                    return

            a = self.squares[self.curIndex]
            b = self.squares[self.curIndex + 1]

            if a.val > b.val:
                self.swapped = True

                # Capture the objects to animate BEFORE changing the list
                obj1, obj2 = a, b

                # Swap in the list (so future comparisons see the swapped order)
                self.squares[self.curIndex] = obj2
                self.squares[self.curIndex + 1] = obj1

                # increment index for algorithm progress (we already handled swap)
                self.curIndex += 1

                # Animate those two specific objects (the original objects we captured)
                self.animate_swap(obj1, obj2)

                # After starting animation, schedule the next single_pass after
                # a bit of a delay to give animation time to run. We will also
                # call single_pass from animation's completion to be safe.
                # But to keep your original flow, we schedule single_pass after
                # animation duration (frames * frame_delay).
                return

            else:
                self.curIndex += 1
                self.after(100, self.single_pass)
                return

    def animate_swap(self, square1, square2):
        """
        Animate square1 moving right and square2 moving left until they exchange places.
        We assume each Square object has a numeric .center_x property representing its x-center.
        Also each Square should have either .tag (string) or .id (canvas item id).
        """

        # Determine which canvas identifier to move (tag preferred)
        def _canvas_key(sq):
            return getattr(sq, "tag", getattr(sq, "id", None))

        key1 = _canvas_key(square1)
        key2 = _canvas_key(square2)
        if key1 is None or key2 is None:
            raise RuntimeError("Square objects must have .tag or .id attributes for canvas movement.")

        # compute the horizontal distance to move (should be positive)
        distance = square2.center_x - square1.center_x
        if distance == 0:
            # nothing to animate
            # still update centers to be robust
            square1.center_x, square2.center_x = square2.center_x, square1.center_x
            # continue sorting
            self.after(50, self.single_pass)
            return

        frames = 12               # number of frames in the animation
        frame_delay = 25          # ms between frames
        dx_per_frame = distance / frames

        # inner recursive animator using frames_left counter
        def _step(frames_left):
            if frames_left <= 0:
                # Finalize exact positions to avoid rounding error
                # Move any residual remaining distance (snap to final)
                # compute current centers from canvas coords to be precise
                coords1 = self.canvas.coords(key1)
                coords2 = self.canvas.coords(key2)
                # coords returns [x1, y1, x2, y2] for rectangle/oval items
                if len(coords1) >= 4 and len(coords2) >= 4:
                    c1 = (coords1[0] + coords1[2]) / 2
                    c2 = (coords2[0] + coords2[2]) / 2
                    # swap center_x values in the objects (they exchanged)
                    square1.center_x, square2.center_x = c2, c1
                else:
                    # fallback: swap the old stored center_x values
                    square1.center_x, square2.center_x = square2.center_x, square1.center_x

                # Once animation done, continue the sorting process
                # small delay so GUI updates nicely
                self.after(50, self.single_pass)
                return

            # Move each item for this frame
            self.canvas.move(key1, dx_per_frame, 0)
            self.canvas.move(key2, -dx_per_frame, 0)

            # schedule next frame
            self.after(frame_delay, lambda: _step(frames_left - 1))

        # start the animation
        _step(frames)

if __name__ == "__main__":
    app = Main()
    app.mainloop()
