#include <stdio.h>            // Recommended over iostream for saving space
#include <propeller.h>        // Propeller-specific functions
#include <simpletools.h>
#include <time.h>
#include "servo.h"// the motor pulse values are different for normal operation and pushes
#define ut1 12 //left ultrasonic trigger
#define ue1 13 //left ultrasonic echo
#define ut2 10 // center ultrasonic tigger
#define ue2 11 //center ultrasonic echo
#define lm 14 //left motor signal line
#define rm 15 //right motor signal line
#define rpi 13// signal from rpi
#define p1 52 //push 1 push
#define p2 23 //push2 for short push
#define p3 20 //push 3 puss (this puss is only used when reaching A1, i have changed the values to put it after uturn initial value 44)
#define p77 12
#define left 16
#define right 18
#define r1 10
#define r2 12
#define l1 7
#define uturnv 110
#define reversev 53
#define reversevshort 25
#define pidelay 2000 // delay when signal from rpi
#define rishi 17 // was 19 earlier at 18:13
#define fslow 10  // was 75 earlier
#define rslow 15  // 15 og // 8
int inter();
int linloc();
void follower();
void followobs();
int cc();
int cl();
void push();
void puss();
void L90();
void R90();
void SR90();
void uturn();
void reverse();
void reverseshort();
void object(void *parc);
void isec(void *para);
void brake();
void spush();
void party();
unsigned int stack1[40 + 25]; // Stack vars for other cog
unsigned int stack2[40 + 25];
unsigned int stack3[40 + 25];
static volatile int cog, cog2, cog3, intno;

int main()
{
  int haha=1;
  int c=0;
  int l=0;
  int r=0;
  int f=0;
  int dc;
  int dl;
  while(1)
  {  
    int sum=inter();
    if (sum < 17000 && sum > 2500)
    {
      int loc=linloc();
      if (loc == 2 || loc == 3) //if true, robot moves straight
      {
        pulse_out(lm,1390);
        pulse_out(rm,1300);
        pause(rslow);
      }
      else if (loc == 0 || loc == 1) //if true, robot moves left
      {
        pulse_out(rm,1300);
        pause(rslow);
        l++;
      }
      else if (loc == 4 || loc == 5) //if true, robot moves right
      {
        pulse_out(lm,1390);
        pause(rslow);
        r++;
      }
    }
    else if(c==3) 
    {
          cog=cogstart(&isec, NULL, stack2, sizeof(stack2));
  ////////////////////////          
          
          spush();
          dc=cc();
          printf("%d \n",dc);
          if(dc<45)
          {
              intno=2;
              spush();
              followobs();
              uturn();
              reverseshort();
              follower();
              puss();
              R90();           
            }              
          else if(dc>45 && dc<70)
          {
              intno=3;
              spush();
              follower();
              spush();
              followobs();
              uturn();
              reverseshort();
              pause(1000);
              follower();
              spush();
              follower();
              spush();
              R90();
              
            }              
          else if (dc>70)
          {
              intno=5;
              spush();
              follower();
              spush();
              follower();
              spush();
              follower();
              spush();
              followobs();
              uturn();
              reverseshort();
              pause(1000);
              follower();
              spush();
              follower();
              spush();
              follower();
              spush();
              follower();
              spush();
              R90();
             
          }          

          follower(); 
          puss();
          puss();
          SR90();
          pause(1500);
          if(input(rpi))
          {
            pause(pidelay);
          }   
          for(int bint=0;bint<3;bint++)
          {      
            spush();
            follower();
            spush();
            if(input(rpi))
            {
              pause(pidelay);
            }
            pause(100);
            
          } 
          R90();
          spush();
          follower();
          spush();
          //i4
          if(intno!=5)
          {
          L90();
          spush();
          follower();
          spush();
          uturn();
          follower();
          spush();
          pause(50);

          //i4
          pause(50);/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////          
          
          if(intno==2)
          {
          spush();
          follower();
          }          
          puss();
          followobs();
          //obstacle reached
          uturn();
          //uturn done
          if(intno==2)
          {
          follower();
          spush();
          }          
          follower();
          spush();          
          //i4 again
          R90();
          spush();
          }                    
          follower();
          //A4
          puss();
          puss();
          SR90();
          if(input(rpi))
         {
           pause(pidelay);
         }
           for(int aint=0;aint<3;aint++)
          {      
            spush();
            follower();
            spush();
            if(input(rpi))
            {
              pause(pidelay);
            }
            pause(100);
            
           
          } 
          //A1
          spush();
          R90();
          spush();
          pause(25);
          follower();
          spush();
          follower();
          //B1
          spush();
          R90();
          for(int aint=0;aint<4;aint++)
          {      
            spush();
            follower();
            spush();
           
          }
          //B5
          if(input(rpi))
          {
            pause(pidelay);
          }
          party();
          break;
              
    }      
    else if(c==2)
    {
      cog=cogstart(&isec, NULL, stack2, sizeof(stack2));
      c++;
      spush();
    }      
    else if(c==1 && f==0) //special intersection ignorance case
    {
      printf("c=1\n");
      if(l>r)
      {
        for(int x=0;x<=rishi;x++)
        {
           pulse_out(rm,400);
           pause(rslow); //not sure if this should be slow or change it back to 9
         }
         f=1;
       }         
      else
      {
       for(int x=0;x<=rishi;x++)
        {
           pulse_out(lm,2300);
           pause(rslow);
         }
         f=1;
       }
       c++; 
     } 
    
                         
    else if(c==0)
    {
      c++;
      pause(10);
    }                    
  }
}




