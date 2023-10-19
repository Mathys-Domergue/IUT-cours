#include "WiFi.h" // Librairie pour l'utilisation du WiFi
const char* ssid="MOT_DE_PASSE";
const char* password="MOT_DE_PASSE";

void setup() {
  Serial.begin(115200); // Pour afficher via la laison série
  Serial.println("");
  
  WiFi.mode(WIFI_STA); // Configurer en Station WiFi
 
  WiFi.disconnect(); 
   WiFi.setHostname("Mon_systeme"); // Le nom avec lequel le système sera vu sur le réseau
  WiFi.begin(ssid,password); // Demande de connexion au réseau WiFi
  while(WiFi.status() != WL_CONNECTED)
    { Serial.println("Tentative de connexion...");
      delay(1000);
    }
    Serial.println("");
   Serial.println("Connecté au réseau WiFi !");

   Serial.println("");
   Serial.println("Informations locales :"); // Affichage d'infos sur le système local
   Serial.print("Adresse IP locale : ");
   Serial.print(WiFi.localIP());
   Serial.println("");
   Serial.print("Nom de domaine : ");
   Serial.print(WiFi.getHostname());
   Serial.println("");
   Serial.print("Adresse MAC : ");
   Serial.print(WiFi.macAddress());
   Serial.println("");

    Serial.println("");
    Serial.println("Informations sur le réseau WiFi :"); // Affichage d'infos sur le serveur WiFi
    Serial.print("SSID : ");
    Serial.print(WiFi.SSID());
    Serial.println("");
    Serial.print("Force du signal : ");
    Serial.print(WiFi.RSSI());
    Serial.println("");
    Serial.print("Adresse IP du DNS : ");
    Serial.print(WiFi.dnsIP());
    Serial.println("");
    Serial.print("Adresse IP de la passerelle : ");
    Serial.print(WiFi.gatewayIP());
    Serial.println("");
    Serial.print("Masque de sous-réseau : ");
    Serial.print(WiFi.subnetMask());
    Serial.println("");
    Serial.print("MAC : ");
    Serial.print(WiFi.BSSIDstr());
    Serial.println("");   
    Serial.print("Canal : ");
    Serial.print(WiFi.channel());
    Serial.println("");

    WiFi.disconnect(true);
    Serial.println("Déconnexion."); // On se déconnecte.
    

   }
  

void loop() {
 
}


