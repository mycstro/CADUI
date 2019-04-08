import ctypes
import os
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ROOT_DIR = os.path.join(BASE_DIR, 'cadui_mem')

cmd = os.path.join(ROOT_DIR, 'memcached -d stop')


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    subprocess.run(cmd)
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

print(cmd)
