# hand_code
measuring the potentiometers; visualizing the data


#***UPDATE JUNE 24

Succesfully managed to start reading into python. Now we have the Arudino data in a more robust format.

Key Insights: pySerial is NOT a complete replacement for Arduino. Instead it simply serves as an interface for reading from and 
writing to a serial port. Thus, to do any interesting thing with it, the following steps are required:

1) Write the Arduino program. Upload it to the board (via Arduino program).
2) In python, import pyserial. Open the port, and simply use the readLine command to get what you would normally get from Serial Monitor into python.

More on ReadLine: note that this INTRICATELY LINKS the ARDUINO and the PYTHON program!
i.e. if you look at the code uploaded, the reason why we readLine 5 times is BECAUSE we Serial.println() 5 times in the Arduino program

In summary, what pySerial does is it REPLACES the serial monitor of Arduino, allowing us to get the data in python and thus be able to write it
to a file, upload it etc.

***END UPDATE

@TODO:
Implementing web stuff
We want to get the readings from the arduino onto the web. This will be the first step in visualization

So far the thinking goes like this: use something that has serial support (i.e. is able to read in the values directly into a programming environment ex. pyserial ). Then, use something like the python web server to put it on the web. Alternatively, we could just write it onto a file, and have the file be accessed by a web app, segregating the two.

The first approach is probably better for prototyping, but the second approach is more scalable.

Reading: 
http://playground.arduino.cc/Main/InterfacingWithHardware#Communication
http://playground.arduino.cc/Main/InterfacingWithSoftware  (interesting: look at Arduino + Unity)
https://ruslanspivak.com/lsbaws-part1/


//Stream of thought stuff
COuple of approaches: 
have it directly via c or python 
or have it as a file and then have it as a C or python thing
or have it as a file and then have it as a webapp stuff—i.e. getting the file onto the web? how?
//have it write to the server/data/assets part and then just do a getJSON based on that
interesting: actually, we should do stuff to 


//essentially implementing the relayr stack
