


# os.system(f'"cmd.exe /c xcopy "{source}" "{destination}" /s /d /y /e /x /v /k /I "')    #/s /d /y /e /x /v /k /I

import os

def xcopyFile(source, destination):
    
        os.system(f'"cmd.exe /c xcopy "{source}" "{destination}" /I "')    #/s /d /y /e /x /v /k /I


PC1 = "H:\Projects\SafeTranferData\Data\PC1"
flash  = "H:\Projects\SafeTranferData\Data\Flash"
PC2 = "H:\Projects\SafeTranferData\Data\PC2"


for root, dirs, files in os.walk(PC1) :

    

    break

for i in range(len(dirs)) :
    print(root +"\\"+ dirs[i])

    source = root

    xcopyFile(source, flash)

    




