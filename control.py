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
        print("Taking image...")
        camera_capture = self.getImage()
        crop_img = camera_capture[100:900, 220:1920]
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
        return True,float(r.json()['value']);
    else:
        return False,0
