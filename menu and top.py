from tkinter import *

def window_exit():
    window.destroy()

def new_window():
    top = Toplevel()
    top.geometry("300x100")
    top.title("New")
    top.iconbitmap('barca.ico')
    top.resizable(False,False)

    btn1= Button(top, text="new button")
    btn1.place(x=0,y=0)
window = Tk()
window.title('Eli Hamelech')
window.geometry("500x500")
window.iconbitmap('barca.ico')
window.resizable(False, False)

menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='New', command=new_window)
new_item.add_command(label='Save')
new_item.add_separator()
new_item.add_command(label='Exit', command=window_exit)

menu.add_cascade(label='File', menu=new_item)

window.config(menu=menu)
window.mainloop()
