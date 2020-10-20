import Tkinter as Tk #or tkinter in v.3
root = Tk.Tk()
w = Tk.Canvas(root, width=500, height=500)
w.pack()
def rectangle(event):
   w.create_rectangle(event.x,event.y, event.x+20, event.y+20, fill="red")
w.bind("<Button-1>", rectangle)

def callback():
    print "CLick again!"
    
button = Tk.Button(root, text="Click!!!", 
                   command = callback, height = 10, width = 20)
button.pack()
root.mainloop()