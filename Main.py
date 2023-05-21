from copyFS import *
from arduinoFS import *
from timeFS import *
from definitionsFS import *



flash_address = findUsbLetter(flashUsbName)
flashStatus   = check_flash(flash_address)        # True or False

while not(flashStatus):
     
     flash_address = findUsbLetter(flashUsbName)
     flashStatus   = check_flash(flash_address)
     print("\nPlease Conect the Property Flash !")
     time.sleep(5)
     
while flashStatus: 

    
    #serialConectionStatus = getSerialOrNone(comPort)  # True or False
    flash_address = findUsbLetter(flashUsbName)
    flashStatus   = check_flash(flash_address)        # True or False


    
    copyF2pFlag = True
    
    for step in range(0, 4):
            flash_address = findUsbLetter(flashUsbName)
            flashStatus   = check_flash(flash_address)
            
            
            while not(flashStatus):

               
                flash_address = findUsbLetter(flashUsbName)
                flashStatus   = check_flash(flash_address)
                time.sleep(2)



    # Copy Details --------------------------------------------------------------------.
              
            print(f'\nCopy step --------------------------------------------------------------------------------------- > {step}')


            if not(copyF2pFlag) :
                 
                ## Admin Section P2F  _________________##

                print("\n***** Start  copy PC to Flash Admin Section")
                print("***** End of copy PC to Flash Admin Section")
                time.sleep(10)

                ## Client Section P2F  _________________##
            
                print("\n***** Start  copy  PC to Flash Client Section")
                print("***** End of copy  PC to Flash Client Section")
                time.sleep(10)

            

            if copyF2pFlag :

                ## Admin Section F2P  _________________##

                print("\n***** Start  copy flash to pc Admin Section")
                print("***** End of copy flash to pc Admin Section")
                time.sleep(10)

                ## Client Section F2P  ________________##
            
                print("\n***** Start  copy flash to pc Client Section")
                print("***** End of copy flash to pc Client Section")

                copyF2pFlag = False
                time.sleep(10)


                # Delete All contain in flash - ---------------------

                print("\n---------------------Delete All contain in flash---------------------")
                time.sleep(10)





    # Time Details --------------------------------------------------------------------.

            time.sleep(stepCopyInterval)
            
      
    # Relay Details ---------------------------------------------------------------------------.
    
    print("------------------------------ Start of Relay Action ------------------------------\n")
    print("relay Status :")

    relyFlag = relayPc1(comPort)
    while not(relyFlag) :
         
         print("in while Flag")
         relyFlag = relayPc1(comPort)
         time.sleep(5)
         

         

    

    
              
         
    time.sleep(10)






"""
   

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
        
        

    # Register Start time since connect Hardware and Relaytime

        
        



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


"""