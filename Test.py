def xcopyx(source, destination):

    os.system(f'cmd /k "xcopy {source} {destination} /s /y /e /x /v /k /I"')

import os
import subprocess
import time

source      = "H:\Projects\SafeTranferData\Data\Fol_1"
destination = "H:\Projects\SafeTranferData\Data\Fol_2"

#"H:\Projects\SafeTranferData\Data\Fol_1\AAAFolder - Copy\12 - Copy.bmp"
#sourceFile = "H:\Projects\SafeTranferData\Data\Fol_1\AAAFolder - Copy\\12 - Copy.bmp"

sourceFile = "H:\Projects\SafeTranferData\Data\Fol_1\\backAl.py"
destFile   = "H:\Projects\SafeTranferData\Data\Fol_2\\"


def xcopyFolder(source, destination):

    os.system(f'cmd /k "xcopy {source} {destination} /s /y /e /x /v /k /I"')
    print("done")




def xcopyFile(source, destination):
    print("Source:", source )
    print("destination:", destination)
    os.system(f'"xcopy {source} {destination}  /y /o /k "')  
    
  
i=100

while i>0 :

    i-=1
    print("I:", i)
    xcopyFile(sourceFile, destFile)
    time.sleep(3)
    



    