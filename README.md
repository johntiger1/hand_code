# hand_code
measuring the potentiometers; visualizing the data


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
