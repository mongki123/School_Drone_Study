# 영문 텍스트를 읽어 한글 텍스트로 저장하는 예제

from os import linesep
from googletrans import Translator
translator = Translator()

read_file_path = "English.txt"
write_file_path = "Korea.txt"

f = open("English.txt", 'r')
lines = f.readlines()

for line in lines:
    result1 = translator.translate(line, dest = 'ko')
    print(result1.text)
    with open(write_file_path, 'a', encoding='UTF8') as f:
        f.write(result1.text + '\n')