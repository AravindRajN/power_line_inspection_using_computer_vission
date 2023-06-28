import os
try:
    os.system("pip install opencv-python")
    os.system("pip install PyAudio")
    os.system("pip install pyttsx3")
    os.system("pip install numpy")
    print("success")
except:
    print("not install property")
