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
    

    print("\n***** Checkin Serial Port and Flash Connection *****")
    # check comPort
    serialConectionStatus = getSerialOrNone(comPort)  # True or False

    # Flash plug status
    flash_address = findUsbLetter(flashUsbName)
    flashStatus   = check_flash(flash_address)       # True or False


    if serialConectionStatus and flash_address :
        print("\nStart next Steps :")
        
        

    # Register Start time since conect Hardware and Relaytime

        
        happenStatusForRelayFlag = happen(findNextTime(inputMinuteIntervalForRelay))               # True or False
       
        if happenStatusForRelayFlag :
            print("Relay make change in 10 second later !")
            time.sleep(20)
            #relayPc1(comPort)

            if not(flashStatus and serialConectionStatus) :
                happenStatusForRelayFlag = False
                time.sleep(40)
                break



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

        print("\n***** Start copy flash to pc")
        print(flash_address , adminAll)
        filterCopy(flash_address, adminAll, [])
        filterCopy(flash_address, adminInspectionPath, incpectionExtentions)
        filterCopy(flash_address, adminforbiddenPath,  forbiddenExtentions)

        ## Client Section ________________________________________________________________________________________________________##
         

        filterCopy(flash_address, clientDestination,  allowExtentions)



    # remove Flash content

        #cleanFlash(flash_address)

    # start copy pc to flash every N minute Sections
        print("\n***** Start copy PC to Flash")
        filterCopy(clientDestination, flash_address, [])
       

 





    print("End of while -----------------------------------------------------------------")
    time.sleep(10)
    pass


