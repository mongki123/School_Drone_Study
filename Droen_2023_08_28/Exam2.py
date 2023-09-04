# GUI 예제 2 ( Slide )

from tkinter import *

window = Tk()
window.title("slide 연습")
window.geometry('250x250')

vertical = Scale(window, from_ = 0, to = 200)
vertical.pack()
horizontal = Scale(window, from_ = 0 , to = 400, orient = HORIZONTAL)
horizontal.pack()

def slide():
    label1 = Label(window, text = horizontal.get()).pakc()
    window.geometry(str(horizontal.get()) + '400')

window.mainloop()