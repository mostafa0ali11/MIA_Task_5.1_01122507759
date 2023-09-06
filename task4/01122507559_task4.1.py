#Author:Moustafa Ezzeldeen
#Battle Field !!
#Simple Battle Between Gru and Vector

import random

class Villain:
 # Class init function and no needed paramaters from user
 def __init__(self):
  self.__Health=100
  self.__Energy=500
  self.__Shield=0.00

 #Methods to get and edit Health,Energy and Shield
 def GetEnergy(self):
  return(self.__Energy)

 def SetEnergy(self,Cost):
  self.__Energy-=Cost

 def GetShield(self):
  return(self.__Shield)

 def SetShield(self,Save):
  self.__Shield=Save

 def GetHealth(self):
  return(self.__Health)

 def SetHealth(self,Damage):
  self.__Health-=Damage*(1-self.__Shield)

 #Reset and Status Methods
 def reset(self):
  self.__Health=100
  self.__Energy=500
  self.__Shield=0.00

 def status(self):
  print(f"{self.__class__.__name__}_Health:{self.GetHealth()} {self.__class__.__name__}_Energy:{self.GetEnergy()} {self.__class__.__name__}_Sheild:{100*self.GetShield()}%")

#Gru Gadgets class
class Gru (Villain):
 #All Gru Gadgets Data will be saved in 2D List to make it easier to access in loops

 #List Format [0-Weapone or Shield Name,1-Energy Cost,2-Damage or Shield Percentage,3-Stock(Used-1 to descripe ∞),4-Descrption]
 Describe_List= [["Freeze Gun",50,11,-1,"Minions occasionally wield freeze ray guns that shoot a freezing beam to immobilize opponents temporarily."],
                 ["Electric Prod",88,18,5,"Minions might use electric prods to deliver mild shocks to enemies, stunning them momentarily."],
                 ["Mega Magnet",92,10,3,"Minions utilize a mega magnet to attract or repel metal objects, potentially disrupting enemy vehicles or equipment.(reduce 20'%' of next opponet attack)"],
                 ["Kalman Missile",120,20,1,"This unavoidable Missile created for  enourmous distraction.(Enemy Shield will not Work)"],
                 ["Energy-Projected BarrierGun",20,0.40,-1,"The spaceship's shields create an invisible, energy-projected barrier around the vehicle. This barrier absorbs and dissipates energy based attacks such as lasers, beams, and plasma shots."],
                 ["Selective Permeability",50,0.90,2,"The shields can be programmed to allow certain objects, signals, or energies to pass through while blocking others. This can be useful for communication or specific tactical maneuvers."]]
 #Weapons and Shields Orders are like Methods Order
 
 def Turn(self,R,Enemy):#R for Row Enemy for Player2
   if self.Describe_List[R][3] and R<=5 and R>=0: #Check Stock (-1 will make true,0 will make false) 

    if R<4:#Check Gadgets is a weapon or shield
     
     if R==3: #Check the weapon is The KALMAN MISSILE or not
      Enemy.SetShield(0) #Kalman Special Ability
   
     elif R==2: #Check the weapon is The Mega Magnet or not
      self.SetShield(0.20) #Mega Magnet Special Ability

     Enemy.SetHealth(self.Describe_List[R][2])#Attack !
     Enemy.SetShield(0)#Set Enemy Defence to 0!

    else: #Shield
     self.SetShield(self.Describe_List[R][2])#Defense !
    
    self.SetEnergy(self.Describe_List[R][1])#Decrease Energy
    self.Describe_List[R][3]-=1 #Decrease Stock

    return 0 #we will use it in aloop
   
   else:
    return 1

 #Vector Gadgets class   
