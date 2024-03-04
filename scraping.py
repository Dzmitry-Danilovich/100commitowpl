import requests

def get_html_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Nie działą {response.status_code}")
            return None
    except Exception as e:
        print(f"Bład podczas pobierania zawortości strony {e}")
        return None

url_to_fetch = "https://www.example.com"
html_content = get_html_content(url_to_fetch)

if html_content:
    print(html_content)
