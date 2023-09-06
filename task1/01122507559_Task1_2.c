/*
Author:Moustafa Ezzeldeen
Description:Launch Missles !
*/

/*Header Files*/
#include <stdio.h>
#include <time.h> /* To use time library of C */
void delay(int number_of_seconds)
{
    /* Converting time into milli_seconds */
    int milli_seconds = 1000 * number_of_seconds;

    /* Storing start time */
    clock_t start_time = clock();

    /* looping till required time is not achieved */
    while (clock() < start_time + milli_seconds);
}
int main()
{
int x;
int i;
scanf("%d",&x);
for(i=x; i>0 ;i--){ printf("%d\n",i); delay(1);}
printf("Blast off to the moon!");
return 1;
}
