import tkinter as tk


root = tk.Tk()
root.title("The button widget")

tk.Button(root, text="Click Me", relief="raised", state="disabled").pack()

root.mainloop()