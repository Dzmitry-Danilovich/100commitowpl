import webbrowser
import panel_url
import scraping
import open_application
import programming_mode

def check(text):
    if "close" in text:
        raise KeyboardInterrupt
    elif "GitHub" in text:
         return webbrowser.open('https://github.com/Dzmitry-Danilovich')
    elif "YouTube" in text:
        return webbrowser.open('https://www.youtube.com')
    elif "scrapping" in text:
        scraping.get_html_content( panel_url.enter_url())
    elif "Telegram" in text:
        return open_application.AplicationOpen("Telegram Lite").launch()
    elif "Discord" in text:
        return open_application.AplicationOpen("Discord").launch()
    elif "start programming mode" in text:
        return programming_mode.programming_mode()
    else:
        return f"Nie raspoznany tekst: {text}"
