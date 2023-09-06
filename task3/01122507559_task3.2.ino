/*
Author:Moustafa Ezzeldeen
Description:Cookiebot localization !
*/
#define Room_Width 5
#define Room_Length 6
#define Erorr_Ratio 0.100 /*Suitable Margin of Error in Readings*/

float UltraSonic_0=0;
float UltraSonic_90=0;
float UltraSonic_180=0;
float UltraSonic_270=0;
float x=0;
float y=0;

void setup() {
  Serial.begin(9600);
}

void loop() {
 void GetReadings(); /*Get Readings*/

 if( ( (1-Erorr_Ratio)*Room_Width <= (UltraSonic_0+UltraSonic_180) ) && ( (UltraSonic_0+UltraSonic_180) <= (1+Erorr_Ratio)*Room_Width ) && ( (1-Erorr_Ratio)*Room_Length <= (UltraSonic_90+UltraSonic_270) ) && ( (UltraSonic_90+UltraSonic_270) <= (1+Erorr_Ratio)*Room_Length ) ) /*Check readings Errors are in our acceptable region or not*/
  {
    x=0.500*(UltraSonic_180) + 0.500*(Room_Width-UltraSonic_0); /*Get the average value from the two sensors*/
    
    y=0.500*(UltraSonic_270) + 0.500*(Room_Length-UltraSonic_90);
    
    Serial.print("Postion(X,Y)=("); Serial.print(x); Serial.print(","); Serial.print(y); Serial.println(")");
  }
  
 else {Serial.println("Error in UltraSonic Readings");}
 
 void Move(); /*Move Cookiebot*/
 
}


void GetReadings(){
  /*Some of Ultra Sonic Sensors Calculations*/
}


void Move(){
  /*Some of Control and self_driving algorithms*/
}
