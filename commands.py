import webbrowser
import panel_url
import scraping

def check(text):
    if "close" in text:
        raise KeyboardInterrupt
    elif "GitHub" in text:
         return webbrowser.open('https://github.com/Dzmitry-Danilovich')
    elif "YouTube" in text:
        return webbrowser.open('https://www.youtube.com')
    elif "scrapping" in text:
        scraping.get_html_content( panel_url.enter_url())
    else:
        return f"Nie raspoznany tekst: {text}"