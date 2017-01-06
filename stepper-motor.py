import os
import glob
import time
from time import strftime
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

FED = 0
mh = Adafruit_MotorHAT(addr = 0x60) #default address for the object is 0x60
myStepper = mh.getStepper(200,1) #200 steps/revolution, motor port #1
myStepper.setSpeed(500)

 
myStepper.step(200, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
myStepper.step(200, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)
mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
