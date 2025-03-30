from tkintro import *
from tkintro import messagebox

def btn1_func():
    result = messagebox.askyesno("Question", "which bear is best?")
    if result:
        text = ent1.get()
        txt.insert(END, text)


window = Tk()
window.title('Eli Hamelech')
window.geometry("400x300")
window.iconbitmap('barca.ico')
window.resizable(False, False)
lbl1 = Label(window, text="Hey!")
lbl1.place(x=5, y=50)
btn1 = Button(window, text= "Yo!", command=btn1_func)
btn1.place(x=5, y=5)
ent1 = Entry(window, width="20")
ent1.place(x=5, y=100)
Lb1 = Listbox(window, selectmode=MULTIPLE)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")

Lb1.pack()
txt = Text(window)
txt.place(x=5, y=150)
window.mainloop()
