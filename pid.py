# Simple PID Implementation to help control temprature in brewery applications
# 2016 Gabriel Jaquish
# Norithern Harvest Brewing Company
# http://www.northernharvest.beer/
#
# All Tempratures are in Degrees Kelvin to prevent negitive values

import os
import glob
import time

#Initalize DS18B20 Temprature Probes, if not already
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

#Define proportional, integral, & derivative gains
var k_p = 
var k_i = 
var k_d =

#Other Variables used within teh PID Equation
var SetPoint, CurrentError, LastError, CurrentTemp, LastTemp


#Find the Current Error (Pos or Neg)
CurrentError = SetPoint - read_temp()

def PID:
  
#Main PID Control Loop
while True:
  PID(





#Modified From Adafruit Temp Probe Implmenentation
#https://cdn-learn.adafruit.com/downloads/pdf/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing.pdf

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp():
  #Open the Probe File
  f = open(device_file, 'r')
  lines = f.readlines()
  f.close()
  equals_pos = lines[1].find('t=')
  if equals_pos != -1:
    temp_string = lines[1][equals_pos+2:]
    #Convert to Degrees Kelvin and return
    return (float(temp_string)/1000) + 273.15

def read_temp():
  lines = read_temp_raw()
  while lines[0].strip()[-3:] != 'YES':
  time.sleep(0.2)
  lines = read_temp_raw()
  equals_pos = lines[1].find('t=')
  
  temp_c = float(temp_string) / 1000.0
  temp_f = temp_c * 9.0 / 5.0 + 32.0
  return temp_c, temp_f

while True:
  print(read_temp())
  time.sleep(1)
