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
        print()

    # Resets all variables and calls a single bubble sort pass
    def BubbleSort(self):
        self.curIndex = 0
        self.single_pass()


    def single_pass(self):

        for i in self.squares:
            print(i.val, end=" ")
        print()

        if not self.sorted: # Only run if the array is not already sorted

            if (self.curIndex == 0): # Only run at the start of the pass
                self.sorted = True # assume its sorted until proved otherwise

            if self.curIndex >= len(self.squares) - 1: # If you reach the end of the array
                if self.sorted == True: # Array is sorted
                    print("Bubble Sort Complete")
                    return
                else: # Array is not sorted so call another pass
                    self.curIndex = 0
                    self.after(100, self.single_pass)
                    return

            if self.squares[self.curIndex].val > self.squares[self.curIndex + 1].val:
                self.sorted = False # Found something out of order
                tmp = self.squares[self.curIndex]
                self.squares[self.curIndex] = self.squares[self.curIndex + 1]
                self.squares[self.curIndex + 1] = tmp
                self.after(100, self.single_pass)
                return

            else: # If the current index doesnt need to be swapped then call another pass
                self.curIndex += 1
                self.after(100, self.single_pass)
                return

if __name__ == "__main__":
    app = Main()
    app.mainloop()
