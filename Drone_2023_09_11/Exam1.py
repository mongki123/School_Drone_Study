from tkinter import *
from tkinter.filedialog import * # 파일 불러오기
from tkinter import filedialog
from os import linesep
import googletrnas
translator = googletrans.Translator() # 구글 번역기
from PIL import Image # 이미지 불러오기
import pytesseract # 이미지에서 글자 추출

def new_file(): # new_file 함수가 실행되어 텍스트 영역 삭제
    text_area.delete(1.0, END)

def open_file():
    file_path = filedialog.askopenfilename()

    print(file_path)
    date = open(file_path, 'rt', encoding="utf-8")
    text_area.delete(1.0, END)
    text_area.insert(END, data.read())

def translate_file():
    file_path = filedialog.askopenfilename()
    print(file_path)
    data = open(file_path, 'rt', encoding="utf-8")
    text_area.delete(1.0, END)
    text_area.insert(END, data.read())

    # text_area 의 값을 가져와 한국어로 번역
    result1 = translator.translate(text_area.get(1.0, END), dest='ko')
    print(result1)
    text_area.delete(1.0, END)
    text_area.insert(END, result1.text) # result1 값을 text_area 에 저장

def imagetotext_file():
    file_path = filedialog.askopenfilename()
    print(file_path)
    text_area.delete(1.0, END)
    pytesseract.pytesseract.tesseract_cmd = r'c:\Program Files\Tesseract-OCR\tesseract.exe'
    txt = pytesseract.image_to_string(Image.open(file_path), lang = 'kor') # 이미지에서 한글을 찾아 문자로 저장
    print(txt) # 추출된 문자 출력
    text_area.insert(END. txt) # result1 값을 text_area 에 저장

def save_file():
    f = asksaveasfile(mode='w', defaultextension=".txt", filetypes=[('Text file', '.txt')])
    text_save = str(text_area.get(1.0, END))
    f.write(text_save)
    f.close()

window = Tk()
window.title("메모장")
window.geometry("400x400+800+300")
window.resizable(False, False)

menu = Menu(window)
menu_1 = Menu(menu, tearoff=0)
menu_1.add_command(label="새파일", command=new_file)
menu_1.add_command(label="파일열기", command=new_file)
menu_1.add_command(label="image to text", command=imagetotext_file)
menu_1.add_command(label="English to 한글", command=imagetotext_file)
menu_1.add_command(label="저장", command=save_file)
menu_1.add_separator() # 메뉴에 줄을 추가
menu_1.add_command(label="종료", command=window.destroy)
menu.add_cascade(label="파일", menu=menu_1)

text_area = Text(window)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky= N + E + S + W)

window.config(menu=menu)

mainloop()
