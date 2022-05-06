
#include <Servo.h> 

Servo servo1;
Servo servo2;            

int servodata;

void setup() 
{ 
Serial.begin(9600);  
Serial.println("Redy");
Serial.println("1 stop ");
Serial.println("2 forward");
Serial.println("3 backward");
Serial.println("4 Turn left");
Serial.println("5 Turn right");

   servo1.attach(9) ;
   pinMode(9, OUTPUT);
    servo2.attach(11) ;
    pinMode(11, OUTPUT);




} 

void loop() 
{

  if (Serial.available() > 0)
  {
     while(Serial.available()==0){};
     String servodata = Serial.readString();
     //servodata = Serial.read();

 if(servodata == '1') // Single Quote! This is a character.
  {
  Serial.println("Stop");
  {                                 
servo1.write(150); //stop 
servo2.write(0);   
 delay(3000);                 
  } 
    }


    if(servodata == '4')
    {
      Serial.println("Turn left");
      {
servo1.write(0); //stop 
servo2.write(150);   
 delay(3000); 
} 
    }

    if(servodata == '5')
    {
      Serial.println("Turn right");
      {
  servo1.write(180);  //Turn right
  servo2.write(180); 
  delay(3000);
    } 
        }


    if(servodata == '2')
    {
      Serial.println("Forward");
      {
  servo1.write(0);  //Forward
  servo2.write(180); 
  delay(3000);
} 
    }

   if(servodata == '3')
    {
      Serial.println("Backward");
  {
servo1.write(180); //Backward
  servo2.write(0);
   delay(3000);
    }
    }


    Serial.println(" ");    // End the line


  }
    }
