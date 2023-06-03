import cv2
import mediapipe as mp
import numpy as np
from tensorflow import keras
from keras.models import load_model
from tkinter import *
from PIL import Image, ImageTk
import cv2
import threading
import customtkinter

customtkinter.set_appearance_mode("Dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

# load the model we saved
class Gesture(customtkinter.CTkToplevel):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("550x400")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.model = keras.models.load_model('model')
        self.cap = cv2.VideoCapture(0)
        self.mpHands = mp.solutions.hands
        self.low_green = np.array([60, 100, 72])
        self.high_green = np.array([102, 255, 255])
        self.hands = self.mpHands.Hands()
        self.image = None
        self.prediction = None
        self.time = 0
        self.string_pred = StringVar(value="No Gesture Detected")
        self.mpDraw = mp.solutions.drawing_utils
        self.vidLabel = customtkinter.CTkLabel(master = self, text="", anchor=CENTER, height=300, width=350, fg_color = "transparent")  
        self.vidLabel.grid(row=0, column=0, sticky="ew")
        self.text_pred = customtkinter.CTkEntry(master = self, textvariable=self.string_pred, width=50, fg_color = "transparent")
        self.text_pred.grid(row=1, column=0, sticky="ew")
        videoThread = threading.Thread(target=self.videoCap, args=())
        videoThread.start()

    def videoCap(self):
        while True:
            ret, image = self.cap.read()
            imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = self.hands.process(imageRGB)
            if results.multi_hand_landmarks:
                for handLms in results.multi_hand_landmarks: # working with each hand
                    for id, lm in enumerate(handLms.landmark):
                        h, w, c = image.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                    self.mpDraw.draw_landmarks(imageRGB, handLms, self.mpHands.HAND_CONNECTIONS, 
                                        self.mpDraw.DrawingSpec(color = (0, 255, 0), thickness = 8, circle_radius = 2),
                                        self.mpDraw.DrawingSpec(color = (0, 255, 0), thickness = 8, circle_radius = 2))
            self.image = imageRGB
            image = cv2.resize(imageRGB, (350,200))
            image = Image.fromarray(self.image)
            image = ImageTk.PhotoImage(image)
            self.vidLabel.configure(text="",image=image)
            self.vidLabel.image = image
            threading.Thread(target=self.predict, args=()).start()
            if self.time == 50:
                self.time = 0
                self.text_pred.delete(0, END)
                if self.prediction == 0:
                    self.text_pred.insert(0, "Gesture 1")
                elif self.prediction == 1:
                    self.text_pred.insert(0, "Gesture 2")
                elif self.prediction == 2:
                    self.text_pred.insert(0, "Gesture 3")
                elif self.prediction == 3:
                    self.text_pred.insert(0, "Gesture 4")
                elif self.prediction == 4:
                    self.text_pred.insert(0, "Gesture 5")
                elif self.prediction == None:
                    self.text_pred.insert(0, "No Gesture Detected")

    def predict(self):
        self.time += 1
        HSV  = cv2.cvtColor(self.image,cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(HSV, self.low_green, self.high_green) 
        res = cv2.bitwise_and(self.image, self.image, mask=mask)
        image_compile = cv2.resize(res, (25,25))
        image_compile = np.reshape(image_compile,[1,25,25,3])
        image_compile = image_compile*1./255.0
        self.prediction = self.model.predict(image_compile)
        self.prediction = np.argmax(np.array(self.prediction*100, dtype = 'int'))



