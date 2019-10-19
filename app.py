import tkinter as tk
from tkinter import filedialog, Text
import os

# creating the main "frame" of the app
root = tk.Tk()
apps = []

# verifying the apps
if os.path.isfile('save.txt'):
  with open('save.txt', 'r') as f:
    temp = f.read()
    apps = [x for x in temp.split(',') if x.strip()] # gets rid of the empty spaces
    print(apps)

def createLabel():
  for app in apps:
    label = tk.Label(frame, text=app, bg="gray") # creates a label for every app
    label.pack()

# creating a filedialog function to search for files
def addApp():
  for widget in frame.winfo_children():
    widget.destroy()

  filename = filedialog.askopenfilename(initialdir="/", title="Select a file", filetypes=(("executables", "*.exe"), ("all files", "*.*")))
  
  apps.append(filename) # storing all the apps in an array
  print(filename)

# creating a function to actually run the apps
def runApps():
  for app in apps:
    os.startfile(app)

# creating a canvas for "root"
canvas = tk.Canvas(root, height=670, width=670, bg="#263D31")
canvas.pack()  # runs the canvas

# creating a second frame in the main app
frame = tk.Frame(root, bg="white") 
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1) # placing the frame
# using relx and rely to specify the position of the frame; in this case it will be positioned in the middle

# creating a button for opening the file
openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D31", command=addApp)
openFile.pack() # placing the button

# creating a button for running the programs that you want in your workspace
runApps = tk.Button(root, text="Run The Apps", padx=10, pady=5, fg="white", bg="#263D31", command=runApps)
runApps.pack()

createLabel()

# runs the app
root.mainloop()

with open('save.txt', 'w') as f:
  for app in apps:
    f.write(app + ',')