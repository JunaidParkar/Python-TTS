import ctypes
import subprocess
import sys

def adm():
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("not an admin, restarting...")
        subprocess.run(["launcher.exe", sys.executable, *sys.argv])
    else:
        print("I'm an admin now.")