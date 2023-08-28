# GUI 예제 3 ( 예제 1 응용 )

import tkinter as tk

window = tk.Tk()

window.title('GUI예제')

counter1 = 0
counter2 = 0

def clicked1():
    global counter1
    counter1 += 1
    label1['text'] = '버튼 클릭 수: ' + str(counter1)

def reset1():
    global counter1
    counter1 = 0
    label1['text'] = '아래에 버튼이 있습니다.'

def clicked2():
    global counter2
    counter2 += 1
    label2['text'] = '버튼 클릭 수: ' + str(counter2)

def reset2():
    global counter2
    counter2 = 0
    label2['text'] = '아래에 버튼이 있습니다.'

label1 = tk.Label(window, text='아래에 버튼이 있습니다.', fg = 'blue', font = 20)

label1.pack(padx=10, pady=10, side = 'left')

button1 = tk.Button(label1, text = "클릭해 보세요.", bg = 'green', font = 15, width = 30, height = 5, command = clicked1)

button1.pack(padx=10, pady=10)

button2 = tk.Button(label1, text = "reset", bg = 'red', font = 15, width = 30, height = 5, command = reset1)

button2.pack(padx=10, pady=10)



label2 = tk.Label(window, text='아래에 버튼이 있습니다.', fg = 'blue', font = 20)


label2.pack(padx=10, pady=10, side = 'right')

button3 = tk.Button(label2, text = "클릭해 보세요.", bg = 'green', font = 15, width = 30, height = 5, command = clicked2)

button3.pack(padx=10, pady=10)

button4 = tk.Button(label2, text = "reset", bg = 'red', font = 15, width = 30, height = 5, command = reset2)

button4.pack(padx=10, pady=10)

window.mainloop()