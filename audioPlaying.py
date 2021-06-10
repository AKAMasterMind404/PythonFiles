import speech_recognition as sr
from translate import Translator
from gtts import gTTS
from playsound import playsound

r = sr.Recognizer()

# with sr.Microphone() as source:
#     print("listening...")
#     r.adjust_for_ambient_noise(source)
#     voice = r.listen(source)
#     text = r.recognize_google(voice)
#     text = gTTS(text, lang="en")
#     print(text)

with sr.AudioFile("input.wav") as source:
    # audio = r.listen(source)
    audio = r.record(source, duration=30)
    print(source.DURATION)
    try:
        text = r.recognize_google(audio, language="ml",)
        print("WORKING ON...")
        print(text)
    except:
        print("Sorry")

translator = Translator(from_lang='ml', to_lang="en")
translation = translator.translate(text)
print(translation)
mal = gTTS(translation, lang="en")
mal.save("voice.mp3")
playsound("voice.mp3")
