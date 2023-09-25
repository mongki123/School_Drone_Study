# CCTV

import time
import datetime as dt
import numpy as np
import cv2

cap = cv2.VideoCapture(0) # cap 이 여래대인 경우 0, 1, 2, 3... 을 넣어 주면 된다.
cap.set(3,640) # 영상 가로 넓이 설정
cap.set(4,480) # 영상 세로 넓이 설정

# 코덱 정의
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
now = dt.datetime.now()
print(now)
out = cv2.VideoWriter(r'D:\My_Python_Project\School_Drone_Study\Drone_2023_09_25\opencv1.avi',fourcc,fps,(width,height))

# 저장파일명, 코덱, 재생속도, 크기
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1) # 영상 상하반전유무에 따라 0,1 을 사용
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # 영상 처리를 위한 흑백 처리 

    cv2.imshow('frmae', frame)
    out.write(frame) # 영상데이터만 저장
    cv2.imshow('gray', gray)
    cv2.imwrite('D:\My_Python_Project\School_Drone_Study\Drone_2023_09_25\opencv1.png', frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

out.release()
cap.release()
cv2.destroyAllwindows()