//------------functions-------------------
int inter()
{
  int pins[6]={8,7,6,5,4,3};  
  for(int i=0;i<6;i++)
  {
    set_direction(pins[i],1);
  }
  int times[6];
  for(int i=0;i<6;i++)
  {
    high(pins[i]);
    pause(1);
    set_direction(pins[i],0);
    times[i]=rc_time(pins[i],1);
  }
  int s = 0;
  for (int i = 0; i < 6; i++)
  {
    s += times[i];
  }
  return s;
}  


int linloc()
{
  int pins[6]={8,7,6,5,4,3};  
  for(int i=0;i<6;i++)
  {
    set_direction(pins[i],1);
  }
  int times[6];
  for(int i=0;i<6;i++)
  {
    high(pins[i]);
    pause(1);
    set_direction(pins[i],0);
    times[i]=rc_time(pins[i],1);
  }
  int bleh = 0;
  int maxind;
  for (int i = 0; i < 6; i++)
  {
    if (times[i] > bleh)
    {
      bleh = times[i];

      maxind = i;
    }
  }
  return maxind;
}  

void follower()
{ 
  int sum=0;
  sum=inter();
  while(sum < 17500 && sum > 2000)
  {
      if(input(rpi))
      {
        pause(pidelay);
      }
      int loc=linloc();
      if (loc == 2 || loc == 3) //if true, robot moves straight
      {
        pulse_out(lm,1390);
        pulse_out(rm,1300);
        pause(fslow);
      }
      else if (loc == 0 || loc == 1) //if true, robot moves left
      {

        pulse_out(rm,1300);
        pause(fslow);
      }
      else if (loc == 4 || loc == 5) //if true, robot moves right
      {
        pulse_out(lm,1390);
        pause(fslow);
      }
      sum=inter();
    }
     high(0);
     pause(500);
     low(0);
}    
void followobs()
{ 
  int cdist=0;
  cdist=cc();
  while(cdist>2)
  {
      if(input(rpi))
      {
        pause(pidelay);
      }        
      int loc=linloc();
      if (loc == 2 || loc == 3) //if true, robot moves straight
      {
        pulse_out(lm,1390);
        pulse_out(rm,1300);
        pause(fslow);
      }
      else if (loc == 0 || loc == 1) //if true, robot moves left
      {
        pulse_out(rm,1300);
        pause(fslow);
      }
      else if (loc == 4 || loc == 5) //if true, robot moves right
      {
        pulse_out(lm,1390);
        pause(fslow);
      }
      cdist=cc();
    }
    
}    
//------------------ultrasonic----------------
int cl()
{         
          brake();
          low(ut1);
          pause(2);
          high(ut1);
          pause(10);
          low(ut1);
          int duration1 = pulse_in(ue1, 1);
          int dl = (duration1 * 0.0343) / 2;
          return dl;
        }          
int cc()
{     low(ut2);
      pause(2);
      high(ut2);
      pause(10);
      low(ut2);
      int duration2 = pulse_in(ue2, 1);
      int dc = (duration2 * 0.0343) / 2;
      return dc;
    }     
void push()
{
           for(int x=0;x<=p1;x++)
          {
             pulse_out(rm,1290);
             pulse_out(lm,1450);
             pause(10);
           }
         }            
void puss()
{
          for(int x=0;x<=p3;x++)
          {
             pulse_out(rm,400);
             pulse_out(lm,2300);
             pause(5);
           }
         } 
void spuss()
{
          for(int x=0;x<=p77;x++)
          {
             pulse_out(rm,400);
             pulse_out(lm,2300);
             pause(5);
           }
         }           
void L90()
{         for(int x=0;x<=left;x++)
            {
             pulse_out(rm,900);
             pulse_out(lm,900);
             pause(30);
            }
}            

void R90()
{         for(int x=0;x<=right;x++)
            {
             pulse_out(rm,1600);
             pulse_out(lm,1600);
             pause(30);
            }
} 
void SR90()
{           
            for(int x=0;x<=55;x++)
            {
             pulse_out(rm,1380);
             pulse_out(lm,1380);
             pause(40);
            }
            
} 
void uturn()
{         for(int x=0;x<=uturnv;x++)
            {
             pulse_out(rm,1380);
             pulse_out(lm,1380);
             pause(30);
            }
} 
void reverse()
{
  for(int x=0;x<=reversev;x++)
            {
             pulse_out(lm,1300);
             pulse_out(rm,1390);
             pause(10);
            }
}
void reverseshort()
{
  for(int x=0;x<=reversevshort;x++)
            {
             pulse_out(lm,1300);
             pulse_out(rm,1390);
             pause(10);
            }
}
void brake()
{
   pulse_out(rm,1350);
   pulse_out(lm,1350); 
 }          
void object(void *parc)
{
  pause(25);
  high(2);
  pause(500);
  low(2);
  cogstop(cog3);
}
void isec(void *para)
{
high(0);
pause(500);
low(0);
cogstop(cog);
}

void party()
{
  high(2);
  pause(500);
  low(2);
  high(1);
  pause(500);
  low(1);
  high(2);
  pause(500);
  low(2);
  high(1);
  pause(500);
  low(1);
  high(2);
  pause(500);
  low(2);
  high(1);
  pause(500);
  low(1);
}  

void spush()
{
          for(int x=0;x<=p2;x++)
          {
             pulse_out(rm,1280);
             pulse_out(lm,1450);
             pause(10);
           }
         }  
         