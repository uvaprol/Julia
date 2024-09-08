from AppOpener import open
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:

    print('say')

    r.pause_threshold = 0.8

    r.adjust_for_ambient_noise(source, duration=1)

    audio = r.listen(source)

text = r.recognize_google(audio, language='ru-RU').lower()

print('you say:', text)
text = text.split(' ')
if text.index('включи') != -1:
    print(text[text.index("включи") + 1])
    open(f'{text[text.index("включи") + 1]}')

