/*
Author:Moustafa Ezzeldeen
Description:Task Manager! with low memory usage.
*/

typedef unsigned char U8; /*Used unsigned Char Because Its size is 1 Byte*/

/*Header Files*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 64 /*Max Description 64 Letter*/
int main()
{

U8 x=0; /*Used Char Because x,ID are Short Unsigned Integers*/ /*x Is Multi Tasking Variable for all uses*/ /*buffer for Description length , counter for loops , Store user inputs , the conditions in IF */
U8 ID_Next=1; /*used to store next ID*/

/* Using Dynamic Memory Allocation Because We don't know how many tasks the user will enter */
U8 **tasks=malloc(1 * sizeof(U8*));/* used to store a dynamically allocated array of pointers of U8 every array represents an task and every pointer represents letter*/

U8 *done=calloc(1,sizeof(U8)); /*Done flag every bit represents an ID in order 1 for completed tasks 0 for incomplete  */ /*calloc to make all bits initialized with zero*/

U8 buffer[BUFFER_SIZE]; /* buffer will be used to accept each string of input from the user*/

U8 a=0; /*Not used but Important! The program would not work if it was deleted*/

printf("Welcome to Minions Task Manager\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Mark Task\n5. Exit\n\n");

while(1) /*Tasks Loop*/
{

 printf("Select an option:");
 scanf("%d",&x);

 if(x==1) /*Add Task*/
   {

     * tasks = realloc(*tasks,ID_Next * sizeof(U8 *)); /*Change size of the array when user add task that represented as pointer of char */
     if((ID_Next!=1) && ((ID_Next-1)%8==0) ){done = realloc(done,( ( (ID_Next-1)/8 ) +1 ) * sizeof(U8));} /*1 byte can store 8 done flag for 8 tasks*/ /*Resize The Done Every 8 ID*/
     printf("\nEnter task description:");

	 /* fgets will store the \n char entered by the user when they hit enter,
     shift up the null terminator by one char so the \n is eliminated from the string */
     while (getchar() != '\n');
     fgets(buffer, BUFFER_SIZE, stdin);
     x = strlen(buffer);
	 buffer[x - 1] = '\0';
	 /* dynamically allocate enough space to store the the string*/
     /* pointer to this block of memory in tasks[i]*/
     tasks[ID_Next-1] = malloc(x * sizeof(U8));

     /*copy the string from the buffer to the dynamically allocated memory*/
     strcpy(tasks[ID_Next-1], buffer);

     done[(ID_Next-1)/8]&=~(1<<((ID_Next-1)%8)); /*initialize all bits with zero because after 8 tasks the realloc will make new uninitialized bits*/

     printf("Task added successfully!\n\n");

     ID_Next++;

   }

 else if(x==2) /*View Task*/
   {
     printf("\nCurrent Tasks:\n");
     for (x = 1; x < ID_Next; x++) /*loop to print all existed tasks*/
     {
     printf("\nTask ID:%d\nDescription:%s\n",x,tasks[x-1]);

     if( ( (done[(x-1)/8]) & ( 1<< ((x-1)%8) ) ) !=0 ){printf("The Task is completed\n\n");} /*Check the done flag*/

     else {printf("The Task is Incomplete\n\n");}
     }

   }

 else if(x==3) /*Remove Task*/
   {

     printf("\nEnter task ID to remove:");
     scanf("%d",&x);
     if((x<ID_Next)&&(x>0))
        {
         if(!((ID_Next-x)==1)) /*Check If the ID is for Last Task or not */
          {
            for(x; x<ID_Next-1; x++)
            {
              tasks[x-1]=realloc(tasks[x-1],strlen(tasks[x]) * sizeof(U8));  strcpy(tasks[x-1],tasks[x]);/*Resize and Move All Tasks One Step Back*/

              if (( (done[(x)/8])  &   ( 1<< ((x)%8) ) )){ done[(x-1)/8] |=( ((done[(x)/8]) & ( 1<< ((x)%8))) >> 1 );printf("here:%d\n",( (done[(x)/8])  &   ( 1<< ((x)%8) ) ));} /*Move All Flags After the Removed Task*/
              else {done[(x-1)/8] &=~(  ( 1<< ((x)%8)) >> 1 ) ;}
            }
          }
         free(tasks[ID_Next-2]);  /*Free The Last Task*/
         done[(ID_Next-2)/8]&=~(1<<((ID_Next-2)%8)); /*Free Last Flag*/
         ID_Next--; printf("Task removed successfully!\n\n");
        }
     else {printf("The Task ID Does Not Exist !!\n\n");}

   }

 else if(x==4) /*Mark Task*/
   {
    printf("\nEnter task ID to mark it completed or incomplete :");
    scanf("%d",&x);
    if((x<ID_Next)&&(x>0))
        {
        done[(x-1)/8]^=(1<<((x-1)%8)); /*toggle the done flag for the wanted id*/
       if( ( (done[(x-1)/8]) & ( 1<< ((x-1)%8) ) ) !=0 ){ printf("Task Marked completed successfully!\n\n");} else {printf("Task Marked incomplete successfully!\n\n");}
        }
    else {printf("The Task ID Does Not Exist !!\n\n");}
   }

 else if(x==5){printf("\nExiting Minions Task Manager. Have a great day!\n"); break;} /*Exit The Loop */

 else         {printf("\nError Enter a valid command !\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Mark Task\n5. Exit\n\n");} /*Error Input*/

}
free(*tasks); /*Free The Dynamic Meomory */
free(done);
return 1;
}
