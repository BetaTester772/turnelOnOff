int LED1 = 13, LED2 = 12, LED3 = 11;
int Sensor1 = 10, Sensor2 = 9, Sensor3 = 8, Sensor4 = 7;
int Sector1 = 0, Sector2 = 0, Sector3 = 0;

void setup() {
  pinMode(Sensor1, INPUT);
  pinMode(Sensor2, INPUT);
  pinMode(Sensor3, INPUT);
  pinMode(Sensor4, INPUT);
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
  Serial.begin(9600);
}

 

void loop() {
  int Sen1 = digitalRead(Sensor1);
  int Sen2 = digitalRead(Sensor2);
  int Sen3 = digitalRead(Sensor3);
  int Sen4 = digitalRead(Sensor4);  
  delay(100);
  if (Sen1 == 1){
    Sector1++;
    Sector2++;
  }
  if (Sen2 == 1){
    Sector1--;
    Sector3++;
  }
  if (Sen3 == 1){
    Sector2--;
  }
  if (Sen4 == 1){
    Sector3--;
  }
  delay(100);
  if (Sector1 >= 1)
    digitalWrite(LED1, HIGH);
  else
    digitalWrite(LED1, LOW);
    
  if (Sector2 >= 1)
    digitalWrite(LED2, HIGH);
  else
    digitalWrite(LED2, LOW);
    
  if (Sector3 >= 1)
    digitalWrite(LED3, HIGH);
  else
    digitalWrite(LED3, LOW);
}
