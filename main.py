from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename

window=Tk()
window.title("Codingal Text Editor")
window.geometry('600x500')
window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1,minsize=800,weight=1)

def openfile():
    """Open a file for editing"""
    filepath=askopenfilename(
        filetypes=[("Text Files","*.txt"),("All files","*.*")]
    )
    if not filepath:
        return
    txtedit.delete(1.0, END)
    with open(filepath, "r") as inputfile:
        text=inputfile.read()
        txtedit.insert(END, text)
        inputfile.close()
    window.title(f"Codingal Text Editor - {filepath}")

def savefile():
    """Open a file for editing"""
    filepath=asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files","*.txt"),("All files","*.*")]
    )
    if not filepath:
        return
    with open(filepath, "w") as outputfile:
        text=txtedit.get(1.0, END)
        outputfile.write(text)
    window.title(f"Codingal Text Editor - {filepath}")

txtedit=Text(window)
frbutton=Frame(window,relief=RAISED,bd=2)
btnopen=Button(frbutton,text="Open",command=openfile)
btnsave=Button(frbutton,text="Save as...",command=savefile)

btnopen.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
btnsave.grid(row=1,column=0,sticky="ew",padx=5)

frbutton.grid(row=0,column=0,sticky="ns")
txtedit.grid(row=1,column=1,sticky="nsew")

window.mainloop()