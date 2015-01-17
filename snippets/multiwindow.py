from Tkinter import Tk, Toplevel, Button

def create():
    new_window = Toplevel(root, takefocus=True)
    new_window.title(string='New window')
    Button(new_window, text='Destroy them all', command=root.destroy).pack()

root = Tk()
Button(root, text='Create', command=create).pack()
root.mainloop()
