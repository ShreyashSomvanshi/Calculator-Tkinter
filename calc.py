from tkinter import *
root = Tk()

root.title("Calculator")
root.iconbitmap('C:/Users/Shreyash/Desktop/icon/favicon1.ico')

a = Entry(root, width=35, borderwidth=5)
a.grid(row=0, column=0, columnspan=3, padx=10,pady=10)

def clickbt(number):
    current = a.get()
    a.delete(0,END)
    a.insert(0, str(current)+str(number))
    
def clrbt():
    a.delete(0,END)
    
def addbt():
    firstNum = a.get()
    global fNum
    global math
    math = "add"
    fNum = int(firstNum)
    a.delete(0,END)
    
def eqlbt():
    secNum = a.get()
    a.delete(0,END)
    if math=='add':
        a.insert(0, fNum + int(secNum))
    elif math=='sub':
        a.insert(0, fNum - int(secNum))
    elif math=='mul':
        a.insert(0, fNum * int(secNum))
    elif math=='div':
        a.insert(0, fNum / int(secNum))

def subbt():
    firstNum = a.get()
    global fNum
    global math
    math = "sub"
    fNum = int(firstNum)
    a.delete(0,END)
    
def divbt():
    firstNum = a.get()
    global fNum
    global math
    math = "div"
    fNum = int(firstNum)
    a.delete(0,END)
    
def mulbt():
    firstNum = a.get()
    global fNum
    global math
    math = "mult"
    fNum = int(firstNum)
    a.delete(0,END)

b1 = Button(root, text="1", padx=40, pady=20, command=lambda: clickbt(1))
b2 = Button(root, text="2", padx=40, pady=20, command=lambda: clickbt(2))
b3 = Button(root, text="3", padx=40, pady=20, command=lambda: clickbt(3))
b4 = Button(root, text="4", padx=40, pady=20, command=lambda: clickbt(4))
b5 = Button(root, text="5", padx=40, pady=20, command=lambda: clickbt(5))
b6 = Button(root, text="6", padx=40, pady=20, command=lambda: clickbt(6))
b7 = Button(root, text="7", padx=40, pady=20, command=lambda: clickbt(7))
b8 = Button(root, text="8", padx=40, pady=20, command=lambda: clickbt(8))
b9 = Button(root, text="9", padx=40, pady=20, command=lambda: clickbt(9))
b0 = Button(root, text="0", padx=40, pady=20, command=lambda: clickbt(0))

# buttonQuit = Button(root, text="OFF",padx=120, pady=10, command=root.quit, bg='#dbdbdb')
# 
# buttonQuit.grid(3,columnspan=3)

bequal = Button(root,text = "=",padx=40, pady=20, command=eqlbt, bg="lightblue")
bclear = Button(root,text = "CLR",padx=120, pady=10, command=clrbt, bg="lightgreen")
bplus = Button(root,text = "+",padx=40, pady=20, command=addbt)
bsub = Button(root,text = "-",padx=40, pady=20, command=subbt)
bmul = Button(root,text = "X",padx=40, pady=20, command=mulbt)
bdiv = Button(root,text = "/",padx=40, pady=20, command=divbt)

bclear.grid(row=2,columnspan=3)

b1.grid(row= 4, column= 0)
b2.grid(row= 4, column= 1)
b3.grid(row= 4, column= 2)

b4.grid(row= 5, column= 0)
b5.grid(row= 5, column= 1)
b6.grid(row= 5, column= 2)

b7.grid(row= 6, column= 0)
b8.grid(row= 6, column= 1)
b9.grid(row= 6, column= 2)

b0.grid(row= 7, column= 1)
bplus.grid(row=7,column=0)
bequal.grid(row=7,column=2)

bsub.grid(row=8,column=1)
bmul.grid(row=8,column=0)
bdiv.grid(row=8,column=2)

root.mainloop()


