from tkinter import *
from  functools import partial

root=Tk()
root.title('Calculator')
root.configure(background='grey')
bclr='black'
fclr='white'

rectxt=''


def click(txt):
    global tb
    if(txt=='C'):
        tb.delete(0,END)
    elif(txt=='X'):
        text=tb.get()[:-1]
        tb.delete(0,END)
        tb.insert(0,text)
    elif(txt=='='):
        try:
            result=eval(tb.get())
            tb.delete(0,END)
            tb.insert(0,result)
        except:
            tb.delete(0,END)
            tb.insert(0,'ERROR')

    else:
        tb.insert(END,txt)
        
btn=[
    'X','(',')','/',
    '7','8','9','*',
    '4','5','6','-',
    '1','2','3','+',
    'C','0','.','='
]


def change():
    global bclr
    global fclr
    global rectxt
    bclr,fclr=fclr,bclr
    rectxt=tb.get()
    create()

def create():
    global tb
    tb=Entry(root,width=10,font=("Arial", 30),bg=bclr,fg=fclr)
    tb.grid(row=0,column=0,columnspan=4,sticky='we',padx=5,pady=2)
    tb.insert(0,rectxt)

    r,c = 1,0

    for binp in btn:
        if(binp=='X' or binp=='C'):
            clr='red'
        elif(binp=='='):
            clr='green'
        else:
            clr=bclr

        clk=partial(click,binp)
        b=Button(root,text=binp, font=("Arial", 20), command=clk,height=2,width=4,bg=clr,fg=fclr)
        b.grid(row=r,column=c)
        c+=1
        if(c==4):
            c=0
            r+=1

    Button(root,text='Theme',command=change, bg=bclr,fg=fclr).grid(row=6,column=0,columnspan=4,sticky='we')

create()

root.mainloop()
    
