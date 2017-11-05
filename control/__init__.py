
import cv2
import numpy as np
import requests
import json
import base64

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
        crop_img = camera_capture[100:900, 220:1920]
        resized = cv2.resize(crop_img, (200, 100))
        return resized
cd 

def request_validation(identifier):
    capture= CameraCapture()
    capture.openCamera()
    image_payload=capture.captureImage()
    capture.closeCamera()
    payload=base64.b64encode(image_payload.ravel().tostring())
    data = {'data':payload.decode(),'id':identifier}
    r = requests.post('https://thawing-oasis-25126/predict',json=data)
    return True,float(r.json()['value']);
