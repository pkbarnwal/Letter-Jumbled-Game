from tkinter import *
import tkinter
import random
from tkinter import messagebox
answers= [
        "laptop",
        "javascript",
        "bhopal",
        "computer",
        "school",
        "india",
        "college",
        "principal",
        "principle",
        "java",
        "python",
        "mobile",
        "key",
        "bottle",
        "chalk",
        "language",
        "friday",
        "january",
        "book",
        "library",
        "button",
        ]
words= [
      "patlpo",
      "vascjapirt",
      "lbhapo",
      "omcuertp",
      "chsolo",
      "nidai",
      "olcleeg",
      "rpnipclai",
      "lriipnpec",
      "ajav",
      "tyhnop",
      "obleim",
      "kye",
      "tbotel",
      "hcakl",
      "galaengu",
      "rfyadi",
      "naayruj",
      "kobo",
      "ilrbyar",
      "utonbt",
      ]
num=random.randrange(0,21,1)
def reSet():
    global num,words,answers
    num=random.randrange(0,21,1)
    lbl.config(text=words[num])
    e1.delete(0,END)




def default():
    global num,words,answers
    lbl.config(text=words[num])

def checkAns():
    global num,words,answers
    var=e1.get()
    if var == answers[num]:
        reSet()
    else:
        messagebox.showerror("Wrong Spelling !! Try again....")
        e1.delete(0,END)








window=Tk()
window.title("Word Game")

window.geometry("450x500+350+150")
window.config(background="#000000")


#img=PhotoImage(file="LOGOquiz.png")
#lblimage=Label(window,image=img,background="#ffffff")
#lblimage.pack()
lbl1=Label(window,
           text="Welcome,Let's Play jumbled",
           font=("Courier New",18),
           fg="#3742fa",
           bg="#ffffff",
           )
lbl1.pack(pady={25})

lbl=Label(window,
          text="This is first question",
          font=("verdana",18),
          bg="#000000",
          fg="#ffffff",
          state=ACTIVE,
          )
         
lbl.pack(pady=25,ipady=10,ipadx=10)


ans=StringVar()
e1=Entry(
         window,
         font=("verdana",16),
         state=NORMAL,
         textvariable=ans,
         )
e1.pack(ipady=5,ipadx=5)

btncheck=Button(
             window,
             text="Check",
             font=("Comic sans ms",14),
             width=10,
             bg="#4C4B4B",
             fg="#6ab04c",
             relief=GROOVE,
             state=NORMAL,
             command=checkAns,
             )
btncheck.pack(pady=30)

btnreset=Button(
             window,
             text="Reset",
             font=("Comic sans ms",14),
             width=10,
             bg="#4C4B4B",
             fg="#EA425C",
             relief=GROOVE,
             state=NORMAL,
             command=reSet   ,
             )
btnreset.pack()
default()
window.mainloop() 

