import tkinter as tk

root = tk.Tk()
root.title("Label")

label = tk.Label(root, text="This is a label widget", bg="lightgreen", font="calibri", wraplength=500, padx=50, pady=50)
label.pack()

root.mainloop()