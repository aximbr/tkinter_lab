import tkinter as tk

root = tk.Tk()
root.title("Checkbutton widget")
root.minsize(300,200)

tk.Label(root, text="Select your favorites fruits:").pack()
tk.Checkbutton(root, text="Apple").pack()
tk.Checkbutton(root, text="Banana").pack()
tk.Checkbutton(root, text="Orange").pack()
tk.Checkbutton(root, text="Grape").pack()
tk.Checkbutton(root, text="Peach").pack()
tk.Checkbutton(root, text="Metabrains", state="disabled").pack()

root.mainloop()