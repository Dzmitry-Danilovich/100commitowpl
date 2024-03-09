import subprocess

class AplicationOpen:
    def __init__(self, app_name):
        self.app_name = app_name
    def launch(self):
        try:
            subprocess.run(['open', '-a', self.app_name])
        except Exception as e:
            print(f"Błąd: {e}")
