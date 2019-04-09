# coding=utf8
import tkinter as tk
from tkinter import messagebox
import time
from pathlib import Path
import csv
import pickle

start = time.time()
zehnMinuten = 600
noInitialVote = 1

votes = {'doors': 0,
         'tessy': 0,
         'canape': 0,
         'eclipse': 0,
         'ea': 0,
         'notepad': 0,
         'mplab': 0,
         'lotus': 0,
         'bob': 0,
         }

results = {'module' : 'test', 'counter': 0}     
try:    
    with open('data.csv', 'rb') as testfile:
        votes = pickle.load(testfile)
        results = pickle.load(testfile)
except:
    print("Started first time")

window = tk.Tk()
window.configure(background = 'darkgrey')
window.title("drecksToolAnalyzer")
window.geometry("1300x1024")
window.iconbitmap('rickroll.ico')

def updateResults():
    global votes, results
    for tool in votes:
        if votes[tool] > results['counter']:
            results['counter'] = votes[tool]
            results['module'] = tool
    with open('data.csv', 'wb') as testfile:
        pickle.dump(votes, testfile)
        pickle.dump(results, testfile)
        
def doorsCallBack():
    global start, votes, zehnMinuten, noInitialVote
    pastTime = time.time() - start
    if(pastTime > zehnMinuten or noInitialVote):
        messagebox.showinfo( "Vote counted", "You voted for Doors")
        votes['doors'] += 1
        Doors.flash()
        start = time.time()
        if(noInitialVote):
            noInitialVote = 0
    else:
        messagebox.showinfo( "Be patient", "Wait {} more seconds".format(600 - int(pastTime)))
    noInitialVote = 0
    with open('data.csv', 'wb') as testfile:
        pickle.dump(votes, testfile)
        pickle.dump(results, testfile)
        
def tessyCallBack():
    global start, votes, zehnMinuten, noInitialVote
    pastTime = time.time() - start
    if(pastTime > zehnMinuten or noInitialVote):
        messagebox.showinfo( "Vote counted", "You voted for Tessy")
        votes['tessy'] += 1
        Tessy.flash()
        start = time.time()
        if(noInitialVote):
            noInitialVote = 0
    else:
        messagebox.showinfo( "Be patient", "Wait {} more seconds".format(600 - int(pastTime)))
    noInitialVote = 0
    with open('data.csv', 'wb') as testfile:
        pickle.dump(votes, testfile)
        pickle.dump(results, testfile)
        
def canApeCallBack():
    global start, votes, zehnMinuten, noInitialVote
    pastTime = time.time() - start
    if(pastTime > zehnMinuten or noInitialVote):
        messagebox.showinfo( "Vote counted", "You voted for CanApe")
        votes['canape'] += 1
        CanAPE.flash()
        start = time.time()
        if(noInitialVote):
            noInitialVote = 0
    else:
        messagebox.showinfo( "Be patient", "Wait {} more seconds".format(600 - int(pastTime)))
    noInitialVote = 0
    with open('data.csv', 'wb') as testfile:
        pickle.dump(votes, testfile)
        pickle.dump(results, testfile)

def eclipseCallBack():
    global start, votes, zehnMinuten, noInitialVote
    pastTime = time.time() - start
    if(pastTime > zehnMinuten or noInitialVote):
        messagebox.showinfo( "Vote counted", "You voted for Eclipse")
        votes['eclipse'] += 1
        Eclipse.flash()
        start = time.time()
        if(noInitialVote):
            noInitialVote = 0
    else:
        messagebox.showinfo( "Be patient", "Wait {} more seconds".format(600 - int(pastTime)))
    noInitialVote = 0
    with open('data.csv', 'wb') as testfile:
        pickle.dump(votes, testfile)
        pickle.dump(results, testfile)
    
def eaCallBack():
    global start, votes, zehnMinuten, noInitialVote
    pastTime = time.time() - start
    if(pastTime > zehnMinuten or noInitialVote):
        messagebox.showinfo( "Vote counted", "You voted for Enterprise Architect")
        votes['ea'] += 1
        EA.flash()
        start = time.time()
        if(noInitialVote):
            noInitialVote = 0
    else:
        messagebox.showinfo( "Be patient", "Wait {} more seconds".format(600 - int(pastTime)))
    noInitialVote = 0
    with open('data.csv', 'wb') as testfile:
        pickle.dump(votes, testfile)
        pickle.dump(results, testfile)
        
def notepadCallBack():
    global start, votes, zehnMinuten, noInitialVote
    pastTime = time.time() - start
    if(pastTime > zehnMinuten or noInitialVote):
        messagebox.showinfo( "Vote counted", "You voted for Notepad++. Shame on you")
        votes['notepad'] += 1
        Notepad.flash()
        start = time.time()
        if(noInitialVote):
            noInitialVote = 0
    else:
        messagebox.showinfo( "Be patient", "Wait {} more seconds".format(600 - int(pastTime)))
    noInitialVote = 0
    with open('data.csv', 'wb') as testfile:
        pickle.dump(votes, testfile)
        pickle.dump(results, testfile)
        
