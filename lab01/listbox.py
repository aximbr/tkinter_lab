import tkinter as tk

root = tk.Tk()
root.title("ListBox widget")

root.minsize(300,200)

l = tk.Listbox(root, width=15, height=10, justify="center", selectbackground="red", selectmode="extended")

for item in range(15):
    l.insert("end", item)

l.pack()

root.mainloop()