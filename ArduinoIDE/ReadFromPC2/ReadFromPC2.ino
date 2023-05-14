String inBytes = "a" ;

byte RAV  = 2;
byte RAG  = 3;
byte RADP = 4;
byte RADN = 5;

byte RBV  = 6;
byte RBG  = 7;
byte RBDP = 8;
byte RBDN = 9;

byte LEDPC1 = 10;
byte LEDPC2 = 11;


void setup() {
  
Serial.begin(9600);
pinMode(LED_BUILTIN, OUTPUT);

}

void loop() {

if (Serial.available()>0){
  inBytes = Serial.readStringUntil('\n');
  
  if (inBytes == "pc1"){

    digitalWrite(LEDPC2, LOW);
    digitalWrite(LEDPC1, HIGH);

    

    digitalWrite(RBDP, LOW);
    digitalWrite(RBDN, LOW);
    delay(3000);
    digitalWrite(RBV, LOW);
    digitalWrite(RBG, LOW);
    delay(1000);

    digitalWrite(RAV, HIGH);
    digitalWrite(RAG, HIGH);
    delay(3000);
    digitalWrite(RADP, HIGH);
    digitalWrite(RADN, HIGH);



    digitalWrite(LED_BUILTIN, HIGH);
    delay(2000);
    digitalWrite(LED_BUILTIN, LOW);

    
    
  }

  if (inBytes == "pc2"){


    digitalWrite(LEDPC1, LOW);
    digitalWrite(LEDPC2, HIGH);

    digitalWrite(RADP, LOW);
    digitalWrite(RADN, LOW);
    delay(3000);
    digitalWrite(RAV , LOW);
    digitalWrite(RAG , LOW);
    delay(1000);

    
    digitalWrite(RBV, HIGH);
    digitalWrite(RBG, HIGH);
    delay(3000);
    digitalWrite(RBDP, HIGH);
    digitalWrite(RBDN, HIGH);
    

    digitalWrite(LED_BUILTIN, HIGH);
    delay(2000);
    digitalWrite(LED_BUILTIN, LOW);

    
    
  }

  }


}
