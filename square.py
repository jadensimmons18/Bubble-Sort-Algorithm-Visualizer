import tkinter as tk


class Square():

    def __init__(self, canvas, x1, y1, x2, y2, val, tag):

        self.tag = f"box{tag}"

        # Create the square
        self.id = canvas.create_rectangle(x1, y1, x2, y2, 
                                fill="white", outline="black", width=2, tags=self.tag)

        
        # Calculate the center of the square
        self.center_x = (x1 + x2) / 2
        self.center_y = (y1 + y2) / 2

        # Draw the value in the center
        self.text_id = canvas.create_text(self.center_x, self.center_y, text=str(val), font=("Arial", 14, "bold"), fill="black", tags=self.tag)

        # Store val
        self.val = val
        self.x1, self.x2 = x1,x2
        

        
