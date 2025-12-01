# Bubble-Sort-Algorithm-Visualizer

A dynamic Graphical User Interface (GUI) application built with **Python** and **Tkinter** that visualizes the execution of sorting algorithms. The current implementation features a fully animated **Bubble Sort**, demonstrating element comparison and swapping in real-time.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Library](https://img.shields.io/badge/Library-Tkinter-orange.svg)
![Status](https://img.shields.io/badge/Status-Active-green.svg)

## 📋 Table of Contents
- [Features](#-features)
- [Demo](#-demo)
- [Getting Started](#-getting-started)
- [Technical Implementation](#-technical-implementation)
- [Project Structure](#-project-structure)

## ✨ Features

* **Real-time Visualization:** Watch the algorithm process data step-by-step.
* **Smooth Animations:** Uses custom logic to animate the swapping of elements, making the sorting process easy to follow.
* **Randomized Data Generation:** Generates a new set of random integers (1-99) for every session.
* **Object-Oriented Design:** modular code structure separating the UI logic from the data objects.

### Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/yourusername/sorting-visualizer.git](https://github.com/yourusername/sorting-visualizer.git)
    ```
2.  Navigate to the project directory:
    ```bash
    cd sorting-visualizer
    ```
3.  Run the application:
    ```bash
    python main.py
    ```

## 🛠 Technical Implementation

### Asynchronous Animation Loop
Unlike standard console visualizations that might use `time.sleep()`, this application maintains a responsive GUI by utilizing Tkinter's `.after()` method. This allows the recursive animation loop to run without freezing the main application thread.

The `animate_swap` function calculates the pixel distance between two objects and incrementally moves them over a set number of frames (12 frames at 25ms intervals).

### The Bubble Sort Logic
The sorting algorithm is implemented with a "pause-and-resume" architecture. When a swap is detected:
1.  The sorting loop pauses.
2.  The animation triggers.
3.  Upon animation completion, the sorting function calls itself (`single_pass`) to resume exactly where it left off.

```python
# Snippet from main.py
if a.val > b.val:
    # Trigger Animation
    self.animate_swap(obj1, obj2)
    return # Pause execution while animation plays
