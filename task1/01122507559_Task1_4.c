/*
Author:Moustafa Ezzeldeen
Description:Kalman Missile !
*/

/*Macros*/
#define mpu6050_Accuracy 79.0000
#define bno55_Accuracy 92.0000
#define y0 0
#define VsinA 21.5801
#define g -9.8066
#define t ((i*4.4011)/9)
#define kg ((mpu6050_Accuracy/100.000)*(bno55_Accuracy/100.000))
/*Header Files*/
#include <stdio.h>


/*Initial velocity (m/s)
30
Angle (degrees)
46
Duration (secs)
4.40
Distance (m)
91.72
Maximum height (m)
23.74
*/

/*Position formula(in y-direction)*/ /* yt=y0+VsinA*t+ 0.50*g*t*t */


int main()
{
printf("Hello World\n\n");
char i;
float Physics[10];
float Legend[10];
for(i=0; i<10;i++){Physics[i]=y0+(VsinA*t)+ (0.5000*g*t*t);}; /*calculate theoretical y-Position */
float mpu6050[10] = {0.0, 11.68, 18.95, 23.56, 25.72, 25.38, 22.65, 18.01, 10.14, -0.26};
float bno55[10] = {0.0,9.49, 16.36, 21.2, 23.16, 22.8, 19.5, 14.85, 6.79, -2.69};
float Good_Readings[10];
for(i=0; i<10;i++){Good_Readings[i]=(mpu6050_Accuracy/(mpu6050_Accuracy+bno55_Accuracy))*mpu6050[i]+(bno55_Accuracy/(mpu6050_Accuracy+bno55_Accuracy))*bno55[i];} /*calculate average reading for sensors*/
printf("Legend_Readings:{");
for(i=0; i<10;i++){Legend[i]=Physics[i]+ kg*(Good_Readings[i]-Physics[i]);printf("%f,",Legend[i]);}; /*kalman filter */
printf("}\n\n");
}
