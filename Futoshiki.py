import tkinter as tk
from PIL import ImageTk, Image
import pygame
pygame.mixer.init()


def create_puzzle():
    
    # Create the window
    pygame.mixer.music.load("el_interface_button_22_hpx.mp3")
    pygame.mixer.music.play(loops = 0)

    window1 =tk.Toplevel() 
    window1.title("Futoshiki Puzzle")
    window1.geometry("2000x2000")
    
    
    # Define the disabled cells
    disabled_cells = [(0,1),(0, 3), (0, 5), (1, 0),(1, 1),(1, 2), (1, 3), (1, 4),(1, 5),(1, 6), (1, 7), (3, 0),(3, 1),(3, 2), (3, 3), (3, 4),(3, 5),(3, 6), (3, 7),(5, 0),(5, 1),(5, 2), (5, 3), (5, 4),(5, 5),(5, 6), (5, 7),(2, 1),(2, 3),(2, 5), (4, 1), (4, 3),(4, 5),(6, 1), (6, 3), (6, 5)]

    # Add the inequality constraints
    constraints = [((0, 2),(2,1),  "^"), ((1, 6), (1, 5), "v"), ((4, 0), (4, 1), ">"), ((6, 5), (5, 6), "^"),((3, 3), (3, 4), "^")]

    # Input values for the puzzle
    input_values = { (4, 6): 3}
    
    
    # Create the grid cells
    for i in range(7):
        for j in range(7):
            if (i, j) in disabled_cells:
                entry = tk.Entry(window1, width=10, state='disabled',font=('Arial', 20))
            else:
                entry = tk.Entry(window1, width=10,font=('Arial', 20))
            entry.grid(row=i, column=j, padx=30, pady=10,ipady=20)
    
     
    # Add the inequality constraints
    for constraint in constraints:
        row1, col1 = constraint[0]
        row2, col2 = constraint[1]
        symbol = constraint[2]
        label = tk.Label(window1, text=symbol,font=("TkDefaultFont", 30))
        label.grid(row=(row1 + row2) // 2, column=(col1 + col2) // 2 + 1)

    # Set the input values in the puzzle
    for (row, col), value in input_values.items():
        entry = window1.grid_slaves(row=row, column=col)[0]
        entry.insert(0, str(value))
        entry.config(state="disabled")
    

   
   
    def solve_puzzle():
        pygame.mixer.music.load("el_interface_button_22_hpx.mp3")
        pygame.mixer.music.play(loops = 0)
       

    # Check that all entries contain a value between 1 and 4
        for i in range(7):
            for j in range(7):
                if (i, j) in disabled_cells:
                    continue
                entry = window1.grid_slaves(row=i, column=j)[0]
                value = entry.get()
                if value:
                    if not value.isdigit() or int(value) not in range(1, 5):
                        entry.config(bg='red')
                        return False
                    else:
                        entry.config(bg='white')

      
                        
        for constraint in constraints:
            r1, c1 = constraint[0]
            r2, c2 = constraint[1]
            row1, col1 = r1, c1
            row2, col2 = r2, c2+1
            if (row1, col1) in disabled_cells or (row2, col2) in disabled_cells:
                continue
            entry1 = window1.grid_slaves(row=row1, column=col1)[0]
            value1 = entry1.get()
            entry2 = window1.grid_slaves(row=row2, column=col2)[0]
            value2 = entry2.get()
            if constraint[2] == "^":
                if value1 and value2:
                    if int(value1) >= int(value2):
                        entry1.config(bg='red')
                        entry2.config(bg='red')
                        
                        return False
                    else:
                        entry1.config(bg ='white')
                        entry2.config(bg ='white')
        for constraint in constraints:
            r1, c1 = constraint[0]
            r2, c2 = constraint[1]
            row1, col1 = r1, c1
            row2, col2 = r2, c2+1
            if (row1, col1) in disabled_cells or (row2, col2) in disabled_cells:
                continue
            entry1 = window1.grid_slaves(row=row1, column=col1)[0]
            value1 = entry1.get()
            entry2 = window1.grid_slaves(row=row2, column=col2)[0]
            value2 = entry2.get()
            if constraint[2] == ">":
                if value1 and value2:
                    if int(value1) <= int(value2):
                        entry1.config(bg='red')
                        entry2.config(bg='red')
                       
                        return False
                    else:
                        entry1.config(bg ='white')
                        entry2.config(bg ='white')
        for constraint in constraints:
            r1, c1 = constraint[0]
            r2, c2 = constraint[1]
            row1, col1 = r1, c1+1
            row2, col2 = r2-1, c2
            if (row1, col1) in disabled_cells or (row2, col2) in disabled_cells:
                continue
            entry1 = window1.grid_slaves(row=row1, column=col1)[0]
            value1 = entry1.get()
            entry2 = window1.grid_slaves(row=row2, column=col2)[0]
            value2 = entry2.get()
            if constraint[2] == "^":
                if value1 and value2:
                    if int(value1) <= int(value2):
                        entry1.config(bg='red')
                        entry2.config(bg='red')
                        
                        return False
                    else:
                        entry1.config(bg ='white')
                        entry2.config(bg ='white')
   
    # Check that each row and column contains unique values
        for i in range(7):
            row_values = set()
            col_values = set()
            for j in range(7):
                if (i, j) in disabled_cells:
                    continue
            # Check row
                row_entry = window1.grid_slaves(row=i, column=j)[0]
                row_value = row_entry.get()
                if row_value:
                    if row_value in row_values:
                        row_entry.config(bg='red')
                        
                        return False
                    else:
                        entry.config(bg ='white')
                    row_values.add(row_value)
            # Check column
                col_entry = window1.grid_slaves(row=j, column=i)[0]
                col_value = col_entry.get()
                if col_value:
                    if col_value in col_values:
                        col_entry.config(bg='red')
                       
                        return False
                    else:
                        entry.config(bg ='white')
                    col_values.add(col_value)
        grid_values = [[0 for j in range(7)] for i in range(7)]
        for i in range(7):
            for j in range(7):
                if (i, j) in disabled_cells:
                    continue
                entry = window1.grid_slaves(row=i, column=j)[0]
                value = entry.get()
                if not value:
                    return False  # Exit if any cell is empty
                grid_values[i][j] = int(value)
    
        return True
   

    # Rest of the code...

    shower_label = None

    def on_submit():
        global shower_label
        if solve_puzzle():
            window2 = tk.Toplevel()
            window2.geometry("2000x2000")
            window2.title("")
            shower_label = tk.Label(window2, text="Congratulations! You solved the puzzle!", font=('Arial', 40))
            shower_label.place(x=400,y = 300)
            shower_label.configure(bg="lightgreen")
            
        else:
            if shower_label is not None:
                 shower_label.destroy()
        return None
 

    submit_button = tk.Button(window1, text="SUBMIT",bg= "pink" ,height=2, width=20,command=on_submit)
    submit_button.grid(row=8, column=3)
    exit_button = tk.Button(window1, text="EXIT",fg="black",bg = "lightblue", height=2, width=20, command=lambda:(window1.destroy(),button_click2()))
    exit_button.place(x=850, y=670)
    
    def button_click1():
        pygame.mixer.music.load("el_interface_button_22_hpx.mp3")
        pygame.mixer.music.play(loops = 0)
        
        
  
    
def button_click():
    create_puzzle()
    

window = tk.Tk()
window.geometry("2000x2000")
window.title("")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
image1 = Image.open("C:\\Users\\Bachu Lakshmi Sravani\\OneDrive\\Pictures\\puzzle.png")

test = ImageTk.PhotoImage(image1)
label1 = tk.Label(image=test)
label1.image = test
x_coordinate = -100
y_coordinate = -200
# Position image
label1.place(x=x_coordinate, y=y_coordinate)
#position button
button = tk.Button(window, text="START",fg="black", height=3, width=30,  command=button_click,font=('Arial', 10))
button.place(x=1250, y=600)
exit_button = tk.Button(window, text="EXIT",fg="black", height=2, width=30, command=lambda:(window.destroy(),button_click2()))
exit_button.place(x=1250, y=700)
def button_click2():
    pygame.mixer.music.load("el_interface_button_22_hpx.mp3")
    pygame.mixer.music.play(loops = 0)
window.mainloop()
