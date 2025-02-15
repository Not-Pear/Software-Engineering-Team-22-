from tkinter import * 
s = Tk()

#sets up ---------------------------------------------------------------------------------
s.geometry('800x600')
s.configure(bg="#000000")
s.title("Entry Terminal")

#title-------------------------------------------------------------------------------------
main_title = Label(s, text="Edit Current Game", font=("Terminal",20,"bold"),bg="black",fg="indigo")
main_title.pack(side="top", pady=10)


#creates a canvas for the general layout ------------------------------------------------
canvas = Canvas(s, width=500, height=450, bg="grey")
canvas.pack()
#make the red side
canvas.create_rectangle(0,0,250,500, fill="dark red", outline="grey")
canvas.create_text(125,15, text="Red Team",font=("Terminal",15,"bold"), fill="#ff746c")
#make the green side 
canvas.create_rectangle(250,0,500,450, fill="dark green", outline="grey")
canvas.create_text(375,15, text="Green Team",font=("Terminal",15,"bold"), fill="#CFFDBC")

#entry boxes ---------------------------------------------------------------------------
red_entries = []

for i in range(20):
    entry= Entry(s, width=20)
    entry.pack()
    canvas.create_window(100, 40 + (i*20), window=entry)

green_entries = []

for i in range(20):
    entry= Entry(s, width=20)
    entry.pack()
    canvas.create_window(350, 40 + (i*20), window=entry)


#bottom buttons 
#check if this can be looped 
def do_nothing(): 
    print("Button Clicked")

f1 = Button(s, text="F1 \n Edit \n Game",bg="black",fg="green", command=do_nothing)
f1.place(x=0,y=520,width=70,height=80)

f2 = Button(s, text="F2 \n Game \n Parameters",bg="black",fg="green", command=do_nothing)
f2.place(x=70,y=520,width=70,height=80)

f3 = Button(s, text="F3 \n Start \n Game",bg="black",fg="green", command=do_nothing)
f3.place(x=140,y=520,width=70,height=80)

f5 = Button(s, text="F5 \n PreEntered \n Games",bg="black",fg="green", command=do_nothing)
f5.place(x=280,y=520,width=70,height=80)

f7 = Button(s, text="F7 \n  \n ",bg="black",fg="green", command=do_nothing)
f7.place(x=420,y=520,width=70,height=80)

f8 = Button(s, text="F8 \n View \n Game",bg="black",fg="green", command=do_nothing)
f8.place(x=490,y=520,width=70,height=80)

f10 = Button(s, text="F10 \n Flick \n Sync",bg="black",fg="green", command=do_nothing)
f10.place(x=630,y=520,width=70,height=80)

f12 = Button(s, text="F10 \n Clear \n Game",bg="black",fg="green", command=do_nothing)
f12.place(x=730,y=520,width=70,height=80)

s.mainloop() 