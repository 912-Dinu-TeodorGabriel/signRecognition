
from tkinter import *
import customtkinter
from ImageCollector import ImageCollector
from Gesture import Gesture
from functools import partial
import os
import shutil
from ModelCreator import modelCreate


customtkinter.set_appearance_mode("Dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x300")
        self.DATA_DIR = "./data/"
        self.checkbox_slider_frame = customtkinter.CTkFrame(self)
        self.checkbox_slider_frame.grid(row=6, column=3, sticky="nsew")
        self.checkbox_1 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text=" Gesture 1 ", command=partial(self.open_imagecollector, 0))
        self.checkbox_1.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="n")
        if os.path.exists(self.DATA_DIR) and os.path.exists(self.DATA_DIR + "0"):
            self.checkbox_1.configure(state="disabled")
            self.text1 = customtkinter.CTkLabel(master=self.checkbox_slider_frame, text=" Gesture 1 already created ", fg_color="green")
            self.text1.grid(row=1, column=1, pady=(20, 0), padx=20, sticky="n")
        
        self.reset1 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="Reset", command=partial(self.reset, 0))
        self.reset1.grid(row=1, column=2, pady=(20, 0), padx=20, sticky="n")

        self.checkbox_2 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text=" Gesture 2 ", command=partial(self.open_imagecollector, 1))
        self.checkbox_2.grid(row=2, column=0, pady=(20, 0), padx=20, sticky="n", )
        if os.path.exists(self.DATA_DIR) and os.path.exists(self.DATA_DIR + "1"):
            self.checkbox_2.configure(state="disabled")
            self.text2 = customtkinter.CTkLabel(master=self.checkbox_slider_frame, text=" Gesture 2 already created ", fg_color="green")
            self.text2.grid(row=2, column=1, pady=(20, 0), padx=20, sticky="n")
        
        self.reset2 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="Reset", command=partial(self.reset, 1))
        self.reset2.grid(row=2, column=2, pady=(20, 0), padx=20, sticky="n")

        self.checkbox_3 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text=" Gesture 3 ", command=partial(self.open_imagecollector, 2))
        self.checkbox_3.grid(row=3, column=0, pady=(20,0), padx=20, sticky="n")
        if os.path.exists(self.DATA_DIR) and os.path.exists(self.DATA_DIR + "2"):
            self.checkbox_3.configure(state="disabled")
            self.text3 = customtkinter.CTkLabel(master=self.checkbox_slider_frame, text=" Gesture 3 already created ", fg_color="green")
            self.text3.grid(row=3, column=1, pady=(20, 0), padx=20, sticky="n")

        self.reset3 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="Reset", command=partial(self.reset, 2))
        self.reset3.grid(row=3, column=2, pady=(20, 0), padx=20, sticky="n")

        self.checkbox_4 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text=" Gesture 4 ", command=partial(self.open_imagecollector, 3))
        self.checkbox_4.grid(row=4, column=0, pady=(20,0), padx=20, sticky="n")
        if os.path.exists(self.DATA_DIR) and os.path.exists(self.DATA_DIR + "3"):
            self.checkbox_4.configure(state="disabled")
            self.text4 = customtkinter.CTkLabel(master=self.checkbox_slider_frame, text=" Gesture 4 already created ", fg_color="green")
            self.text4.grid(row=4, column=1, pady=(20, 0), padx=20, sticky="n")
        
        self.reset4 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="Reset", command=partial(self.reset, 3))
        self.reset4.grid(row=4, column=2, pady=(20, 0), padx=20, sticky="n")

        self.checkbox_5 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text=" Gesture 5 ", command=partial(self.open_imagecollector, 4))
        self.checkbox_5.grid(row=5, column=0, pady=(20,0), padx=20, sticky="n")
        if os.path.exists(self.DATA_DIR) and os.path.exists(self.DATA_DIR + "4"):
            self.checkbox_5.configure(state="disabled")
            self.text5 = customtkinter.CTkLabel(master=self.checkbox_slider_frame, text=" Gesture 5 already created ", fg_color="green")
            self.text5.grid(row=5, column=1, pady=(20, 0), padx=20, sticky="n")
        
        self.reset5 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="Reset", command=partial(self.reset, 4))
        self.reset5.grid(row=5, column=2, pady=(20, 0), padx=20, sticky="n")

        self.checkbox_6 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text=" Recognition ", command=self.open_gesture_recognition)
        self.checkbox_6.grid(row=6, column=0, pady=(20,0), padx=20, sticky="n")
        if not os.path.exists(self.DATA_DIR) or len(os.listdir(self.DATA_DIR)) < 5:
            self.checkbox_6.configure(state="disabled")
            self.text6 = customtkinter.CTkLabel(master=self.checkbox_slider_frame, text=" Not enough data to train ", fg_color="red")
            self.text6.grid(row=6, column=1, pady=(20, 0), padx=20, sticky="n")
        elif len(os.listdir(self.DATA_DIR)) == 5 and not os.path.exists("./model"):
                self.text6 = customtkinter.CTkLabel(master=self.checkbox_slider_frame, text=" Ready to train ", fg_color="green")
                self.text6.grid(row=6, column=1, pady=(20, 0), padx=20, sticky="n")
        elif os.path.exists("./model"):
            self.text6 = customtkinter.CTkLabel(master=self.checkbox_slider_frame, text=" Model trained ", fg_color="green")
            self.text6.grid(row=6, column=1, pady=(20, 0), padx=20, sticky="n")
        self.reset6 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="Reset", command=partial(self.reset, 5))
        self.reset6.grid(row=6, column=2, pady=(20, 0), padx=20, sticky="n")
        self.toplevel_window = None
        
    def open_imagecollector(self, gesture_number:int):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ImageCollector(self)
            self.toplevel_window.setGestureNumber(gesture_number)
            #to disable the checkbox
            if gesture_number == 0:
                self.checkbox_1.configure(state="disabled")
                self.text1 = customtkinter.CTkLabel(master=self.checkbox_slider_frame, text="Gesture 1 already created", fg_color="green")
                self.text1.grid(row=1, column=1, pady=(20, 0), padx=20, sticky="n")
                self.reset1 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="Reset", command=partial(self.reset, 0))
                self.reset1.grid(row=1, column=2, pady=(20, 0), padx=20, sticky="n")
            elif gesture_number == 1:
                self.checkbox_2.configure(state="disabled")
                self.text2 = customtkinter.CTkLabel(master=self.checkbox_slider_frame, text="Gesture 2 already created", fg_color="green")
                self.text2.grid(row=2, column=1, pady=(20, 0), padx=20, sticky="n")
                self.reset2 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="Reset", command=partial(self.reset, 1))
                self.reset2.grid(row=2, column=2, pady=(20, 0), padx=20, sticky="n")

            elif gesture_number == 2:
                self.checkbox_3.configure(state="disabled")
                self.text3 = customtkinter.CTkLabel(master=self.checkbox_slider_frame, text="Gesture 3 already created", fg_color="green")
                self.text3.grid(row=3, column=1, pady=(20, 0), padx=20, sticky="n")
                self.reset3 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="Reset", command=partial(self.reset, 2))
                self.reset3.grid(row=3, column=2, pady=(20, 0), padx=20, sticky="n")

            elif gesture_number == 3:
                self.checkbox_4.configure(state="disabled")
                self.text4 = customtkinter.CTkLabel(master=self.checkbox_slider_frame, text="Gesture 4 already created", fg_color="green")
                self.text4.grid(row=4, column=1, pady=(20, 0), padx=20, sticky="n")
                self.reset4 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="Reset", command=partial(self.reset, 3))
                self.reset4.grid(row=4, column=2, pady=(20, 0), padx=20, sticky="n")

            elif gesture_number == 4:
                self.checkbox_5.configure(state="disabled")
                self.text5 = customtkinter.CTkLabel(master=self.checkbox_slider_frame, text="Gesture 5 already created", fg_color="green")
                self.text5.grid(row=5, column=1, pady=(20, 0), padx=20, sticky="n")
                self.reset5 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="Reset", command=partial(self.reset, 4))
                self.reset5.grid(row=5, column=2, pady=(20, 0), padx=20, sticky="n")

            if len(os.listdir(self.DATA_DIR)) == 5:
                self.checkbox_6.configure(state="normal")
                self.text6.destroy()
                self.text6 = customtkinter.CTkLabel(master=self.checkbox_slider_frame, text=" Ready to train ", fg_color="green")
                self.text6.grid(row=6, column=1, pady=(20, 0), padx=20, sticky="n")

    def open_gesture_recognition(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            #if the dir model is in the file
            if not os.path.isdir("./model"):
                self.createModel()
            self.toplevel_window = Gesture(self)
    def createModel(self):
        #destroy all the widgets
        self.checkbox_slider_frame.destroy()
        #Please wait text
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.text7 = customtkinter.CTkLabel(master=self.slider_progressbar_frame, text="Please wait...", font = ("Helvetica", 20))
        self.text7.grid(row=0, column=1, pady=(20, 0), padx=20, sticky="n")
        self.seg_button_1 = customtkinter.CTkSegmentedButton(self.slider_progressbar_frame)
        self.seg_button_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_1.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        modelCreate()


    def reset(self, gesture_number:int):
        if os.path.exists(self.DATA_DIR) and os.path.exists(self.DATA_DIR + str(gesture_number)):
            shutil.rmtree(self.DATA_DIR + str(gesture_number))
        if os.path.exists("./model"):
            shutil.rmtree("./model")
        if gesture_number == 0:
            self.checkbox_1.configure(state="normal")
            self.text1.destroy()
        elif gesture_number == 1:
            self.checkbox_2.configure(state="normal")
            self.text2.destroy()
        elif gesture_number == 2:
            self.checkbox_3.configure(state="normal")
            self.text3.destroy()
        elif gesture_number == 3:
            self.checkbox_4.configure(state="normal")
            self.text4.destroy()
        elif gesture_number == 4:
            self.checkbox_5.configure(state="normal")
            self.text5.destroy()
        if len(os.listdir(self.DATA_DIR)) < 5:
            self.checkbox_6.configure(state="disabled")
            self.text6.destroy()
            self.text6 = customtkinter.CTkLabel(master=self.checkbox_slider_frame, text=" Not enough data to train ", fg_color="red")
            self.text6.grid(row=6, column=1, pady=(20, 0), padx=20, sticky="n")
        elif len(os.listdir(self.DATA_DIR)) == 5:
            self.checkbox_6.configure(state="normal")
            self.text6.destroy()
            self.text6 = customtkinter.CTkLabel(master=self.checkbox_slider_frame, text=" Ready to train ", fg_color="green")
            self.text6.grid(row=6, column=1, pady=(20, 0), padx=20, sticky="n")

app = App()
app.mainloop() 
