#  tmpFile.write('$driveEject = New-Object -comObject Shell.Application\n')
#             tmpFile.write('$driveEject.Namespace(17).ParseName("'+disk+':").InvokeVerb("Eject")')

import os

import string
# os.system("'$driveEject = New-Object -comObject Shell.Application\n'")
# os.system("'$driveEject.Namespace(17).ParseName("'D:'").InvokeVerb('Eject')'")


# os.system('powershell $driveEject = New-Object -comObject Shell.Application;')
# os.system('powershell Get-WmiObject -Class Win32_LogicalDisk >> %APPDATA%/t.txt')


# print(f'{%APPDATA%/t.txt}')
# with open('%APPDATA%/t.txt') as f :
#     lines = f.readlines()



import subprocess
# output = subprocess.check_output("powershell Get-WmiObject -Class Win32_LogicalDisk", shell=True)


# m = (output.decode())
# mm = m.splitlines()
# #print(mm[2])

# for i in mm :
#     if i[0:8] == "DeviceID"  :
       
#         ID = i[15:]
#         print(ID)

#     if i[0:10] == "VolumeName" :
#         VN = i[15:]
#         print(VN)






def findUsbLetter(usbName):

    DeviceID   = []
    VolumeName = []

    output = subprocess.check_output("powershell Get-WmiObject -Class Win32_LogicalDisk", shell=True)
    
    m = (output.decode())
    mm = m.splitlines()

    for i in mm :
      if i[0:8] == "DeviceID"  :
        
            ID = i[15:]
            DeviceID.append(ID)
            
      if i[0:10] == "VolumeName" :
            VN = i[15:]
            if VN == '' :
                    
                    VolumeName.append("None")
            else:

                    VolumeName.append(VN)
                

    for index , volumeN in enumerate(VolumeName) :
       
        if volumeN.lower() == str(usbName.lower()) :
           return DeviceID[index]

    return "None"

    


print(findUsbLetter("projects"))

