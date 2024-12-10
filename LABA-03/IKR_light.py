from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (2400, 1500)
camera.start_preview()
sleep(2)
camera.capture('/home/b03-404/Desktop/Scripts/red2.png')
