// SENSOR ULTRASSÔNICO
#define trigPin 3
#define echoPin 2
long duration;
int distance;

// BUZZERS
int buzzerDistancia = 13;
int buzzerGas = 12;

// MOTOR DE VIBRAÇÃO
int vibration = 8;

// LEDs
int ledverde = 11;
int ledazul = 10;
int ledvermelho = 9;
int ledlaranja = 4;
int ledbranco = 5;

// SENSORES
int LDR = A1;
int sensorGas = A2;
int sensorTemp = A0;

int valorLDR = 0;
int valorGas = 0;

// SETUP
void setup()
{
  Serial.begin(9600);

  // Ultrassônico
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  // Buzzers
  pinMode(buzzerDistancia, OUTPUT);
  pinMode(buzzerGas, OUTPUT);

  // Vibração
  pinMode(vibration, OUTPUT);

  // LEDs
  pinMode(ledverde, OUTPUT);
  pinMode(ledazul, OUTPUT);
  pinMode(ledvermelho, OUTPUT);
  pinMode(ledlaranja, OUTPUT);
  pinMode(ledbranco, OUTPUT);

  // Sensores
  pinMode(LDR, INPUT);
  pinMode(sensorGas, INPUT);
  pinMode(sensorTemp, INPUT);
}

// LOOP
void loop()
{

  // SENSOR ULTRASSÔNICO
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);

  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);

  distance = duration * 0.034 / 2;

  if (distance > 300 || distance <= 0)
  {
    noTone(buzzerDistancia);
    digitalWrite(vibration, LOW);

    Serial.println("Nenhum objeto detectado");
  }

  else if (distance <= 300 && distance > 200)
  {
    tone(buzzerDistancia, 300);
    digitalWrite(vibration, LOW);

    Serial.print("Objeto distante: ");
    Serial.print(distance);
    Serial.println(" m");
  }

  else if (distance <= 200 && distance > 80)
  {
    tone(buzzerDistancia, 700);
    digitalWrite(vibration, LOW);

    Serial.print("Objeto aproximando: ");
    Serial.print(distance);
    Serial.println(" m");
  }

  else if (distance <= 80)
  {
    tone(buzzerDistancia, 2000);
    digitalWrite(vibration, HIGH);

    Serial.print("PERIGO! Muito perto: ");
    Serial.print(distance);
    Serial.println(" m");
  }

  // SENSOR DE TEMPERATURA
  float temperatura =
    (-40 + 0.488155 * (analogRead(sensorTemp) - 20));

  if (temperatura > 30)
  {
    digitalWrite(ledlaranja, HIGH);
  }
  else
  {
    digitalWrite(ledlaranja, LOW);
  }

  // LDR
  valorLDR = analogRead(LDR);

  if (valorLDR < 400)
  {
    apagaLeds();
    digitalWrite(ledverde, HIGH);
  }

  else if (valorLDR >= 400 && valorLDR < 600)
  {
    apagaLeds();
    digitalWrite(ledazul, HIGH);
  }

  else if (valorLDR > 600)
  {
    apagaLeds();
    digitalWrite(ledvermelho, HIGH);
  }
  
  // SENSOR DE GÁS MQ-2
	valorGas = analogRead(sensorGas);

	// NIVEL BAIXO DE GÁS
	if (valorGas > 400 && valorGas <= 500)
    {
  	digitalWrite(ledbranco, HIGH);
	
 	 noTone(buzzerGas);

  	Serial.println("Gas detectado!");
	}

	// NIVEL ALTO DE GÁS
	else if (valorGas > 500)
  {
  	digitalWrite(ledbranco, HIGH);

  	tone(buzzerGas, 1000);

  	Serial.println("ALERTA DE GAS!");
	}

	// SEM GÁS
	else
	{
  	digitalWrite(ledbranco, LOW);

  	noTone(buzzerGas);
    }
  // MONITOR SERIAL
  Serial.print("Distancia: ");
  Serial.print(distance);
  Serial.print(" cm");

  Serial.print(" | Temperatura: ");
  Serial.print(temperatura);

  Serial.print(" C");

  Serial.print(" | LDR: ");
  Serial.print(valorLDR);

  Serial.print(" | Gas: ");
  Serial.println(valorGas);

  delay(500);
}

// FUNÇÃO APAGAR LEDS
void apagaLeds()
{
  digitalWrite(ledverde, LOW);
  digitalWrite(ledazul, LOW);
  digitalWrite(ledvermelho, LOW);
  digitalWrite(ledbranco, LOW);
}