from AppOpener import open, close
import speech_recognition as sr
import mouse
import keyboard

r = sr.Recognizer()

with sr.Microphone() as source:

    print('say')

    r.pause_threshold = 0.8

    r.adjust_for_ambient_noise(source, duration=1)

    audio = r.listen(source)

text = r.recognize_google(audio, language='ru-RU').lower()

print('you say:', text)
# text = text.split(' ')
# text = str(text)
if text.find('включи') != -1:
    text = text.split(' ')
    print(text[text.index("включи") + 1])
    open(f'{text[text.index("включи") + 1]}')


elif text.find('пиши') != -1:
    print(text.find('пиши'))
    message = text[text.find('пиши')+5:].capitalize()
    print(message)
    pass

elif text.find('закрой') != -1:
    text = text.split(' ')
    print(text[text.index("закрой") + 1])
    close(f'{text[text.index("закрой") + 1]}')
    # keyboard.press('Alt+F4')
# print(type(str(text)))