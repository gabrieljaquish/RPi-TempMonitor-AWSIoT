#Fermentaion Temprature Monitor
##What is it for?
This lightweight piece of code is being developed to help remotely monitor the tempratures of fermentation vessels.  
It is designed for use on a [Raspberry Pi 3](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/) running [Raspbian JESSIE](https://www.raspbian.org/)

## What Does it do?
- Publish Temprature Data to [Amazon IoT](https://aws.amazon.com/iot/) via [MQTT](http://mqtt.org/)
- Subscribe to control Topics from [Amazon IoT](https://aws.amazon.com/iot/) using [MQTT](http://mqtt.org/)

## Hardware
- [Raspberry Pi 3](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)
- [DS1820] (http://www.systronix.com/Resource/ds1820.pdf) 1–Wire&trade; Digital Thermometer
- Custom PCB hat providing simple plug and play setup of one or more DS1820 with built in 4.7K&#8486; Pull up resistor

## Software
- [Raspbian Jessie](https://www.raspbian.org/) - Raspberry Pi OS
- [Node.JS](https://nodejs.org/) & [Node Package Manager](https://www.npmjs.com/) - General Frameworks used
- [AWS IoT SDK for JavaScript](https://github.com/aws/aws-iot-device-sdk-js) - AWS Package to help connect node.js applications to AWS IoT
- [ds18x20.js](https://github.com/mraxus/ds18x20.js) - Raspberry Pi Specific node.js DS1820 temprature probe reading
