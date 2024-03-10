import pyautogui
import speech_recognition as sr
recognizer = sr.Recognizer()
def add_notes():
    with sr.Microphone() as source:
        print("Co trzeba dodać?")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="en-US")

    except sr.UnknownValueError:
        print("Nie")
    except sr.RequestError as e:
        print("Błąd serwera; {0}".format(e))

    pyautogui.click(536, 53)

    pyautogui.typewrite(text)
