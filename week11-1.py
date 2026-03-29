#24331A05E2
#To design and develop a GUI application to display ―Hello World.
import tkinter as tk
def show_text():
    text = entry.get()
    result_label.config(text="Hello " + text)
root = tk.Tk()
root.title("GUI Application")
label = tk.Label(root, text="Enter your name:")
label.pack()
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="Submit", command=show_text)
button.pack()
result_label = tk.Label(root, text="")
result_label.pack()
root.mainloop()