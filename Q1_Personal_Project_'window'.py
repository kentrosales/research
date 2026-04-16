from tkinter import *
import tkinter as tk
root = Tk()
root.title("Staff Details")

#WRITING TEXT
Label(root, text = "Welcome", fg = "red", font ="arial 24 bold").pack(padx=10, pady= 5)
Label(root, text = "You have been chosen.", fg = "blue", font ="arial 24 bold").pack(padx=10, pady= 5)

def show_input():
    user_input = text_box.get(index1="1.0", 
                              index2 = "end")
    output_label.config(text= user_input)
    

text_box = tk.Text(root, height = 3, width = 30)
text_box.pack(pady=10)

button = tk.Button(root, text = "Submit", command = show_input)
button.pack()


output_label = tk.Label(root, text= "", fg = "orange", font = "Arial 14")
output_label.pack(pady=10)



root.mainloop()
