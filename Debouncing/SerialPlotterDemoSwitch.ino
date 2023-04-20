int inter,                // pot contient la valeur actuelle du pot, ancien_pot
    ancien_inter;         // ancien_pot contient la valeur précédente
int sortieST1;            // Valeur lue à la sortie de l'inverseur Schmitt-Trigger (ST)
int sortieST2;            // Valeur lue à la sortie de l'inverseur Schmitt-Trigger (ST)
float valInter,
 valSortieST1,
 valSortieST2;            // Utilisé pour convertir en voltage les valeurs lues
int tolerance=25;         // Permet de réduire l'axe X du graphique affiché 50 = 1/2V approx.

void setup() {
  Serial.begin(9600);
  inter = analogRead(A1);
  ancien_inter = inter;
}

void loop() {
  inter = analogRead(A1); //A1 est branché à la jonction R et C (ou pin3 du 7414)
  while ((inter >= ancien_inter+tolerance) or (inter <= ancien_inter-tolerance)) {  // Si changement
    sortieST1= analogRead(A3); //A3 est branché à la pin 4 du 7414
    sortieST2= analogRead(A2); //A2 est branché à la pin 2 du 7414
    valInter = float(inter*5)/1024; // Conversion en volts pour l'affichage
    valSortieST1 = 5-float(sortieST1*5)/1024; // Conversion en volts pour l'affichage
    valSortieST2 = float(sortieST2*5)/1024; // Conversion en volts pour l'affichage

    Serial.print("inter:");
    Serial.println(valInter);
    Serial.print("Inv(SortieST1):");
    Serial.println(valSortieST1);
    Serial.print("SortieST2:");
    Serial.println(valSortieST2);

    ancien_inter = inter;
  }  
}