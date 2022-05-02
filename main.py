from vosk import Model,KaldiRecognizer
import speech_recognition
import pyttsx3
import wave
import json
import os

class VoiceAssitant:
    name=""
    sexe=""
    speech_language=""
    recognitionlanguage=""

def setup_assistant_voice():
    voices=ttsEngine.getProperty('voices')[26]
    if assistant.speech_language=='fr':
        ttsEngine.setProperty("voice",voices.id)



if __name__=="__main__":
    recognizer=speech_recognition.Recognizer()
    microphone=speech_recognition.Microphone()

    ttsEngine=pyttsx3.init()

    assistant=VoiceAssitant()
    assistant.name="Prince"
    assistant.sexe="Male"
    assistant.speech_language="fr"

    setup_assistant_voice()

    while True:
        pass

