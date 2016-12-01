// Once upon a time, two servos were used to drive the switch. Now there's only one, on pin 9, but pin 5 is still ready to go just in case


// Pin declaration
const int btnPin = A0; // manual button trigger
const int remPin = A4; // pin for remote trigger 
const int servoPin1 = 5;
const int servoPin2 = 9;

// state variables
int btnState = 0;        
int oldBtnState = 0;
int remState = 0;
int oldRemState = 0;    
int count = 0;

void setup() {
  // init pin modes
  pinMode(btnPin, INPUT);
  pinMode(remPin, INPUT);
  pinMode(servoPin1, OUTPUT);
  pinMode(servoPin2, OUTPUT);

  // initialize servos as opposing, as they'll be on opposite sides of the switch
  digitalWrite(servoPin1, HIGH);
  digitalWrite(servoPin2, LOW);
}


void loop() {
  btnState = digitalRead(btnPin);
  remState = digitalRead(remPin);
  if (btnState != oldBtnState) {
    // If the state has changed from low to high, we should increment the counter
    if (btnState == HIGH) {
      count++;
      // change state according to the counter
      if (count % 2 == 0) {
        digitalWrite(servoPin1, HIGH);
        digitalWrite(servoPin2, LOW);
      } 
      else {
        digitalWrite(servoPin1, LOW);
        digitalWrite(servoPin2, HIGH);
      }
      //set cooldown of one second
      delay(1000);
    }
  }

  if (remState != oldRemState) {
    if (remState == HIGH) {
      count++;
      // change state according to the counter
      if (count % 2 == 0) {
        digitalWrite(servoPin1, HIGH);
        digitalWrite(servoPin2, LOW);
      } 
      else {
        digitalWrite(servoPin1, LOW);
        digitalWrite(servoPin2, HIGH);
      }
      //set cooldown of one second
      delay(1000); 
    }
  }
  // save this state as the old one for later
  oldBtnState = btnState;
  oldRemState = remState;
}


