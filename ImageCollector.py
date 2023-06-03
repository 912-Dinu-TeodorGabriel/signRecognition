import os
import numpy as np
import mediapipe as mp
from tkinter import *
from PIL import Image, ImageTk
import cv2
import threading
import customtkinter

customtkinter.set_appearance_mode("Dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

class ImageCollector(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.DATA_DIR = "./data/"
        if not os.path.exists(self.DATA_DIR):
            os.makedirs(self.DATA_DIR)

        self.geometry("550x300")
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.cap = cv2.VideoCapture(0)
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils
        self.i = 0

        self.low_green = np.array([60, 100, 72])
        self.high_green = np.array([102, 255, 255])
        self.vidLabel = customtkinter.CTkLabel(self, text="", anchor=CENTER, height=300, width=350, fg_color = "transparent")  
        self.vidLabel.grid(row=0, column=0, sticky="ew")
        img = ImageTk.PhotoImage(Image.open("./images/handpose1-removebg-preview.png").resize((350, 300), Image.ANTIALIAS))
        self.handposeLabel = customtkinter.CTkLabel(self, text="", image=img, anchor=CENTER, height=300, width=350, fg_color = "transparent")
        self.handposeLabel.grid(row=0, column=1, sticky="ew")

        self.imageLandmarks = None
        videoThread = threading.Thread(target=self.video, args=())
        videoThread.start()

    def setGestureNumber(self, i):
        self.i = i
        if not os.path.exists(os.path.join(self.DATA_DIR, str(self.i))):
            os.makedirs(os.path.join(self.DATA_DIR, str(self.i)))
        
        

    def saveImage(self):
        count = len(os.listdir(os.path.join(self.DATA_DIR, str(self.i)))) + 1
        image = self.imageLandmarks
        image = cv2.resize(image, (25, 25))
        HSV  = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(HSV, self.low_green, self.high_green)
        res = cv2.bitwise_and(image, image, mask=mask)
        cv2.imwrite(os.path.join(self.DATA_DIR, str(self.i), str(count) + ".jpg"), res)
        if(len(os.listdir(os.path.join(self.DATA_DIR, str(self.i)))) == 50):
            self.handposeLabel.destroy()
            img = ImageTk.PhotoImage(Image.open("./images/handpose2-removebg-preview.png").resize((350, 300), Image.ANTIALIAS))
            self.handposeLabel = customtkinter.CTkLabel(self, text="", image=img, anchor=CENTER, height=300, width=350, fg_color = "transparent")
            self.handposeLabel.grid(row=0, column=1, sticky="ew")
        elif(len(os.listdir(os.path.join(self.DATA_DIR, str(self.i)))) == 90):
            self.handposeLabel.destroy()
            img = ImageTk.PhotoImage(Image.open("./images/handpose3-removebg-preview.png").resize((350, 300), Image.ANTIALIAS))
            self.handposeLabel = customtkinter.CTkLabel(self, text="", image=img, anchor=CENTER, height=300, width=350, fg_color = "transparent")
            self.handposeLabel.grid(row=0, column=1, sticky="ew") 
        elif(len(os.listdir(os.path.join(self.DATA_DIR, str(self.i)))) == 130):
            self.handposeLabel.destroy()
            img = ImageTk.PhotoImage(Image.open("./images/handpose4-removebg-preview.png").resize((350, 300), Image.ANTIALIAS))
            self.handposeLabel = customtkinter.CTkLabel(self, text="", image=img, anchor=CENTER, height=300, width=350, fg_color = "transparent")
            self.handposeLabel.grid(row=0, column=1, sticky="ew")    
        elif(len(os.listdir(os.path.join(self.DATA_DIR, str(self.i)))) == 160):
            self.handposeLabel.destroy()
            img = ImageTk.PhotoImage(Image.open("./images/handpose5-removebg-preview.png").resize((350, 300), Image.ANTIALIAS))
            self.handposeLabel = customtkinter.CTkLabel(self, text="", image=img, anchor=CENTER, height=300, width=350, fg_color = "transparent")
            self.handposeLabel.grid(row=0, column=1, sticky="ew")  
        elif(len(os.listdir(os.path.join(self.DATA_DIR, str(self.i)))) == 200):
            self.handposeLabel.destroy()
            img = ImageTk.PhotoImage(Image.open("./images/handpose6-removebg-preview.png").resize((350, 300), Image.ANTIALIAS))
            self.handposeLabel = customtkinter.CTkLabel(self, text="", image=img, anchor=CENTER, height=300, width=350, fg_color = "transparent")
            self.handposeLabel.grid(row=0, column=1, sticky="ew")        

    def video(self):
        while True:
            ret, image = self.cap.read()
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = self.hands.process(image)
            if results.multi_hand_landmarks:
                for handLms in results.multi_hand_landmarks: # working with each hand
                    for id, lm in enumerate(handLms.landmark):
                        h, w, c = image.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                self.mpDraw.draw_landmarks(image, handLms, self.mpHands.HAND_CONNECTIONS, 
                                        self.mpDraw.DrawingSpec(color = (0, 255, 0), thickness = 10, circle_radius = 2),
                                        self.mpDraw.DrawingSpec(color = (0, 255, 0), thickness = 10, circle_radius = 2))
            self.imageLandmarks = image
            if(results.multi_hand_landmarks and len(os.listdir(os.path.join(self.DATA_DIR, str(self.i)))) < 200):
                self.saveImage()
            image = cv2.resize(image, (370,300))
            image = Image.fromarray(image)
            image = ImageTk.PhotoImage(image)
            self.vidLabel.configure(text="",image=image)
            self.vidLabel.image = image