def mplabCallBack():
    global start, votes, zehnMinuten, noInitialVote
    pastTime = time.time() - start
    if(pastTime > zehnMinuten or noInitialVote):
        messagebox.showinfo( "Vote counted", "You voted for MPLAB-X")
        votes['mplab'] += 1
        MPLAB.flash()
        start = time.time()
        if(noInitialVote):
            noInitialVote = 0
    else:
        messagebox.showinfo( "Be patient", "Wait {} more seconds".format(600 - int(pastTime)))
    noInitialVote = 0
    with open('data.csv', 'wb') as testfile:
        pickle.dump(votes, testfile)
        pickle.dump(results, testfile)
    
def lotusCallBack():
    global start, votes, zehnMinuten, noInitialVote
    pastTime = time.time() - start
    if(pastTime > zehnMinuten or noInitialVote):
        messagebox.showinfo( "Vote counted", "You voted for Lotus Notes")
        votes['lotus'] += 1
        Lotus.flash()
        start = time.time()
        if(noInitialVote):
            noInitialVote = 0
    else:
        messagebox.showinfo( "Be patient", "Wait {} more seconds".format(600 - int(pastTime)))
    noInitialVote = 0
    with open('data.csv', 'wb') as testfile:
        pickle.dump(votes, testfile)
        pickle.dump(results, testfile)
        
def bobCallBack():
    global start, votes, zehnMinuten, noInitialVote
    pastTime = time.time() - start
    if(pastTime > zehnMinuten or noInitialVote):
        
        widget = tk.Label(window, compound='top')
        widget.bobvote_png = tk.PhotoImage(file ="bobvote.gif")
        widget['text'] = "Someone accidently voted for Bob"
        widget['image'] = widget.bobvote_png
        widget.pack(expand = True)
        votes['bob'] += 1
        Bob.flash()
        start = time.time()
        if(noInitialVote):
            noInitialVote = 0
    else:
        messagebox.showinfo( "Be patient", "Wait {} more seconds".format(600 - int(pastTime)))
    with open('data.csv', 'wb') as testfile:
        pickle.dump(votes, testfile)
        pickle.dump(results, testfile)
    
        
def resultsCallBack():
    global start, votes
    updateResults()
    messagebox.showinfo( "Results", "Drecks tool: {}, Number of votes: {}".format(results['module'], results['counter']))
    Results.flash()
        
        

       
   
   
   
Doors = tk.Button(window, text ="Doors", width = 50, height = 3, command = doorsCallBack, bg="yellow")
Doors.place(x = 35,y = 50)
Doors.pack()

Tessy = tk.Button(window, text ="Tessy", width = 90, height = 5, command = tessyCallBack, bg="yellow")
Tessy.place(x = 35,y = 50)
Tessy.pack()

CanAPE = tk.Button(window, text ="CanAPE", width = 50, height = 3, command = canApeCallBack, bg="yellow")
CanAPE.place(x = 35,y = 50)
CanAPE.pack()

Eclipse = tk.Button(window, text ="Eclipse", width = 50, height = 3, command = eclipseCallBack, bg="yellow")
Eclipse.place(x = 35,y = 50)
Eclipse.pack()

EA = tk.Button(window, text ="Enterprise Architect", width = 50, height = 3, command = eaCallBack, bg="yellow")
EA.place(x = 35,y = 50)
EA.pack()

Notepad = tk.Button(window, text ="Notepad", width = 50, height = 3, command = notepadCallBack, bg="yellow")
Notepad.place(x = 35,y = 50)
Notepad.pack()

MPLAB = tk.Button(window, text ="MPLAB-X", width = 50, height = 3, command = mplabCallBack, bg="yellow")
MPLAB.place(x = 35,y = 50)
MPLAB.pack()

Lotus = tk.Button(window, text ="Lotus", width = 50, height = 3, command = lotusCallBack, bg="yellow")
Lotus.place(x = 35,y = 50)
Lotus.pack()

Bob = tk.Button(window, text ="Bob", width = 10, height = 1, command = bobCallBack, bg="darkgrey")
Bob.place(x = 35,y = 50)
Bob.pack()

Results = tk.Button(window, text ="Show result", width = 50, height = 3, command = resultsCallBack, bg="red")
Results.place(x = 35,y = 50)
Results.pack()

labelframe = tk.LabelFrame(window, text="Anleitung:")
labelframe.pack(fill="both", expand="yes", )

left = tk.Label(labelframe, text="Everyone please feel free to vote your favourite Dreckstool of the day once every 10 minutes :)")
left.pack()


window.mainloop()
