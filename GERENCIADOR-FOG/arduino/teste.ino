
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

}

void loop() {
  // put your main code here, to run repeatedly:
  p1();
  p2();
  delay(2000);
}

void p1() {
  int umidade = 50;
  int temperatura = 25;
  int sensorChamas = 1;
  int valorSensorFumaca = 4;
  byte pacoteOrigem = 0xAA;
  byte pacoteOrigem2 = 0xA8;
  Serial.write(0x11);
  Serial.write(pacoteOrigem);
  Serial.write(pacoteOrigem2);
  Serial.print(umidade);
  Serial.print(temperatura);
  Serial.print('0');
  Serial.print(valorSensorFumaca);
  Serial.print(sensorChamas);
}

void p2() {
  int umidade = 50;
  int temperatura = 25;
  int sensorChamas = 1;
  int valorSensorFumaca = 4;
  byte pacoteOrigem = 0xAA;
  byte pacoteOrigem2 = 0xAB;
  Serial.write(0x11);
  Serial.write(pacoteOrigem);
  Serial.write(pacoteOrigem2);
  Serial.print(umidade);
  Serial.print(temperatura);
  Serial.print('0');
  Serial.print(valorSensorFumaca);
  Serial.print(sensorChamas);
}
