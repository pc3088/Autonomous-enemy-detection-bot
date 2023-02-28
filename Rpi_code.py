import cv2
import cv2.aruco as aruco
import RPi.GPIO as GPIO
import time
import numpy as np
from gpiozero import Servo
import pigpio
from time import sleep
pi = pigpio.pi()
servo=18 #pin 12
LedPinE=4  #pin7
LedPinF=17 #pin 11
commpin=27 #pin 13
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(servo,GPIO.OUT)
GPIO.setup(LedPinE,GPIO.OUT)
GPIO.setup(LedPinF,GPIO.OUT)
GPIO.setup(commpin, GPIO.OUT)
#servo = Servo(ServoPin)

cap = cv2.VideoCapture(0)
delay = 1
count0=1
count1=1
count2=1
count3=1
count4=1
count5=1
count6=1
count7=1
count8=1
count9=1

count10=1
count11=1
count12=1
count13=1
count14=1
count15=1
count16=1
count17=1
count18=1
count19=1

def Aruco(img, markersize = 6, total = 250, draw = True):
	key = getattr(aruco, f'DICT_{markersize}X{markersize}_{total}')
	#grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	Dictionary = aruco.Dictionary_get(key)
	Para = aruco.DetectorParameters_create()
	bbox, ids,_ = aruco.detectMarkers(img, Dictionary, parameters = Para)
#	print(ids)

	if draw:
		aruco.drawDetectedMarkers(img, bbox)
	return bbox, ids

#def ServoMove(ServoAngle):
#  sleep(1)
#  PulseWidth = 0
#  PulseWidth=ServoAngle*9.72+500 #OnTime for PWM
#  PulseWidth=PulseWidth/1000000
#  for indx in range(0,2):
#     GPIO.output(ServoPin, 1)
#     sleep(PulseWidth)
#     GPIO.output(ServoPin, 0)
#     sleep(0.02)

pwm = pigpio.pi() 
pwm.set_mode(servo, pigpio.OUTPUT)
 
pwm.set_PWM_frequency( servo, 50 )

def roi(img):
	height = img.shape[0]
	width = img.shape[1]
	grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	ROI = np.array([[(120,height),(120,180),(500,180),(500,height)]], dtype=np.int32)
	black = np.zeros_like(grey_img)
	roi = cv2.fillPoly(black, ROI, 255)
	roi_img = cv2.bitwise_and(grey_img,roi)
	return roi_img
