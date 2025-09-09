/*
 * Arun CS
 * Github : https://github.com/aruncs31s
 */ 

const int RELAY_PIN_1 = 26 ;
const int RELAY_PIN_2 = 27 ;


void setup(){
  Serial.begin(9600);
  pinMode(relay,OUTPUT);

}
void loop(){
  digitalWrite(RELAY_PIN_1,LOW);
  Serial.println("Relay PIN_1 made low");
  delay(5000);
  digitalWrite(RELAY_PIN_1,High);
  Serial.println("Relay PIN_1 made High");
   delay(5000);
}
