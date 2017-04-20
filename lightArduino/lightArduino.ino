// Once upon a time, two servos were used to drive the switch. Now there's only one, on pin 9, but pin 5 is still ready to go just in case


// Pin declaration
const int btnPin = A0; // manual button trigger
const int remPin = A1; // pin for remote trigger 
const int servoPin1 = 5;
const int servoPin2 = 9;

// state variables
int btnState = 0;        
int remState = 0;   

void setup() {
  // init pin modes
  pinMode(btnPin, INPUT);
  pinMode(remPin, INPUT);
  pinMode(servoPin1, OUTPUT);
  pinMode(servoPin2, OUTPUT);

  pinMode(10, OUTPUT);
  digitalWrite(10, HIGH);
}


void loop() {
  // query states of inputs
  btnState = digitalRead(btnPin);
  remState = digitalRead(remPin);

  // If either of them are high...
  if(btnState == HIGH || remState == HIGH) {
    // let's change the state of the servo pins
    digitalWrite(servoPin1, !digitalRead(servoPin1));
    digitalWrite(servoPin2, !digitalRead(servoPin2));

    // sleep for two seconds to prevent spam
    delay(2000);
  }
}


