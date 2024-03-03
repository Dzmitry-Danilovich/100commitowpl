import webbrowser

def check(text):
    if "close" in text:
        raise KeyboardInterrupt

    elif "GitHub" in text:
         return webbrowser.open('https://github.com/Dzmitry-Danilovich')

    elif "YouTube" in text:
        return webbrowser.open('https://www.youtube.com')
