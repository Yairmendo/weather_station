//Estación de calidad de aire

//Lib
#include "ESP826WiFi.h"
#include <aREST.h>
#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>


//Def
#define DHTPIN D5
#define DHTTYPE DHT22
#define MQ A0

//Init
DHT dht(DHTPIN, DHTTYPE);

//aREST
aREST rest = aREST();

//WiFi
const char* ssid = "Nombre de tu red"
const char* password = "contraseña de la red"

//Port
#define LISTEN_PORT 80

//Crear instancia de servidor
WiFiServer server(LISTEN_PORT)

//Variables API
float mq, humidity, temperature;

void setup(){
  Serial.begin(9600);
  dht.begin();

//Iniciar Variables API
rest.variable("temperature", &temperature);
rest.variable("humidity", &humidity);
rest.variable("pollution", &mq);

//Name ID
  rest.set_id("1");
  rest.set_name("sensor_wemos");

//Conectar a WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED)
    {
      delay(500);
      Serial.print(".");
    }
  Serial.print("");
  Serial.print("WiFi connected!");

//Start Server
  server.begin();
  serial.printIn("Server started!");

//IP
  Serial.printIn(WiFi.localIP());
}

void loop() {
  //Wait
  delay(1000);
  mq = analogRead(MQ); //MQ135
  humidity = dht.readHumidity(); //RH %0 - 100 (Punto rocio)
  temperature = dht.readTemperature(); //0 - 100 *100

  //REST Calls
  WiFiClient client = server.available();
  if (!cliente)
  {
    return;
  }
  while(!client.available())
  {
    delay(1);
  }
  rest.handle(client);
  }
