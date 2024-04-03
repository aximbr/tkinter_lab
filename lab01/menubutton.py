import tkinter as tk

root = tk.Tk()
root.title("Menu Button widget")

menubutton = tk.Menubutton(root, text="Select Options")

menu = tk.Menu(menubutton, tearoff=False)

menubutton["menu"] = menu
menu.add_command(label="Option 1")
menu.add_command(label="Option 2")
menu.add_command(label="Option 3")
menu.add_command(label="Option 4")

menubutton.pack()

root.minsize(300,200)

root.mainloop()