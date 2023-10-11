import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id) # 0 for male, 1 for female
        
def say(output):
    print(output)
    engine.say(output)
    engine.runAndWait()
