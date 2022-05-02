from vosk import Model,KaldiRecognizer
import speech_recognition
import wave
import json
import os

class VoiceAssitant:
    name=""
    sexe=""
    speech_language=""
    recognitionlanguage=""