class Vector (Villain):
 #All Vector Gadgets Data will be saved in 2D List to make it easier to access in loops

 #List Format [0-Weapone or Shield Name,1-Energy Cost,2-Damage or Shield Percentage,3-Stock(Used-1 to descripe ∞),4-Descrption]
 Describe_List= [["Laser Blasters",40,8,-1,"Vector's primary weapon would be powerful laser blasters attached to his flying pod. These blasters emit focused energy beams that can slice through obstacles and damage enemy vehicles."],
                 ["Plasma Grenades",56,13,8,"Vector could use plasma grenades that  explode on impact, releasing fiery  energy bursts that deal significant  damage to enemy vehicles caught in the  blast radius."],
                 ["Sonic Resonance Cannon",100,22,3,"Fires powerful sonic waves that can shatter enemy shields and disrupt their systems, temporarily incapacitating them."],
                 ["Energy Net Trap",15,0.32,-1,"Vector's pod might have the ability to deploy an energy net that ensnares enemy vehicles, temporarily immobilizing them and leaving them vulnerable to Vector's other attacks."],
                 ["Quantum Deflector",40,0.80,3,"Manipulates quantum states to create a deflection field, causing enemy projectiles to miss the spaceship by a slight margin in the quantum realm."]]
 #Weapons and Shields Orders are like Methods Order

 def Turn(self,R,Enemy): #R for Row Enemy for Player1
   if self.Describe_List[R][3] and R<=4 and R>=0: #Check Stock (-1 will make true,0 will make false) 

    if R<3:#Check Gadgets is a weapon or shield

     Enemy.SetHealth(self.Describe_List[R][2])#Attack !
     Enemy.SetShield(0)#Set Enemy Defence to 0!

    else: #Shield
     self.SetShield(self.Describe_List[R][2])#Defense !
    
    self.SetEnergy(self.Describe_List[R][1])#Decrease Energy
    self.Describe_List[R][3]-=1 #Decrease Stock

    return 0 #we will use it in aloop
   
   else:
    return 1

def Restart(): #Restart LOOP
   X=0
   while X<=0 or X>2:
    X=input("Enter 1.to Restart The Game or 2.to Exsit! :")
    X=int(X)

   if X==1:
    return 0 #Mode
   if X==2:
    return 5 #Mode
    


def Items_Status(Player,Max_Gadgets): #Print items Functions
 for R in range(Max_Gadgets):
  if Player.Describe_List[R][2]>1: #check the type for perfect print
   Gadget_Status="Damage"
   persent=1
  else:
   Gadget_Status="Shield"
   persent=100
  if Player.Describe_List[R][3]<0: #to make -1 = ∞
   stock="∞"
  else: 
   stock=Player.Describe_List[R][3]
  
  print(f"\n{R+1}.{Player.Describe_List[R][0]} {Gadget_Status}={Player.Describe_List[R][2]*persent} Stock={stock} Energy_Cost={Player.Describe_List[R][1]}\nDescrption:{Player.Describe_List[R][4]}")
 print(f"\n{Max_Gadgets+1}.Pass the turn(Must use When you Haven't Enough Energy)")



Mode=0
Player1=Gru()
Player2=Vector()

#int main(void){ /*The main code*/ 

