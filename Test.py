from sys import version_info
if version_info.major == 2:
   import Tkinter as tk
elif version_info.major == 3:
   import tkinter as tk
from tkinter import ttk



class Application(tk.Frame):
   def __init__(self, master=None):
       super().__init__(master)
       self.master = master
       self.pack()
       self.create_widgets()
       self.master.configure(bg='blue')
   def create_widgets(self):

       self.Text = tk.Text(root, height=12, width=30)
       self.Text.pack()
       self.Text.insert(tk.END, "Hvad vi har brugt")


       self.quit = tk.Button(self, text="QUIT", fg="blue",
                             command=self.master.destroy)
       self.quit.pack(side="top")


root = tk.Tk()
root.geometry("300x250")
app = Application(master=root)
app.mainloop()
#Virker