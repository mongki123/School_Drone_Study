# GUI 예제 1 ( Command )

import tkinter as tk

window = tk.Tk()

window.title('GUI예제')

counter = 0

def clicked():
    global counter
    counter += 1
    label1['text'] = '버튼 클릭 수: ' + str(counter)

def reset():
    global counter
    counter = 0
    label1['text'] = '아래에 버튼이 있습니다.'

label1 = tk.Label(window, text='아래에 버튼이 있습니다.', fg = 'blue', font = 20)

label1.pack(padx=10, pady=10)

button1 = tk.Button(window, text = "클릭해 보세요.", bg = 'green', font = 15, width = 30, height = 5, command = clicked)

button1.pack(padx=10, pady=10)

button2 = tk.Button(window, text = "reset", bg = 'red', font = 15, width = 30, height = 5, command = reset)

button2.pack(padx=10, pady=10)

window.mainloop()