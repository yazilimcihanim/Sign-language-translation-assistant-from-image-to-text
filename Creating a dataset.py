import os
import cv2

DATA_DIR="./data"  #dosya yolu

if not os.path.exists(DATA_DIR):# data dosyası yoksa oluşturulur.
    os.makedirs(DATA_DIR)
    
number_of_class=29  # sınıf sayısı
data_size=150  # her sınıftaki görüntü sayısı 

cap=cv2.VideoCapture(0)
for j in range(number_of_class):
    if not os.path.exists(os.path.join(DATA_DIR,str(j))): #DATA_DIR içine sınıf sayısı kadar klasör oluşturur
        os.makedirs(os.path.join(DATA_DIR,str(j)))
        
    print("data sınıfları {}".format(j))
    
    while True:
        _,frame=cap.read() #cap.read() ile bir video çerçevesi okunur,cv2.putText fonksiyonuyla ekrana "hazır olunca q bas" şeklinde bir metin eklenir. 
        cv2.putText(frame,"hazir olunca q bas",(100,50),cv2.FONT_HERSHEY_SIMPLEX,1.3,(0,0,255),3)
        
        cv2.imshow("frame",frame)
        if cv2.waitKey(25) & 0xFF==ord("q"):
            break
        
    counter=0
    
    while counter<data_size:
        _,frame=cap.read()
        cv2.imshow("frame",frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR,str(j),"{}.jpg".format(counter)),frame)
        
        counter+=1
        
cap.release()
cv2.destroyAllWindows()
        
