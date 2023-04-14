int inter,                // inter contient la valeur actuelle de inter
    ancien_inter;         // ancien_inter contient la valeur précédente
int sortieST1;            // Valeur lue à la sortie de l'inverseur Schmitt-Trigger (ST)
int sortieST2;            // Valeur lue à la sortie de l'inverseur Schmitt-Trigger (ST)
float valInter,
 valSortieST1,
 valSortieST2;            // Utilisé pour convertir en voltage les valeurs lues
int tolerance=50;         // Permet de réduire l'axe X du graphique affiché 50 = 1/2V approx.
int valeurs[500];
bool roule = true;
int nb = 50;              // Nombre de valeurs de A1 à conserver

void setup() {
  Serial.begin(9600);
  inter = analogRead(A1);
  ancien_inter = inter;
//  Serial.print("inter=");
//  Serial.println(inter);
}

void loop() {
  while (roule) {
    inter = analogRead(A1);
      if ((inter >= ancien_inter+tolerance)
          or (inter <= ancien_inter-tolerance)) {  // Si changement important
        delay(250);
        for (int i=0;i<nb;++i) {                   // Commence à recueillir
          inter = analogRead(A1);                  //  les valeurs lues
          valeurs[i] = inter;                      //  pour les analyser
        } // fin du for
//        roule = !roule;
        for (int i=0; i<nb;i++){
          Serial.print("inter:");
          Serial.println(float(valeurs[i]*5)/1023);
        } // fin du for
      } // fin du if
    } // fin du while
    ancien_inter = inter;
  } // fin de loop
