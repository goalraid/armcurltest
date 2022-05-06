#include <Servo.h>
Servo myservo;
Servo myservo2;
Servo myservo3;
Servo myservo4;
Servo myservo5;
Servo myservo6;
int pos = 150;
int pos2 = 70;


void setup()

{
myservo.attach(3);
myservo.write(pos);

myservo2.attach(5);
myservo2.write(pos);

myservo3.attach(6);
myservo3.write(pos);

myservo4.attach(9);
myservo4.write(pos);

myservo5.attach(10);
myservo5.write(pos);

myservo6.attach(11);
myservo6.write(pos);

Serial.begin(9600);
}

void loop() {
myservo.write(pos2);


myservo2.write(pos2);


myservo3.write(pos2);


myservo4.write(pos2);


myservo5.write(pos2);


myservo6.write(pos2);

delay(3000);
myservo.write(pos);


myservo2.write(pos);


myservo3.write(pos);


myservo4.write(pos);


myservo5.write(pos);


myservo6.write(pos);

delay(3000);
}
