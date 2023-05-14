

# xcopy C:\Users\lan-27600\Desktop\source\arduinoSide.py C:\Users\lan-27600\Desktop\destination /s /y /e /x /v /k
import subprocess
import os
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False




if is_admin():
# Code of your program here
    print(" is admin ")
    os.system('cmd /k "H:\Projects\SafeTranferData\\batchT1.bat"')
    pass
else:
# Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)