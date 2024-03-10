import subprocess
import mouse_controle

class AplicationOpen:
    def __init__(self, app_name):
        self.app_name = app_name
    def launch(self):
        try:
            subprocess.run(['open', '-a', self.app_name])
            if self.app_name == "Notes":
                mouse_controle.add_notes()

        except Exception as e:
            print(f"Błąd: {e}")
