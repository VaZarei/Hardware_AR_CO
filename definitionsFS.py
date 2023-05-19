from copyFS import *
from arduinoFS import *
from timeFS import *
from definitionsFS import *

"""

   Definition all about Variable


"""



# ---------------  Controller  -------------------

inputMinuteInterval = 1   # max = 1440 m
comPort = 'COM4'


# -----------------  Time  -----------------------




# -----------------  Copy  -----------------------


flashUsbName       =  "forTransfer"


source            = "H:\Projects\SafeTranferData\Data\Fol_1"
clientDestination = "H:\Projects\SafeTranferData\Data\Fol_2"
adminDestination  = "H:\Projects\SafeTranferData\Data\Admin"


allowExtentions       = ["jpg", "txt", "pdf", "rar", "bmp", "accdb"]
incpectionExtentions  = ["exe", "py", "mp4", "ini"]
forbiddenExtentions   = ["mp3", "py"]


adminAllowPath       =  f"{adminDestination}\\AllowPathAdmin\\"  
adminInspectionPath  =  f"{adminDestination}\\InspectionPath\\"             # for Admin, Need to Inspection Then Send ...
adminforbiddenPath   =  f"{adminDestination}\\ForbiddenPath\\"              # for Admin, Forbiden To transfer
adminAll             =  f"{adminDestination}\\All\\"                        # for Admin, main Source to destinations appending ...