while 1: #Game Loop
 
 if Mode==5: #EXist The Game after finished battle
  break
 
 #Reset for in case of restart the game
 Player1.Describe_List=[["Freeze Gun",50,11,-1,"Minions occasionally wield freeze ray guns that shoot a freezing beam to immobilize opponents temporarily."],["Electric Prod",88,18,5,"Minions might use electric prods to deliver mild shocks to enemies, stunning them momentarily."],["Mega Magnet",92,10,3,"Minions utilize a mega magnet to attract or repel metal objects, potentially disrupting enemy vehicles or equipment.(reduce 20'%' of next opponet attack)"],["Kalman Missile",120,20,1,"This unavoidable Missile created for  enourmous distraction.(Enemy Shield will not Work)"],["Energy-Projected BarrierGun",20,0.40,-1,"The spaceship's shields create an invisible, energy-projected barrier around the vehicle. This barrier absorbs and dissipates energy based attacks such as lasers, beams, and plasma shots."],["Selective Permeability",50,0.90,2,"The shields can be programmed to allow certain objects, signals, or energies to pass through while blocking others. This can be useful for communication or specific tactical maneuvers."]]
 Player2.Describe_List=[["Laser Blasters",40,8,-1,"Vector's primary weapon would be powerful laser blasters attached to his flying pod. These blasters emit focused energy beams that can slice through obstacles and damage enemy vehicles."],["Plasma Grenades",56,13,8,"Vector could use plasma grenades that  explode on impact, releasing fiery  energy bursts that deal significant  damage to enemy vehicles caught in the  blast radius."],["Sonic Resonance Cannon",100,22,3,"Fires powerful sonic waves that can shatter enemy shields and disrupt their systems, temporarily incapacitating them."],["Energy Net Trap",15,0.32,-1,"Vector's pod might have the ability to deploy an energy net that ensnares enemy vehicles, temporarily immobilizing them and leaving them vulnerable to Vector's other attacks."],["Quantum Deflector",40,0.80,3,"Manipulates quantum states to create a deflection field, causing enemy projectiles to miss the spaceship by a slight margin in the quantum realm."]]
 Player1.reset()
 Player2.reset()

 turn=random.randint(0,1) #Make the first turn in the game random ODD for Gru Even for Vector
 RoundsNo=1

 print("\nWelcome To The Game !")

 while Mode<=0 or Mode>4: #Mode Selector Loop
  print("\nPlease Select A Mode\n1.Gru(Human) VS Vector(Human)\n2.Gru(Human) VS Vector(AI)\n3.Gru(AI) vs Vector(Human)\n4.Gru(AI) vs Vector(AI) (Spectator Mode)\n5.Exist!")
  Mode=input()
  Mode=int(Mode)
 if Mode==5: #EXist The Game
  break
 
 print("\nWelcome To The Battle !")
 while 1: #Battle Loop
  
  if turn>1: #One Round Every 2 turns
   RoundsNo+=1 
   
  print(f"\nThe Round Number:{RoundsNo}\n") #Status
  print("Player1 Status:")
  Player1.status()
  print("")
  print("Player2 Status:")
  Player2.status()
  

  if turn%2==1: #Gru turn
   print("\nGru's Turn")

   Items_Status(Player1,6) #Print Gru Gadegts to choose from

   X=0
   while X<=0 or X>7: #Gru Gadegts Select Loop if the player enter a Gadegt Number for empty stock or no energy The program will ask him to enter the number again 
    
    if Mode==1 or Mode==2: #Human Mode Check
     X=input("\nEnter Your Gadegt Number:")
     X=int(X)
    
    else: #AI Mode Check
     X=random.randint(1,7)

    if X>6: #Protect Program from Error
     pass #continue in loop without going to Stock and energy check

    elif Player1.Describe_List[X-1][3]==0: #Stock check
     print("You Don't Have this item !")
     X=0 #continue in loop

    elif (Player1.GetEnergy()-Player1.Describe_List[X-1][1]) <0: #Energy check
     print("You Don't Have enough energy for this item !")
     X=0 #continue in loop

   if X==7: #Pass Check
    print("\nGru Have Passed The Turn !")
   
   else:
    Player1.Turn(X-1,Player2) #The Turn from methods in the Class
    print(f"\nGru Have Played The {Player1.Describe_List[X-1][0]} !")


   if Player2.GetHealth()<=0: #Check Game Over
    print("\nGAME IS OVER !! GRU WIN THE BATTLE.\n")
    Mode=Restart() #Restart Function
    break
   
   elif (Player1.GetEnergy()<20) and (Player2.GetEnergy()<15): #Check Game Draw
    print("\nThe game is over drawn. Nobody won !!\n")
    Mode=Restart() #Restart Function
    break
 
   turn+=1 #Next turn


  print(f"\nThe Round Number:{RoundsNo}\n") #Status
  print("Player1 Status:")
  Player1.status()
  print("")
  print("Player2 Status:")
  Player2.status()


  if turn%2==0: #Vector turn
   
   print("\nVector's Turn")

   Items_Status(Player2,5) #Print Vector Gadegts to choose from

   X=0
   while X<=0 or X>6: #Vector Gadegts Select Loop if the player enter a Gadegt Number for empty stock or no energy The program will ask him to enter the number again 
    
    if Mode==1 or Mode==3: #Human Mode Check
     X=input("\nEnter Your Gadegt Number:")
     X=int(X)
    
    else: #AI Mode Check
     X=random.randint(1,6)

    if X>5: #Protect Program from Error
     pass #continue in loop without going to Stock and energy check

    elif Player2.Describe_List[X-1][3]==0: #Stock check
     print("You Don't Have this item !")
     X=0 #continue in loop

    elif (Player2.GetEnergy()-Player2.Describe_List[X-1][1]) <0: #Energy check
     print("You Don't Have enough energy for this item !")
     X=0 #continue in loop

   if X==6: #Pass Check
    print("\nVector Have Passed The Turn !")
   
   else:
    Player2.Turn(X-1,Player1) #The Turn from methods in the Class
    print(f"\nVector Have Played The {Player2.Describe_List[X-1][0]} !")

   if Player1.GetHealth()<=0: #Check Game Over
    print("\nGAME IS OVER !! Vector WIN THE BATTLE.\n")
    Mode=Restart() #Restart Function
    break
   
   elif (Player1.GetEnergy()<20) and (Player2.GetEnergy()<15): #Check Game Draw
    print("\nThe game is over drawn. Nobody won !!\n")
    Mode=Restart() #Restart Function
    break
   
   turn+=1 #Next turn