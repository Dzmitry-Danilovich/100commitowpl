import requests

def get_html_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            try:
                with open("work_with_folder", "w") as file:
                    file.write(response.text)
            except Exception as e:
                print(f"Błąd {e}")
        else:
            print(f"Nie działą {response.status_code}")
            return None
    except Exception as e:
        print(f"Bład podczas pobierania zawortości strony {e}")
        return None

