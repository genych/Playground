import tkinter


def callback(event):
    """ Move current item to the background """
    event.widget.tag_lower(event.widget.find_withtag('current'))


root = tkinter.Tk()
img = tkinter.PhotoImage(file='../static/fun.gif')
canvas = tkinter.Canvas(root, width=240, height=40, bg='black')
canvas.pack()
canvas.bind('<1>', callback)

bottom = [canvas.create_rectangle(x, 0, x+40, 40, fill="blue") 
          for x in (0, 100, 200)]
top = [canvas.create_image(x, 0, image=img, anchor='nw') for x in (0, 100, 200)]

root.mainloop()
