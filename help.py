import tkinter as tk
import speech_recognition as sr
from tkinter import messagebox as mb


def shortcuts():
    # Notification of all of the shortcuts
    mb.showinfo("Notification", 
                 "Ctrl + N -> New File"
                 "\nCtrl + O -> Open File"
                 "\nCtrl + W -> Open New Window"
                 "\nCtrl + S -> Save File"
                 "\nCtrl + P -> Speech to Text"
                 "\nCtrl + Q -> Toggle Theme"
                 "\nCtrl + = -> Zoom In"
                 "\nCtrl + - -> Zoom Out")


def speech_to_text(text):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        # Notification to alert the user
        mb.showinfo("Notification", "Speak now after closing the notification... With a pause you can stop the Speech to Text")
        audio = recognizer.listen(source)

        try:
            # Notification to alert the user
            mb.showinfo("Notification", "Translating your speech to text")
            recognized_text = recognizer.recognize_google(audio)
            text.insert(tk.END, recognized_text)
        except sr.UnknownValueError:
            # Error message if the Speech Recognition couldn't understand the users speech/audio
            mb.showerror("Error", "Speech Recognition could not understand audio")
            return
        except sr.RequestError as e:
            # Error message if the request isn't handled by the server
            mb.showerror("Error", f"Could not request results from Speech Recognition service; {e}")