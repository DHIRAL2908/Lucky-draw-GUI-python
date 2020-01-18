import tkinter
import tkinter.font as tfont
from random import randint

def start():
 texts.delete("1.0", tkinter.END)
 i = randint(1,2)
 if i==1:
     texts.insert(tkinter.INSERT, "You Won!\n")
 else:
     texts.insert(tkinter.INSERT, "Sorry, you lost...\n")

r = tkinter.Tk()
fonts = tfont.Font(size=32)
texts = tkinter.Text(r, width=15, height=1, bg='black', fg='violet red', font=fonts)
but = tkinter.Button(r, bg='thistle1', fg='deep pink', text="Draw", command = start)

r.title('Lucky Draw')
r.overrideredirect(1)

texts.pack()
but.pack()
tkinter.mainloop()