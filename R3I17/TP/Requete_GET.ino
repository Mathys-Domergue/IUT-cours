#include "WiFi.h" // Librairie pour l'utilisation du WiFi
#include <HTTPClient.h> // Librairie pour le client http
const char* ssid="MOT_DE_PASSE";
const char* password="MOT_DE_PASSE";


void setup() {
  Serial.begin(115200); // Pour afficher via la liaison série
  Serial.println("");
  
  WiFi.mode(WIFI_STA); // Configurer en Station WiFi
 
  WiFi.disconnect(); 
   
  WiFi.begin(ssid,password); // Demande de connexion au réseau WiFi
  while(WiFi.status() != WL_CONNECTED)
    { Serial.println("Tentative de connexion...");
      delay(1000);
    }
    Serial.println("");
   Serial.println("Connecté au réseau WiFi !");
   Serial.println("");
      
  }
  

void loop() {
 HTTPClient http;

 http.begin("http://www.google.fr");
 int HttpRetCode = http.GET();

 if(HttpRetCode > 0)
 {
  Serial.println("Données reçues...");
  String Contents = http.getString();
  Serial.println(HttpRetCode);
  Serial.println(Contents);
  http.end();
 }
 delay(5000);
  
 }
