import cv2
import numpy as np

def main():
    degisim = cv2.VideoCapture(0)
    while True:
        goruntuvar, bolum = degisim.read()

        yeni = cv2.cvtColor(bolum, cv2.COLOR_BGR2HSV)

        zemink = np.array([0, 100, 100])
        üstk = np.array([10, 255, 255])

        maskeleme = cv2.inRange(yeni, zemink, üstk)

        
        sonuc = cv2.bitwise_and(bolum, bolum, mask=maskeleme)

        
        cv2.imshow('Original', bolum) 
        cv2.imshow('Result', sonuc)

        
        if cv2.waitKey(1) & 0xFF == ord('Q'):
            break

    
    degisim.release()
    cv2.destroyAllWindows()

if __name__ == "_main_":
    main()
