
#  Futoshiki Puzzle Game

This is a logic-based number puzzle game built with Python using Tkinter. Your task is to fill numbers into a grid while following specific rules.

---

##  Game Description

* The game is played on a 7×7 grid.
* Some cells are disabled or pre-filled.
* Inequality signs (>, ^, v) show how certain cells relate to each other.
* The goal is to fill in the white cells with numbers 1–4 such that:

  * Each number appears only once per row and column.
  * All inequality signs are respected.

📄 Full game rules and an image of the puzzle layout are provided in the attached PDF file: rules\_and\_layout.pdf

---

##  Features

* Graphical user interface (GUI) built using Tkinter.
* Real-time input validation.
* Visual feedback on incorrect entries.
* Congratulatory message upon successfully solving the puzzle.

---

## Requirements

Make sure Python 3 is installed. Then install the following libraries:

```bash
pip install pillow pygame
```

Tkinter comes built-in with most Python installations.

---
## How to Run

1. Ensure all project files (including the PDF) are in one folder.
2. Open a terminal in that folder.
3. Run the game with:

```bash
python main.py
```

---
## How to Play

1. Click the START button.
2. Fill in the white cells with numbers from 1 to 4.
3. Click SUBMIT to check your answer.
4. If correct, a message will appear. If not, incorrect cells will turn red.
5. Click EXIT to close the game.

