int pot,                  // pot contient la valeur actuelle du pot, ancien_pot
    ancien_pot;           // ancien_pot contient la valeur précédente
int sortieST;             // Valeur lue à la sortie de l'inverseur Schmitt-Trigger (ST)
float valPot, valSortieST;// Utilisé pour convertir en voltage les valeurs lues
int tolerance=10;         // Permet de réduire l'axe X du graphique affiché 50 = 1/2V approx.

void setup() {
  Serial.begin(9600);
  pot = analogRead(A1);
  ancien_pot = pot;
}

void loop() {
  pot = analogRead(A1); // A1 est connecté à la partie centrale du pot (ou à la pin 1 du 7414)
  while ((pot >= ancien_pot+tolerance) or (pot <= ancien_pot-tolerance)) {  // Si changement
    sortieST= analogRead(A2); //A2 est connecté à la pin 2 du 7414
    valPot = float(pot*5)/1023; // Conversion en volts pour l'affichage
    valSortieST = float(sortieST*5)/1023; // Conversion en volts pour l'affichage

    Serial.print("Pot:");
    Serial.println(valPot);
    Serial.print("SortieST:");
    Serial.println(valSortieST);

    ancien_pot = pot;
  }  
}
