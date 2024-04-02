import tkinter as tk

root = tk.Tk()
root.title("Frame widget")

root.minsize(300,200)

frame = tk.Frame(root, bg="red", width=400, height=400)

 


label = tk.Label(frame, text="This is a label widget", bg="lightgreen", font="calibri", wraplength=100, padx=10, pady=10).pack()
for text, value in [("apple", 1), ("banana", 2), ("orange", 3), ("strawberry", 5)]:
    tk.Radiobutton(frame, text=text, value=value, indicatoron=0, width=20).pack()

frame.pack()
root.mainloop()