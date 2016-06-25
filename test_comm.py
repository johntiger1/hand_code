import serial
import time
#recall that in WINDOWS, we don't use dev tty!

ser = serial.Serial('COM5', 9600, timeout=0) # open serial port
#print(ser.name) # check which port was really used
#x = ser.read(100) # read a string, of 100 bytes

#potentially, this IS the LOOP
while 1:
    #print ("this is what we have\n")
    try:
        #ser.write('hello')
        print ser.readline()
        print ser.readline()
        print ser.readline()
        print ser.readline()
        print ser.readline()
        time.sleep(1)
    except ser.SerialTimeoutException:
        print('Data could not be read')
        time.sleep(1)
# close port



