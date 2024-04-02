import tkinter as tk

root = tk.Tk()
root.title("Menu widget")

root.minsize(300,200)

mainmenu = tk.Menu(root)

# File Menu starts here
filemenu = tk.Menu(mainmenu, tearoff=0)
filemenu.add_command(label= "New Text File")
filemenu.add_command(label= "New File")
filemenu.add_command(label= "New Window")
filemenu.add_separator()
filemenu.add_command(label= "Open File")
filemenu.add_command(label= "Open Folder")

mainmenu.add_cascade(label="File", menu= filemenu)
# Open Recent menu starts here
openrecent = tk.Menu(mainmenu)
openrecent.add_command(label="File 1 11/01/2024")
openrecent.add_command(label="File 2 10/01/2024")
openrecent.add_command(label="File 3 09/01/2024")
openrecent.add_command(label="File 4 08/01/2024")

filemenu.add_cascade(label="Open recent", menu=openrecent)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)

# Edit menu starts here
editmenu = tk.Menu(mainmenu)
editmenu.add_command(label= "undo")
editmenu.add_command(label= "redo")
editmenu.add_separator()
editmenu.add_command(label= "Copy")
editmenu.add_command(label= "Cut")
editmenu.add_command(label= "Paste")
editmenu.add_separator()
editmenu.add_command(label= "Find")
editmenu.add_command(label= "Replace")

mainmenu.add_cascade(label="Edit", menu= editmenu)
# View menu starts here
viewmenu = tk.Menu(mainmenu)
viewmenu.add_command(label= "Command Palette")
viewmenu.add_command(label= "Open View")
viewmenu.add_separator()
viewmenu.add_command(label= "Apperance")
viewmenu.add_command(label= "Editor Layout")
viewmenu.add_separator()
viewmenu.add_command(label= "Explore")
viewmenu.add_command(label= "Test")

mainmenu.add_cascade(label="View", menu= viewmenu)
root.config(menu= mainmenu)

root.mainloop()