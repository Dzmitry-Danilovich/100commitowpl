import subprocess
import webbrowser
import time

def programming_mode():
    try:
        subprocess.run(['open', '-a', 'Safari'])
        webbrowser.open('https://www.youtube.com/watch?v=wu9stvpFU1M')
        time.sleep(5)
        subprocess.run(['open', '-a', 'PyCharm CE'])
    except Exception as e:
        print(f'Error in: {e}')