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
    voices=ttsEngine.getProperty('voices')
    if assistant.speech_language=='fr':
        ttsEngine.setProperty("voice","french")
        ttsEngine.setProperty("rate", 100)

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
            pass
        except speech_recognition.RequestError:
            print("Essaie de la reconnaissance hors ligne")
            recognized_data=use_offline_recognition()

        return recognized_data

def use_offline_recognition():
    recognized_data=''
    if not os.path.exists("models/vosk-model-small-fr-0.22"):
        print("Veuillez télécharger un model")
        exit(1)
    else:
        wave_audio_file=wave.open("microphone-results.wav","rb")
        model=Model("models/vosk-model-small-fr-0.22")
        offline_recognizer=KaldiRecognizer(model,wave_audio_file.getframerate())
        data=wave_audio_file.readframes(wave_audio_file.getnframes())
        if len(data)>0:
            if offline_recognizer.AcceptWaveform(data):
                recognized_data=offline_recognizer.Result()
        recognized_data=json.loads(recognized_data)
        recognized_data=recognized_data['text']

    return recognized_data



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
        #os.remove("microphone-results.wav")
        print(voice_input)




        play_voice_assistant_sppech(voice_input)

