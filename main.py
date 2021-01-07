import cv2
import winsound
import pywhatkit
import pytz
import datetime
def alert():
    time1 = pytz.timezone('Europe/London')
    time2 = datetime.datetime.now().strftime('%H:%M')
    print(time2)
    time3 = time2
    time3 = time3.replace(':', '')
    time4 = list(time3)
    print(time4)
    time5 = str(time4.pop(0))
    time5 = time5 + str(time4.pop(-3))
    time6 = str(time4.pop(-2))
    time6 = time6 + str(time4.pop(-1))
    print(time5)
    print(time6)
    time5 = int(time5)
    time6 = int(time6)
    time6 = 1 + time6
    pywhatkit.sendwhatmsg('+919810220510', 'Theif',time5,time6 )


cam = cv2.VideoCapture(0)
while cam.isOpened():
    ret,frame1 = cam.read()
    ret,frame2 = cam.read()
    diff = cv2.absdiff(frame1,frame2)
    gray = cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    _, thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh,None,iterations =3)
    contours,_ = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame1,contours,-1,(0,255,0),2)
    for c in contours:
        if cv2.contourArea(c)< 5000:
            continue
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        winsound.Beep(500,200)
        # alert()
    if cv2.waitKey(10)==ord('q'):
        break
    cv2.imshow('security Cam',frame1)


