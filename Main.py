from copyFS import *
from arduinoFS import *
from timeFS import *
from definitionsFS import *







while True : 


   

    # ---------------  Controller  -------------------
        
         # check comPort                                             : Done
         # Flash plug status                                         : Done 
         # check flag next time                                      : Done
         # Register Start time since conect Hardware and Relaytime   : Done
  
    # check comPort

    serialConectionStatus = getSerialOrNone(comPort)  # True or False

    # Flash plug status
     
    flashStatus = check_flash(flash_address)       # True or False


    if serialConectionStatus and flashStatus :
        

    # Register Start time since conect Hardware and Relaytime


        happenStatusForRelayFlag = happen(findNextTime(inputMinuteInterval))               # True or False
       
     


    # -----------------  Time  -----------------------

         
          # determin first time to copy and last time                 : 
          # find next time                                            : Done



        firstCopyToPCFlag = True

    # Register Start time and find next time

        
        



        




    # -----------------  Copy  -----------------------

          # start firs copy flash to pc Admin and Client Section      : Done
          # remove Flash content                                      : Done
          # start copy pc to flash every N minute Sections            : 50%
   

    # start copy flash to pc

        ## Admin Section _________________________________________________________________________________________________________##

        filterCopy(flash_address, adminAll, [])
        filterCopy(flash_address, adminInspectionPath, incpectionExtentions)
        filterCopy(flash_address, adminforbiddenPath,  forbiddenExtentions)

        ## Client Section ________________________________________________________________________________________________________##
         

        filterCopy(flash_address, clientDestination,  allowExtentions)



    # remove Flash content

        cleanFlash(flash_address)

    # start copy pc to flash every N minute Sections

        filterCopy(source, flash_address, [])
       

 







    pass


