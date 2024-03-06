#program powienien otwierać aplikacji i foldery

import subprocess

def run_application(application_path, arguments=[]):
    try:
        subprocess.run([application_path] + arguments)
    except Exception as e:
        print(f"Błąd podczas uruchamiania aplikacji: {e}")

