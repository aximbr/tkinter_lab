import tkinter as tk

root = tk.Tk()
root.title("canvas widget")

root.minsize(300,200)

canvas = tk.Canvas(root, bg="blue", width=500, height=500)

rect = 10, 10, 100, 50
canvas.create_rectangle(rect, fill="green")

sqrd = 50, 50, 100, 100
canvas.create_rectangle(sqrd, fill="orange")

line = 20, 20, 150, 200, 100, 300
canvas.create_line(line, fill="red")

oval = 30,30, 200, 200
canvas.create_oval(oval, fill="gray")

cord = 50,50, 120, 250
canvas.create_arc(cord, start=0, extent=150, fill="purple")

pol = 50,50, 120, 250, 450, 300
canvas.create_polygon(pol, fill="pink")

canvas.pack()
root.mainloop()