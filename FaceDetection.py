import cv2

# Create Bounding Box
def draw_ped(img,label,x0,y0,xt,yt,color=(255,0,255),text_color=(255,255,255)) :
    (w,h), baseline = cv2.getTextSize(label,cv2.FONT_HERSHEY_COMPLEX,0.5,1)

    cv2.rectangle(img,
                (x0, y0 + baseline),
                (max(xt,x0 + w), yt),
                color,
                2
                )
    cv2.rectangle(img,
                (x0,y0 - h),
                (x0 + w, y0 + baseline),
                color,
                -1
                )
    cv2.putText(img,
                label,
                (x0,y0),
                cv2.FONT_HERSHEY_COMPLEX,
                0.5,
                text_color,
                1,
                cv2.LINE_AA
                )                       
    return img

# Face Detection Using Image
# img = cv2.imread("img/family.jpg")
# face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")

# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# faces = face_cascade.detectMultiScale(gray,1.3,5)

# for (x,y,w,h) in faces:
#     img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
    
# cv2.imshow("Frame",img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Face Detection Using Webcam
face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml") # Open Files CaCascadeClassifier
cap = cv2.VideoCapture(0) # Open Video Stream

while cap.isOpened():
    ret,frame = cap.read()
    
    if ret :
        
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #Convert To Gray Scale
        faces = face_cascade.detectMultiScale(gray,1.3,5)
        
        for (x,y,w,h) in faces :
            frame = draw_ped(frame,"Faces",x,y,x+w,y+h)
        
        cv2.imshow("Frame",frame) # Show Image
        
        if cv2.waitKey(1) == ord('q') :
            break
        
cap.release()
cv2.destroyAllWindows()
