from tkinter import *

def update(data):
    global math_expr
    math_expr+=str(data)
    entry.delete(0,END)
    entry.insert(0, math_expr)

def clear():
    global math_expr
    math_expr = ""
    entry.delete(0, END)

def summary():
    global math_expr
    result=eval(math_expr)
    entry.delete(0, END)
    entry.insert(0, result)

window=Tk()
window.title('Calculator')
window.geometry("250x130")
window.iconbitmap('barca.ico')
window.resizable(False, False)

math_expr = ""

entry=Entry(window, width=39)
entry.grid(row=0, column= 0, columnspan=4)

btn1=Button(window, text="1",height=1,width=7,command=lambda:update(1))
btn1.grid(row=1,column=0)
btn2=Button(window, text="2",height=1,width=7,command=lambda:update(2))
btn2.grid(row=1,column=1)
btn3=Button(window, text="3",height=1,width=7,command=lambda:update(3))
btn3.grid(row=1,column=2)
btn4=Button(window, text="4",height=1,width=7,command=lambda:update(4))
btn4.grid(row=2,column=0)
btn5=Button(window, text="5",height=1,width=7,command=lambda:update(5))
btn5.grid(row=2,column=1)
btn6=Button(window, text="6",height=1,width=7,command=lambda:update(6))
btn6.grid(row=2,column=2)
btn7=Button(window, text="7",height=1,width=7,command=lambda:update(7))
btn7.grid(row=3,column=0)
btn8=Button(window, text="8",height=1,width=7,command=lambda:update(8))
btn8.grid(row=3,column=1)
btn9=Button(window, text="9",height=1,width=7,command=lambda:update(9))
btn9.grid(row=3,column=2)
btn0=Button(window, text="0",height=1,width=7,command=lambda:update(0))
btn0.grid(row=4,column=1)
#mathematical operations
btn_plus=Button(window, text="+",height=1,width=7,command=lambda:update("+"))
btn_plus.grid(row=1,column=3)
btn_minus=Button(window, text="-",height=1,width=7,command=lambda:update("-"))
btn_minus.grid(row=2,column=3)
btn_mult=Button(window, text="*",height=1,width=7,command=lambda:update("*"))
btn_mult.grid(row=3,column=3)
btn_div=Button(window, text="/",height=1,width=7,command=lambda:update("/"))
btn_div.grid(row=4,column=3)
btn_equal=Button(window, text="=",height=1,width=7,command=summary)
btn_equal.grid(row=4,column=2)
btn_clear=Button(window, text="Clear",height=1,width=7,command=clear)
btn_clear.grid(row=4,column=0)
window.mainloop()
