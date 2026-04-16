# Author: Kent Rovin Rosales
# Project: "I Love You" Project

from tkinter import *
import tkinter as tk
root = Tk()


cat_image = tk.PhotoImage(file=r"C:\Users\kentr\Pictures\cat_ily.png")

Label(root, text = "Click the buttom for a surprise <3", font ="arial 24 bold").pack(padx = 1, pady =1)
Label(root, text = "Do not click", font = "arial 14 bold").pack(padx = 1, pady = 1)

def cat():
    output_label.config(image=cat_image)
    output_label.image = cat_image
def text():
    text.config(text= "Hello", fg= "red", font= "arial 40 bold").pack(padx = 10, pady = 5)
    
button = tk.Button(root, text = "Submit", command = cat)
button.pack()
button = tk.Button(root, text= "Hello",command= text)
button.pack()

output_label = tk.Label(root)
output_label.pack(pady=10)
text = tk.Label(root)
text.pack(pady = 10)


root.mainloop()

# Few takeaways from this project:
# a.) Importance of formatting
# b.) Importance of the K.I.S.S principle - keeping the code short and simple made the code easy to navigate and edit
