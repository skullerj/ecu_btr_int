
import cv2
import numpy as np
import requests
import json
import base64
from subprocess import call
import time

class ServoMove():
	position = 400
	def __init__(self):
		call(['gpio','mode','33','pwm'])	
		call(['gpio','pwm','33','300'])
		time.sleep(1)
		call(['gpio','pwm','33','500'])
		time.sleep(1)
		self.position=400
		call(['gpio','pwm','33','400'])
	
	
	def center(self):
		self.position=400
		call(['gpio','pwm','33','400'])
		
	def accept(self):	
		self.position=530
		call(['gpio','pwm','33','530'])
		time.sleep(1)
		self.center()
		
	def reject(self):
		self.position=300
		call(['gpio','pwm','33','300'])
		time.sleep(1)
		self.center()



class CameraCapture():

    camera = None
    ramp_frames = 10
    def openCamera(self):
        self.camera = cv2.VideoCapture(0)

    def closeCamera(self):
        self.camera.release()

    def getImage(self):
        retval, im = self.camera.read()
        return im

    def captureImage(self):

        for i in range(self.ramp_frames):
            temp = self.getImage()
        camera_capture = self.getImage()
        print camera_capture.shape
        crop_img = camera_capture[20:360, 0:680]
        resized = cv2.resize(crop_img, (200, 100))
        return resized 

def request_validation(identifier):
    capture= CameraCapture()
    capture.openCamera()
    image_payload=capture.captureImage()
    capture.closeCamera()
    payload=base64.b64encode(image_payload.ravel().tostring())
    data = {'data':payload.decode(),'id':identifier}
    r = requests.post('http://35.203.169.198/predict',json=data)
    if(r.json()['valid']=='True'):
		return True,float(r.json()['value'])
    else:
		return False,0

