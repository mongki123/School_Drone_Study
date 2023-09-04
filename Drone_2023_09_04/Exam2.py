# 이미지를 읽어 텍스트 변환 예제

from PIL import Image
import pytesseract

image_path = r"ExamImage.png" # 이미지 저장 경로

img = Image.open('ExamImage.png')
pytesseract.pytesseract.tesseract_cmd = r'c:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(img,lang='kor+eng')
# 이미지에서 한글을 찾아 문자로 추출

print(text) # 추출된 문자 출력

