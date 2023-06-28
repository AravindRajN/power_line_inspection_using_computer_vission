
#{install all the following required pkg
#pip install opencv-python
#pip install PyAudio
#pip install pyttsx3
#pip install numpy}
## or ##
#{use run this python code pkginstaller.py}
import cv2
import pyttsx3
import numpy as np

def video(cap):
    while True:
        # Read a frame from the video
        ret, frame = cap.read()
        
        # If the frame was read correctly
        if ret:
            # Convert the frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Apply a Gaussian blur to reduce noise and avoid false detections
            blur = cv2.GaussianBlur(gray, (5, 5), 0)
            
            # Detect edges using the Canny edge detector
            edges = cv2.Canny(blur, 50, 250)
            
            # Define a region of interest (ROI) where power lines are likely to be present
            mask = np.zeros_like(edges)
            height, width = mask.shape
            roi = np.array([[(0, height), (0, height//2), (width, height//2), (width, height)]], dtype=np.int32)
            cv2.fillPoly(mask, roi, 255)
            masked_edges = cv2.bitwise_and(edges, mask)
            
            # Detect lines using the Hough transform
            lines = cv2.HoughLinesP(masked_edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=50)
            
            # Draw the detected lines on the original frame
            if lines is not None:
                for line in lines:
                    x1, y1, x2, y2 = line[0]
                    cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
            
            # Show the result
            cv2.imshow('Power Line Detection', frame)
            
            # Exit if the 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()
def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()
while True:
    speak("enter the type of input")
    a=int(input("enter the type of input\n 1.jpg \n 2.video\n select the no:"))
    if a==2:
        # Load the video
        speak("we are tracking the electrical line wire")
        cap = cv2.VideoCapture('power.mp4')
        video(cap)
    elif a==1:
        print("we developing this feature on future right now we build it for video only")
        speak("we developing this feature on future right now we build it for video only")
        cap = cv2.VideoCapture('power.mp4')
        video(cap)
    else:
        print("something went wrong")
        speak("something went wrong")
