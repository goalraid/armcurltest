#include<Servo.h>
Servo servo1;
int pos = 0;
void setup() {
  // put your setup code here, to run once:
servo1.attach(9);
Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
while(Serial.available()==0){};
String data = Serial.readString();
servo1.write(data.toInt());
Serial.println(data);
}
