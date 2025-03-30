from tkinter import *
import os

def execute_cmd():
    txt.delete("1.0", END)
    command = ent1.get()
    output = os.popen(command).read()
    txt.insert("1.0",output)


window = Tk()
window.title('Eli Hamelech')
window.geometry("645x500")
window.iconbitmap('barca.ico')
window.resizable(True, True)

lbl1 = Label(window, text="Enter Command:")
lbl1.place(x=5, y=5)

ent1 = Entry(window, width=30)
ent1.place(x=100,y=5)

btn1 = Button(window, text="Execute", command=execute_cmd)
btn1.place(x=300,y=0)

txt = Text(window)
txt.place(x=0, y=100)

window.mainloop()
