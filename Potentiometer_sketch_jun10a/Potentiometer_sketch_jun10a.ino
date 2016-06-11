/***
 * Reads in analog values from pins 0 to 3
 * Specifically written for potentiometers (variable resistors)
*/

int arrPotPins[4] = {0,1,2,3}; //currently hard-coded to use Analog pins 0 1 2 3
int arrPotReadings[4]; //hard-coded to correspond to arrPotPins (i.e. arrPotPins.length should be the size of this arrray)

void setup() 
{
  Serial.begin(9600);
}

void loop() 
{
  
  Serial.println("This is the resistance at pin ");
  for (int i = 0; i < 4; i++)
  {
      
      arrPotReadings[i] = analogRead(arrPotPins[i]); //analog reading from the indicated pin
      Serial.println(arrPotReadings[i]);
  }
  delay(1000); //update every second

   //@TODO
   //analog reads from 0 to 1023, so we will need to scale it to get the true resistance 
   

}
