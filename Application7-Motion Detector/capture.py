import cv2, time, pandas
from datetime import datetime

first_frame=None
status_list=[None,None]
times=[]
df=pandas.DataFrame(columns=["Start","End"])

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    status=0

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0) #its for the grayscale

    if first_frame is None:  #here if the first video screen is normal then let it be gray yeeeeeeehhh!!
        first_frame=gray
        continue

    delta_frame=cv2.absdiff(first_frame,gray)       #its just like delta force and absoulute difference helps to find that
    thresh_frame=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]      #this window will actually set the difference between the moving object as white
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2) #it dilates potholes in frame

    (_,cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # contour representing the shape or form

    for contour in cnts:       #here its time to put the rectangle again ..
        if cv2.contourArea(contour) < 1000:
            continue
        status=1 #it will comes in else statment so that it doesn't capture green on all objects samjhe kuch..
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),3)

    status_list.append(status)
    if status_list[-1]==1 and status_list[-2]==0: #this list describes the changes take when an object comes into picture
        times.append(datetime.now())  #it lets you capture the current time of the visibility of the object
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())
    cv2.imshow("Gray Frame",gray)
    cv2.imshow("Delta Frame",delta_frame)
    cv2.imshow("Threshold Frame",thresh_frame)
    cv2.imshow("Color Frame",frame)

    key=cv2.waitKey(1)

    if key==ord('q'):       #it is to close the windows
        if status==1:
            times.append(datetime.now())
        break

print(status_list)
print(times)

for i in range(0,len(times),2):
    df=df.append({"Start":times[i],"End":times[i+1]},ignore_index=True)

df.to_csv("Times.csv")

video.release()
cv2.destroyAllWindows()