#sleep(0.5)
#servo.max()
GPIO.output(LedPinE,GPIO.LOW)
GPIO.output(LedPinF,GPIO.LOW)
#servo.max()
while True:
  GPIO.output(LedPinE,GPIO.LOW)
  ret, img = cap.read()
  grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  bbox, ids = Aruco(grey_img)
  if cv2.waitKey(1) == 113:
    break
  cv2.imshow('Halal4Lyf',grey_img)
  id=int(ids or 69)
  print(id)
  if id==10 and count10<2:
       GPIO.output(commpin, GPIO.HIGH)
       sleep(0.5)
       GPIO.output(commpin, GPIO.LOW)
       GPIO.output(LedPinE,GPIO.HIGH)
       pwm.set_servo_pulsewidth( servo, 500 ) ;
       time.sleep( 3 )
       GPIO.output(LedPinE,GPIO.LOW)
       pwm.set_servo_pulsewidth( servo, 2500 ) ;
       time.sleep( 3 )
       pwm.set_PWM_dutycycle(servo, 0)
       pwm.set_PWM_frequency( servo, 0 )
       sleep(0.2)   
       count10 = 2
  elif id==11 and count11<2:
       GPIO.output(commpin, GPIO.HIGH)
       sleep(0.5)
       GPIO.output(commpin, GPIO.LOW)
       GPIO.output(LedPinE,GPIO.HIGH)
       pwm.set_servo_pulsewidth( servo, 500 ) ;
       time.sleep( 3 )
       GPIO.output(LedPinE,GPIO.LOW)
       pwm.set_servo_pulsewidth( servo, 2500 ) ;
       time.sleep( 3 )
       pwm.set_PWM_dutycycle(servo, 0)
       pwm.set_PWM_frequency( servo, 0 )
       sleep(0.2)   
       count11 = 2  
  elif id==12 and count12<2:
       GPIO.output(commpin, GPIO.HIGH)
       sleep(0.5)
       GPIO.output(commpin, GPIO.LOW)
       GPIO.output(LedPinE,GPIO.HIGH)
       pwm.set_servo_pulsewidth( servo, 500 ) ;
       time.sleep( 3 )
       GPIO.output(LedPinE,GPIO.LOW)
       pwm.set_servo_pulsewidth( servo, 2500 ) ;
       time.sleep( 3 )
       pwm.set_PWM_dutycycle(servo, 0)
       pwm.set_PWM_frequency( servo, 0 )
       sleep(0.2)   
       count12 = 2  
  elif id==13 and count13<2:
       GPIO.output(commpin, GPIO.HIGH)
       sleep(0.5)
       GPIO.output(commpin, GPIO.LOW)
       GPIO.output(LedPinE,GPIO.HIGH)
       pwm.set_servo_pulsewidth( servo, 500 ) ;
       time.sleep( 3 )
       GPIO.output(LedPinE,GPIO.LOW)
       pwm.set_servo_pulsewidth( servo, 2500 ) ;
       time.sleep( 3 )
       pwm.set_PWM_dutycycle(servo, 0)
       pwm.set_PWM_frequency( servo, 0 )
       sleep(0.2)   
       count13 = 2  
  elif id==14 and count14<2:
       GPIO.output(commpin, GPIO.HIGH)
       sleep(0.5)
       GPIO.output(commpin, GPIO.LOW)
       GPIO.output(LedPinE,GPIO.HIGH)
       pwm.set_servo_pulsewidth( servo, 500 ) ;
       time.sleep( 3 )
       GPIO.output(LedPinE,GPIO.LOW)
       pwm.set_servo_pulsewidth( servo, 2500 ) ;
       time.sleep( 3 )
       pwm.set_PWM_dutycycle(servo, 0)
       pwm.set_PWM_frequency( servo, 0 )
       sleep(0.2)  
       count14 = 2  
  elif id==15 and count15<2:
       GPIO.output(commpin, GPIO.HIGH)
       sleep(0.5)
       GPIO.output(commpin, GPIO.LOW)
       GPIO.output(LedPinE,GPIO.HIGH)
       pwm.set_servo_pulsewidth( servo, 500 ) ;
       time.sleep( 3 )
       GPIO.output(LedPinE,GPIO.LOW)
       pwm.set_servo_pulsewidth( servo, 2500 ) ;
       time.sleep( 3 )
       pwm.set_PWM_dutycycle(servo, 0)
       pwm.set_PWM_frequency( servo, 0 )
       sleep(0.2)   
       count15 = 2  
  elif id==16 and count16<2:
       GPIO.output(commpin, GPIO.HIGH)
       sleep(0.5)
       GPIO.output(commpin, GPIO.LOW)
       GPIO.output(LedPinE,GPIO.HIGH)
       pwm.set_servo_pulsewidth( servo, 500 ) ;
       time.sleep( 3 )
       GPIO.output(LedPinE,GPIO.LOW)
       pwm.set_servo_pulsewidth( servo, 2500 ) ;
       time.sleep( 3 )
       pwm.set_PWM_dutycycle(servo, 0)
       pwm.set_PWM_frequency( servo, 0 )
       sleep(0.2)   
       count16 = 2  
  elif id==17 and count17<2:
       GPIO.output(commpin, GPIO.HIGH)
       sleep(0.5)
       GPIO.output(commpin, GPIO.LOW)
       GPIO.output(LedPinE,GPIO.HIGH)
       pwm.set_servo_pulsewidth( servo, 500 ) ;
       time.sleep( 3 )
       GPIO.output(LedPinE,GPIO.LOW)
       pwm.set_servo_pulsewidth( servo, 2500 ) ;
       time.sleep( 3 )
       pwm.set_PWM_dutycycle(servo, 0)
       pwm.set_PWM_frequency( servo, 0 )
       sleep(0.2)  
       count17 = 2  
  elif id==18 and count18<2:
       GPIO.output(commpin, GPIO.HIGH)
       sleep(0.5)
       GPIO.output(commpin, GPIO.LOW)
       GPIO.output(LedPinE,GPIO.HIGH)
       pwm.set_servo_pulsewidth( servo, 500 ) ;
       time.sleep( 3 )
       GPIO.output(LedPinE,GPIO.LOW)
       pwm.set_servo_pulsewidth( servo, 2500 ) ;
       time.sleep( 3 )
       pwm.set_PWM_dutycycle(servo, 0)
       pwm.set_PWM_frequency( servo, 0 )
       sleep(0.2) 
       count18 = 2  
  elif id==19 and count19<2:
       GPIO.output(commpin, GPIO.HIGH)
       sleep(0.5)
       GPIO.output(commpin, GPIO.LOW)
       GPIO.output(LedPinE,GPIO.HIGH)
       pwm.set_servo_pulsewidth( servo, 500 ) ;
       time.sleep( 3 )
       GPIO.output(LedPinE,GPIO.LOW)
       pwm.set_servo_pulsewidth( servo, 2500 ) ;
       time.sleep( 3 )
       pwm.set_PWM_dutycycle(servo, 0)
       pwm.set_PWM_frequency( servo, 0 )
       sleep(0.2)   
       count19 = 2  
 ########################################### from 0 to 9 
  elif id==0 and count0<2:
       GPIO.output(commpin, GPIO.HIGH)
       sleep(0.5)
       GPIO.output(commpin, GPIO.LOW)
       GPIO.output(LedPinF,GPIO.HIGH)
       start = time.time()
       while time.time() - start < delay:
              pass
       GPIO.output(LedPinF,GPIO.LOW)  
       count0 = 2  
  elif id==1 and count1<2:
       GPIO.output(commpin, GPIO.HIGH)
       sleep(0.5)
       GPIO.output(commpin, GPIO.LOW)
       GPIO.output(LedPinF,GPIO.HIGH)
       start = time.time()
       while time.time() - start < delay:
              pass
       GPIO.output(LedPinF,GPIO.LOW)  
       count1 = 2  
  elif id==2 and count2<2:
       GPIO.output(commpin, GPIO.HIGH)
       sleep(0.5)
       GPIO.output(commpin, GPIO.LOW)
       GPIO.output(LedPinF,GPIO.HIGH)
       start = time.time()
       while time.time() - start < delay:
              pass
       GPIO.output(LedPinF,GPIO.LOW)  
       count2 = 2  
  elif id==3 and count3<2:
       GPIO.output(commpin, GPIO.HIGH)
       sleep(0.5)
       GPIO.output(commpin, GPIO.LOW)
       GPIO.output(LedPinF,GPIO.HIGH)
       start = time.time()
       while time.time() - start < delay:
              pass
       GPIO.output(LedPinF,GPIO.LOW)  
       count3 = 2  
  elif id==4 and count4<2:
       GPIO.output(commpin, GPIO.HIGH)
       sleep(0.5)
       GPIO.output(commpin, GPIO.LOW)
       GPIO.output(LedPinF,GPIO.HIGH)
       start = time.time()
       while time.time() - start < delay:
              pass
       GPIO.output(LedPinF,GPIO.LOW)  
       count4 = 2  
  elif id==5 and count5<2:
       GPIO.output(commpin, GPIO.HIGH)
       sleep(0.5)
       GPIO.output(commpin, GPIO.LOW)
       GPIO.output(LedPinF,GPIO.HIGH)
       start = time.time()
       while time.time() - start < delay:
              pass
       GPIO.output(LedPinF,GPIO.LOW)  
       count5 = 2  
  elif id==6 and count6<2:
       GPIO.output(commpin, GPIO.HIGH)
       sleep(0.5)
       GPIO.output(commpin, GPIO.LOW)
       GPIO.output(LedPinF,GPIO.HIGH)
       start = time.time()
       while time.time() - start < delay:
              pass
       GPIO.output(LedPinF,GPIO.LOW)  
       count6 = 2  
  elif id==7 and count7<2:
       GPIO.output(commpin, GPIO.HIGH)
       sleep(0.5)
       GPIO.output(commpin, GPIO.LOW)
       GPIO.output(LedPinF,GPIO.HIGH)
       start = time.time()
       while time.time() - start < delay:
              pass
       GPIO.output(LedPinF,GPIO.LOW)  
       count7 = 2  
  elif id==8 and count8<2:
       GPIO.output(commpin, GPIO.HIGH)
       sleep(0.5)
       GPIO.output(commpin, GPIO.LOW)
       GPIO.output(LedPinF,GPIO.HIGH)
       start = time.time()
       while time.time() - start < delay:
              pass
       GPIO.output(LedPinF,GPIO.LOW)  
       count8 = 2  
  elif id==9 and count9<2:
       GPIO.output(commpin, GPIO.HIGH)
       sleep(0.5)
       GPIO.output(commpin, GPIO.LOW)
       GPIO.output(LedPinF,GPIO.HIGH)
       start = time.time()
       while time.time() - start < delay:
              pass
       GPIO.output(LedPinF,GPIO.LOW)  
       count9 = 2  
