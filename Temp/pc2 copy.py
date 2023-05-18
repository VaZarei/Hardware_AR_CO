import serial
import time



import serial
from serial import SerialException


def getSerialOrNone(port):
    try:
       return serial.Serial(port)
    except:
       return "None"


port = 'COM4'

while True :
   
   print(getSerialOrNone(port))
   time.sleep(2)



# Use the serial port...




# while True :

#     print("444444444444")

#     try:
        
#         print("1111111111111111")
#         print(serial.Serial('COM4', 9600, timeout=5.0))
       
        
#     except serial.SerialException:
#         print("6666--------------------------------6")
#         while True:

#              print(serial.Serial('COM4', 9600, timeout=5.0))
#              time.sleep(2)
#              print("22222222222222")





# # while True:
    
# #     i = input("input(pc1 / pc2) :").strip()
# #     if i =='done':
# #         print("Finesh program")
# #         break

# #     serialcomm.write(i.encode())
# #     time.sleep(0.5)
    

# # serialcomm.close()