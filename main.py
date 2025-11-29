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
        self.start_button.place(x = 400, y = 250, anchor="center")

        # Squares array
        self.squares = []

        # Variables
        self.sorted = False
        self.swapped = False

    def start_pressed(self):
        self.start_button.place_forget()
        self.draw_squares()
        self.BubbleSort() # Start first pass

    def draw_squares(self):
        # Generate the squares with random values
        x1 = 10  # Initiate x1 at position 20
        y1 = 220
        x2 = 70  # Initiate x2 at position 80
        y2 = 280
        for i in range(10):
            self.squares.append(Square(self.canvas, x1, y1, x2,
                           y2, random.randint(1, 99), i))
            print(self.squares[i].val, end=" ")
            x1 += 80
            x2 += 80
        print() # Newline

    # Resets all variables and calls a single bubble sort pass
    def BubbleSort(self):
        self.curIndex = 0
        self.sorted = False
        self.single_pass()


    def single_pass(self):

        for i in self.squares:
            print(i.val, end=" ")
        print() # NewLine
    
        if not self.sorted: # Only run if the array is not already sorted

            if (self.curIndex == 0): # Only run at the start of the pass
                self.swapped = False # assume its sorted until proved otherwise

            if self.curIndex >= len(self.squares) - 1: # If you reach the end of the array
                if self.swapped == False: # Array is sorted
                    print("Bubble Sort Complete")
                    self.sorted = True
                    return
                else: # Array is not sorted so call another pass
                    self.curIndex = 0
                    self.after(100, self.single_pass)
                    return

            if self.squares[self.curIndex].val > self.squares[self.curIndex + 1].val: # if current square is bigger than next square
                self.swapped = True # Found something out of order
                tmp = self.squares[self.curIndex]
                self.squares[self.curIndex] = self.squares[self.curIndex + 1]
                self.squares[self.curIndex + 1] = tmp
                self.curIndex += 1
                self.animate_swap(self.squares[self.curIndex], self.squares[self.curIndex + 1]) #Call the animation on both squares
                self.after(100, self.single_pass)
                return

            else: # If the current index doesnt need to be swapped then call another pass
                self.curIndex += 1
                self.after(100, self.single_pass)
                return

    def animate_swap(self, square1, square2):

        distance = square2.center_x - square1.center_x # = 80
        frames = 10
        movement_per_frame = distance / frames

        self.animation(square1, square2, movement_per_frame, distance)

    def animation(self, square1, square2, movement, total_distance):

        coords = self.canvas.coords(self.square1.id)
        x1, y1, x2, y2 = coords
        square1_current_center = (x1 + x2) / 2

        if square1_current_center >= square2.center_x:
            return

        coords = self.canvas.coords(self.square2.id)
        x1, y1, x2, y2 = coords
        square2_current_center = (x1 + x2) / 2

        if square2_current_center <= square1.center_x:
            return

        self.canvas.move(square1.tag, movement, 0)
        self.canvas.move(square2.tag, -movement, 0)
        self.canvas.after(100, self.animate, dx)

if __name__ == "__main__":
    app = Main()
    app.mainloop()
