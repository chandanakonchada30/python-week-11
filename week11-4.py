#24331A05E2
#To design and develop a GUI application using CheckButton and Radiobuttonwidgets.
import tkinter as tk
root = tk.Tk()
root.title("Languages")
# Checkbuttons
tk.Label(root, text="Languages you know:").pack()
c = tk.IntVar()
python = tk.IntVar()
tk.Checkbutton(root, text="C", variable=c).pack()
tk.Checkbutton(root, text="Python", variable=python).pack()
tk.Label(root, text="Favorite language:").pack()
fav = tk.StringVar()
tk.Radiobutton(root, text="C", variable=fav, value="C").pack()
tk.Radiobutton(root, text="Python", variable=fav, value="Python").pack()
root.mainloop()