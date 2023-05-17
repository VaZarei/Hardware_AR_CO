import os
import time

flash_address =  "r:"



def check_flash(flash_address):
    i = 0
    try:
      for files in os.listdir(flash_address) :
        i+=1
      return i

    except FileNotFoundError :
       return i



while True:
   
    checking = check_flash(flash_address)

    if checking > 0 :
     print("The Address is available") 
    else:
     print("The Address is not available !!!")

    time.sleep(2)
    

    
