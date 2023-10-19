#include "WiFi.h" // Librairie pour l'utilisation du WiFi
const char* ssid="NOM_WIFI";
const char* password="MOT_DE_PASSE";

void setup() {
  Serial.begin(115200); // Pour afficher via la laison série
  Serial.println("");
  WiFi.mode(WIFI_STA); // Configurer en Station WiFi
  WiFi.begin(ssid,password); // Demande de connexion au réseau WiFi
  while(WiFi.status() != WL_CONNECTED)
    { Serial.println("Tentative de connexion...");
      delay(1000);
    }
   Serial.println("Connecté au réseau WiFi !");
   
  }
  

void loop() {
 
}
