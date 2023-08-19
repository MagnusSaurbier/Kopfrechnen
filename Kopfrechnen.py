import tkinter as tk
import random
import time

from Kopfrechnen_gamemodes import gamemodes

# GUI
root = tk.Tk()
root.geometry("800x400")
root.resizable(False, False)

# globals
answered = False # True if answer was checked, False if Task is shown and answer is yet to be revealed
task = "" # task to be solved
result = 0 # correct result of task
gamemode = gamemodes["Multiplication"][0] # current gamemode

# GUI elements
Task = tk.Label(root, text="Task", font=("Arial", 40))
Task.pack(pady=20)
Answer = tk.Entry(root, font=("Arial", 40))
Answer.pack(pady=20)
Result = tk.Label(root, text="", font=("Arial", 40))
Result.pack(pady=20)
Next = tk.Button(root, text="Next", font=("Arial", 40))
Next.pack(pady=20)

# Tasktype selection menu
Menu = tk.Menu(root)
root.config(menu=Menu)
for category in gamemodes:
    categoryMenu = tk.Menu(Menu)
    Menu.add_cascade(label=category, menu=categoryMenu)
    for g in gamemodes[category]:
        t = g.title
        categoryMenu.add_command(label=t, command=lambda g=g: setTaskType(g))
    
def setTaskType(g):
    """Set gamemode to g"""
    global gamemode
    gamemode = g
    root.title(g.title)
    next()

def next():
    """Generate new task"""
    global answered, task, result, gamemode
    task, result = gamemode.makeTask()

    Task.config(text=task)
    Answer.delete(0, tk.END)
    Result.config(text="")
    Answer.focus()
    Next.config(state="disabled")

    answered = False # new task is to be solved

def checkAnswer():
    """Check if answer is correct, show result in green or red"""
    try: answer = int(Answer.get())
    except: pass
    Result.config(text=result)
    if result == answer:
        Result.config(fg="lightgreen")
    else:
        Result.config(fg="red")
    Next.config(state="normal")

    global answered
    answered = True # answer was checked

def PressedEnter():
    """Callback for Enter key: Switches state between answered and not answered"""
    print("click", answered)
    if not answered: checkAnswer()
    else: next()

Answer.bind("<Return>", lambda x: PressedEnter())
Next.config(command=next)

next()
root.mainloop()