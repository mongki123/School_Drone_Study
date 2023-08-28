import tkinter

window = tkinter.Tk()
window.title(" Kim myeong gi")
window.geometry("640x480+100+100")
window.resizable(False, False)

def check():
    label.config(text = "RadioVariety_1 = " + str(RadioVariety_1.get()) + "\n" + 
                 "RadioVariety_1 = " + str(RadioVariety_1.get()) + "\n\n" + 
                 "Total = " + str(RadioVariety_1.get() + RadioVariety_2.get()))
    
RadioVariety_1 = tkinter.IntVar()
RadioVariety_2 = tkinter.IntVar()

radio1 = tkinter.Radiobutton(window, text="1번", value=1, variable=RadioVariety_1, command = check)
radio1.pack()

radio2 = tkinter.Radiobutton(window, text="2번(1번)", value=2, variable=RadioVariety_1, command = check)
radio2.pack()

radio3 = tkinter.Radiobutton(window, text="3번", value=3, variable=RadioVariety_1, command = check)
radio3.pack()

label = tkinter.Label(window, text="None", height=5)
label.pack()

radio4 = tkinter.Radiobutton(window, text="4번", value=4, variable=RadioVariety_2, command = check)
radio4.pack()

radio5 = tkinter.Radiobutton(window, text="5번", value=5, variable=RadioVariety_2, command = check)
radio5.pack()

window.mainloop()