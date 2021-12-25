import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter import StringVar

def beonyeok(csvfilepath, rpyfilepath):
    data = pd.read_csv(csvfilepath)
    print(data.keys())
    untrans = data[data.keys()[0]]
    trans = data[data.keys()[1]]

    readdat = []
    for i in range(0,len(untrans)):
        readdat.append([untrans[i].replace("\"",r"\""), trans[i]])
    
    f = open(rpyfilepath, "r+")
    dat = f.read()

    #replace all strings with the batched translation
    for [u,t] in readdat:
        dat = dat.replace(u,t)

    #reverse the first being accidentally translated
    for [u,t] in readdat:
        dat = dat.replace(t,u,1)

    #open writefile
    w = open(rpyfilepath[0:-4]+"edit.rpy", "w")
    
    showinfo(
        title="Success!",
        message=str(w.write(dat))+" lines written to ["+rpyfilepath[0:-4]+"edit.rpy "+"] Finished :D"
    )
    f.close()
    w.close()

#debug
#beonyeok("./game/williamroute2.csv", "./game/williamroute2.rpy")

root = tk.Tk()
root.title('Import CSV Trans to Rpy')
root.geometry('650x300')

file1 = StringVar()
file1.set("no file selected")
file2 = StringVar()
file2.set("no file selected")

def select_rpyfile():
    filetypes = (
        ('rpy files', '*.rpy'),
        ('all files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open rpy',
        initialdir='./',
        filetypes=filetypes)

    file1.set(filename)

def select_csvfile():
    filetypes = (
        ('csv files', '*.csv'),
        ('all files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open csv',
        initialdir='./',
        filetypes=filetypes)

    file2.set(filename)

# open button
open_buttonrpy = ttk.Button(
    root,
    text='Open rpy',
    command=select_rpyfile
)

open_buttoncsv = ttk.Button(
    root,
    text='Open csv',
    command=select_csvfile
)

def conditionalb():
    if file1.get()!="no file selected" and file2.get()!= "no file selected":
        beonyeok(file2.get(), file1.get())
    else: showinfo(
        title="Error",
        message="No file selected!"
    )

generate_button = ttk.Button(
    text="GENERATE!",
    command=conditionalb
)

open_buttonrpy.grid(column=1, row=0, padx=(0,20))
tk.Label(text="Select your rpy file!").grid(column=0, row = 0, padx =(20,20), pady = (20,20))
tk.Label(textvariable=file1).grid(column=2, row = 0)

open_buttoncsv.grid(column=1, row=1, padx=(0,20))
tk.Label(text="Select your csv file!").grid(column=0, row = 1, padx =(20,20), pady = (20,20))
tk.Label(textvariable=file2).grid(column=2, row = 1)

generate_button.grid(column = 0, row = 2)
# run the application
root.mainloop()
