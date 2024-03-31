import tkinter as tk

root = tk.Tk()
root.title("Radio Button widget")

root.minsize(300,200)


for text, value in [("apple", 1), ("banana", 2), ("orange", 3), ("strawberry", 5)]:
    tk.Radiobutton(root, text=text, value=value, indicatoron=0).pack()

root.mainloop()