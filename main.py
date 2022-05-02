import pyaudio
import vosk
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


def recognize(model: vosk.Model, phrase_wav_path: str) -> str:
    wave_audio_file = wave.open(phrase_wav_path, "rb")

    offline_recognizer = KaldiRecognizer(model, wave_audio_file.getframerate())

    offline_recognizer.SetWords(True)

    data = wave_audio_file.readframes(wave_audio_file.getnframes())

        # print(wave_audio_file.getcomptype())
        # print(wave_audio_file.getnchannels())
        # print(wave_audio_file.getframerate())

    offline_recognizer.AcceptWaveform(data)
    # recognized_data = json.loads(offline_recognizer.Result())
    recognized_data = offline_recognizer.Result()
    recognized_data=json.loads(recognized_data)
    recognized_data=recognized_data['text']

    return recognized_data if len(recognized_data)>0 else "Veuillez répéter"

def setup_assistant_voice():
    voices=ttsEngine.getProperty('voices')
    if assistant.speech_language=='fr':
        ttsEngine.setProperty("voice","french")


def play_voice_assistant_sppech(text_to_speech):
    ttsEngine.say(str(text_to_speech))
    ttsEngine.runAndWait()

def record_recognize_audio(*args:tuple):
    with microphone:
        recognized_data=""
        recognizer.adjust_for_ambient_noise(microphone,duration=2)
        try:
            print("A l'écoute ...")
            audio=recognizer.listen(microphone,5,5)
            with open("microphone-results.wav","wb") as file:

                file.write(audio.get_wav_data())
        except speech_recognition.WaitTimeoutError:
            print("Recommence")
            return

        try:
            print("Reconnaissance start..")
            recognized_data=recognizer.recognize_google(audio,language='fr')
        except speech_recognition.UnknownValueError:

            recognized_data ="Veuillez repétez "
        except speech_recognition.RequestError:
            print("Essaie de la reconnaissance hors ligne")
            recognized_data=use_offline_recognition()

        return recognized_data

def use_offline_recognition():
    recognizer_data=""

    model = Model("models/vosk-model-small-fr-0.22")
        # wavname = "/content/drive/MyDrive/Colab Notebooks/demo_Mono_S16_LE_44100.wav"
    wavname = "microphone-results.wav"

    out = recognize(model, wavname)

    recognizer_data=out
    print(recognizer_data)

    return recognizer_data





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
        voice_input=record_recognize_audio()

        print(voice_input)






        play_voice_assistant_sppech(voice_input)

