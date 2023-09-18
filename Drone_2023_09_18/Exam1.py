# Digital Clock 만들기

import tkinter as tk
from time import strftime

window = tk.Tk()
window.title("Digital Clock")

def update_time():
    current_time = strftime("%H:%M:%S") # 현재 시간 가져오기
    clock_label.config(text=current_time) # 클럭 라벨 업데이트
    window.after(1000, update_time) # 업데이트 시간 1초
    
# 클럭 라벨 구성
clock_label = tk.Label(window, font=("Family", 40), bg="blue", fg="white")
clock_label.pack(pady=40)

# 클럭 실행
update_time()
window.mainloop()