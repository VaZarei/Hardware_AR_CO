String inBytes = "a" ;

void setup() {
  
Serial.begin(9600, COM3);
pinMode(LED_BUILTIN, OUTPUT);

}

void loop() {

if (Serial.available()>0){
  inBytes = Serial.readStringUntil('\n');
  
  if (inBytes == "on"){
    digitalWrite(LED_BUILTIN, HIGH);
    Serial.write("Led on");
  }

  if (inBytes == "off"){
    digitalWrite(LED_BUILTIN, LOW);
    Serial.write("LED OFF");
  }

  }


}
