from AppOpener import open, close
import speech_recognition as sr
import mouse
import keyboard

def Open_or_close(text, mod):
    text = text.split(' ')
    if mod:
        open(f'{text[text.index("включи") + 1]}')
    else:
        close(f'{text[text.index("закрой") + 1]}')
    pass
def Write_text(text):
    message = text[text.find('пиши') + 5:].capitalize()
    return

def Julia_brain(text):
    if text.find('юля') != -1 or text.find('julia'):
        if text.find('включи') != -1:
            Open_or_close(text, True)
        elif text.find('закрой') != -1:
            Open_or_close(text, False)

        elif text.find('пиши') != -1:
            Write_text(text)

def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('say')
        r.pause_threshold = 0.8
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    text = r.recognize_google(audio, language='ru-RU').lower()
    print('you say:', text)
    Julia_brain(text)

if __name__ == 'main':
    main()

