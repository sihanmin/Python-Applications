import Tkinter as Tk #or tkinter in v.3

class RectangleGUI:
   def __init__(self, master):
	   self.master = master
	   self.canvas = Tk.Canvas(master, width=500, height=500)
	   self.canvas.pack()
	   self.canvas.bind("<Button-1>", self.rectangle)
   def rectangle(self,ev):
	   self.canvas.create_rectangle(ev.x, ev.y, ev.x+20, ev.y+20, fill="blue")
       
root = Tk.Tk()
gui=RectangleGUI(root)
root.mainloop()