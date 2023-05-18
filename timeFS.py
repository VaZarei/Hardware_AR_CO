from copyFS import *
from arduinoFS import *
from timeFS import *
from definitionsFS import *

from datetime import datetime

def findNextTime(inputMinuteInterval) :

        timeNow = str(datetime.now().strftime("%H:%M:%S %p"))
        # print(timeNow)
    
        h = int(timeNow[0:2])
        m = int(timeNow[3:5])
        s = int(timeNow[6:8])
   
        tn = h*3600 + m*60 + s    # time now base Minutes
        nt = tn + inputMinuteInterval * 60
       

        hh  = nt // 3600
        mm = (nt - hh * 3600) // 60 
        ss = nt - (hh * 3600) - mm * 60


        hn = hh - 24 if hh > 24 else hh
        mn = mm - 60 if mm > 60 else mm
        sn = ss - 60 if ss > 60 else ss 

        


        return int(hn), int(mn), int(sn)


def happen(nextTime) :
    
    
    nh, nm, ns = nextTime
    timeNow = str(datetime.now().strftime("%H:%M:%S %p"))
    # print(timeNow)
    
    h = int(timeNow[0:2])
    m = int(timeNow[3:5])
    
    
    if (h == nh) and (m == nm) :
         return True


