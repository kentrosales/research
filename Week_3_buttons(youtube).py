#GUI window
from tkinter import *
root = Tk()
root.geometry('600x600')
root.title('Square Area')

count = 0
def click():
    global count
    count+=1
    label.config(text=count)
    label2.pack

button = Button(root, text='Click me!!!')

button.config(command=click)#performs call back of function
button.config(font=('Ink Free',50, 'bold'))
button.config(bg='#ff6200')
button.config(fg='#fffb1f')
button.config(activebackground='#FF0000')
button.config(activeforeground='#FF0000')
image = PhotoImage(file='cursor.png')
button.config(image=image)
button.config(compound='bottom')
# button.config(state=DISABLED) #disables button
label = Label(root, text=count)
label.config(font=('Monospace',50))
label.pack()
button.pack()
label2= Label(root, image=image)
label2.pack
root.mainloop()
