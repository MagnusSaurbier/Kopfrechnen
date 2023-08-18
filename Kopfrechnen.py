import tkinter as tk
import random
import time

from Kopfrechnen_gamemodes import gamemodes

root = tk.Tk()
root.title("2-digit squares")
root.geometry("400x400")
root.resizable(False, False)

# globals
answered = False
task = ""
result = 0
gamemode = gamemodes[0]


Task = tk.Label(root, text="Task", font=("Arial", 40))
Task.pack(pady=20)
Answer = tk.Entry(root, font=("Arial", 40))
Answer.pack(pady=20)
Result = tk.Label(root, text="", font=("Arial", 40))
Result.pack(pady=20)
Next = tk.Button(root, text="Next", font=("Arial", 40))
Next.pack(pady=20)

Menu = tk.Menu(root)
root.config(menu=Menu)
TaskTypeMenu = tk.Menu(Menu)
Menu.add_cascade(label="Task Type", menu=TaskTypeMenu)
for g in gamemodes:
    t = g.title
    TaskTypeMenu.add_command(label=t, command=lambda g=g: setTaskType(g))
    
def setTaskType(g):
    global gamemode
    gamemode = g
    root.title(g.title)
    next()

def makeTask():
    return gamemode.makeTask()

def next():
    global answered, task, result
    task, result = makeTask()

    Task.config(text=task)
    Answer.delete(0, tk.END)
    Result.config(text="")
    Answer.focus()
    Next.config(state="disabled")

    answered = False

def check():
    try: answer = int(Answer.get())
    except: pass
    Result.config(text=result)
    if result == answer:
        Result.config(fg="lightgreen")
    else:
        Result.config(fg="red")
    Next.config(state="normal")

    global answered
    answered = True

def click():
    print("click", answered)
    if not answered: check()
    else: next()

Answer.bind("<Return>", lambda x: click())
Next.config(command=next)

next()
root.mainloop()