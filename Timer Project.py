from tkinter import *
root=Tk()
root.geometry("200x150")
root.title("Timer")
l1=Label(root,font="times 20")
l1.grid(row=1,column=2)
times=StringVar()
#t=times.get()
e1=Entry(root,textvariable=times)
e1.grid(row=3,column=2)
#t=0
#def set_timer():
 #   global t
  #  t=t+int(e1.get())
   # return t
k=0
def stop():
    global k
    k=1
def start():
    global t
    t=int(times.get())
    countdown()
def countdown():
    global t,k
    if t>0:
        if k>0:
            k=0
        else:
            l1.config(text=t)
            t=t-1
            l1.after(1000,countdown)
    else:
        l1.config(text="END")
b1=Button(root,text="START",width=20,command=start).grid(row=4,column=2,padx=20)
b2=Button(root,text="STOP",width=20,command=stop).grid(row=6,column=2,padx=20)
b3=Button(root,text="RESUME",width=20,command=countdown).grid(row=8,column=2,padx=20)

root.mainloop()

            
