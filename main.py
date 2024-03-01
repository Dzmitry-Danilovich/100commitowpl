import speech_recognition as sr

recognizer = sr.Recognizer()
def rozpoznaj_mowe():
    with sr.Microphone() as source:
        print("Proszę mówić...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="en-US")
        print("Rozpoznano: " + text)
    except sr.UnknownValueError:
        print("Nie rozpoznano mowy")
    except sr.RequestError as e:
        print("Błąd serwera; {0}".format(e))

while True:
    rozpoznaj_mowe()
