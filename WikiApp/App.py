# My first big app project which searches the wikipedia for you and shows you the result in the app
from tkinter import *
from time import sleep
import wikipedia
from os import *


app=Tk()
# Creating app visuals
app.geometry('320x396+0+0')
app.title('My Wiki')
app.minsize(width=320, height=396)
app.maxsize(width=900, height=500)
# app.wm_iconbitmap('')
# Visuals Done
# Button Fuctions
def search():
    print('Seaching In Wiki...')
    query = input.get()
    result_rtn = wikipedia.summary(query, sentences=10)
    print(f'The Result From Wikipedia Is: {result_rtn}')
    ResultArea.insert(1.0, result_rtn)
def exit():
    print('Exiting App')
    sleep(0.2)
    app.destroy()
"""    
def copy():
    print('Search Result Copied')
    # ResultArea.event_generate(('<<Copy>>'))                                                      
"""    
def clear():
    print('Result cleared')
    ResultArea.delete(1.0, END)
# Creating Content
title=Label(text='Hello User Welcome To My Wiki', background='black', fg='white')
title.pack(fill=X)
# User Input
input=Entry(background='black', foreground='white')
input.pack(side=BOTTOM, pady=6, fill=X, padx=5)
# Search Button
btn=Button(text='Search', background='black',foreground='white', command=search)
btn.pack(anchor='se', side=BOTTOM, padx=4)
# Exit Button
exit=Button(text='Exit App', background='black', foreground='red', command=exit)
exit.pack(anchor='se',side=BOTTOM, padx=4, pady=5)
#Function Buttons
"""
copy_btn=Button(text='Copy Result',  background='black', foreground='white', command=copy)
copy_btn.pack(side=BOTTOM, anchor=SE, padx=4, pady=2)
"""
clear_btn=Button(text='Clear Result', background='black', foreground='white', command=clear)
clear_btn.pack(side=BOTTOM, anchor=SE, padx=4, pady=2)
#====================Result Pane
result=Label(text='The Result From Wikipedia Is:-', background='black', foreground='white', border=6,relief=SUNKEN )
result.pack(side=TOP, fill=X, pady=2)
#=========Result Shown Area
ResultArea = Text(app)
ResultArea.pack(side=TOP, fill=BOTH, expand=True)
#=========Scroll Bar
Scroll = Scrollbar(ResultArea)
Scroll.pack(side=RIGHT,  fill=Y)
Scroll.config(command=ResultArea.yview)
ResultArea.config(yscrollcommand=Scroll.set)
 
app.mainloop()
# App done