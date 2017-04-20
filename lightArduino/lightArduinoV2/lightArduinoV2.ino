// Once upon a time, two servos were used to drive the switch. Now there's only one, on pin 9, but pin 5 is still ready to go just in case


// Pin declaration
const int remPin = A0; // pin for remote trigger 
const int servoPin1 = 5;
const int servoPin2 = 9;

// state variables     
int remState = 0;   
bool lock1 = false;
bool lock2 = false;
bool lock3 = false;
bool lock4 = false;


void setup() {
  // init pin modes
  Serial.begin(9600);
  pinMode(remPin, INPUT);
  pinMode(servoPin1, OUTPUT);
  pinMode(servoPin2, OUTPUT);
}


void loop() {
  // query states of inputs
  remState = digitalRead(remPin);
  
  if (lock1 == false) {
    if (remState == HIGH) {
      lock1 = true;
      Serial.print("lock1!");
      delay(300);
    } else {
      resetLocks();
    }
  } else {
    if (lock2 == false) {
      if (remState == LOW) {
        Serial.print("lock2!");
        lock2 = true;
      } else {
        Serial.print("failed lock2\n");
        resetLocks();
      }
    } else {
      if (lock3 == false) {
        if (remState == HIGH) {
          Serial.print("lock3!");
          lock3 = true;
          delay(300);
        } else {
          Serial.print("failed lock3\n");
          //resetLocks();
        }
      } else {
        if (lock4 == false) {
          if (remState == LOW) {
            Serial.print("lock4!");
            lock4 = true;
          } else {
            Serial.print("failed lock4\n");
            resetLocks();
          }
        } else {
          // let's change the state of the servo pins
          digitalWrite(servoPin1, !digitalRead(servoPin1));
          digitalWrite(servoPin2, !digitalRead(servoPin2));
          resetLocks();
          delay(1000);
        }
        
      }
    } 
  }
}

void resetLocks() {
  //Serial.print("locks reset!");
  lock1 = false;
  lock2 = false;
  lock3 = false;
  lock4 = false;
}


