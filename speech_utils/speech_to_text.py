import openai
import speech_recognition as sr
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

r = sr.Recognizer()
mic = sr.Microphone(device_index=0)
r.dynamic_energy_threshold = False
r.energy_threshold = 400

def transcribe_speech(audio):
    file_path = os.path.join(os.path.dirname(__file__), "speech.wav")
    with open(file_path, "wb") as f:
        f.write(audio.get_wav_data())
    speech = open(file_path, "rb")
    completion = openai.Audio.transcribe(
        model = "whisper-1",
        file = speech
    )
    user_input = completion["text"]
    return user_input

def listen():
    with mic as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration = 0.5)
        audio = r.listen(source)
        try:
            result = transcribe_speech(audio)
            print(result)
            return result
        except:
            exit("Sorry, something went wrong!")
