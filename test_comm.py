
# Import serial (this is the library that allows us to read and write to the serial port)
import serial
import time

# recall that in WINDOWS, we don't use dev tty! (dev tty works for Mac/Unix environments)
ser = serial.Serial('COM5', 9600, timeout=0) # open serial port, baud rate 9600

#TODO Link it with the Arduino program so that COM5 and the # of readLines doesn't need to be hardcoded

f = open("pot_readings", "w")

# Note: this is NOT the "loop" of Arduino
# In fact, that is the WRONG paradigm of thinking--we're not directly translating
# the arduino into python code, we're simply using pyserial to write to and read from the serial port
while 1:
    try:
        # Python refresher: goes from 0 to 4 (inclusive, exclusive--so 5 iterations)
        for i in range (0, 4):
            print ser.readline() #testing purposes only
            f.write(ser.readline())

        time.sleep(1)
    except ser.SerialTimeoutException:
        print('Data could not be read')
        time.sleep(1)
# close port, close file

f.close(f)

# TODO make JSON stuff using python built-ins --should be very simple

