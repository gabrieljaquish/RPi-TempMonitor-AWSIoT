var tempSensor = require('ds18x20');
var awsIot = require('aws-iot-device-sdk');

var isLoaded = tempSensor.isDriverLoaded();

//Check if the DS18x20 Driver is loaded
if (isLoaded);
{
  console.log("Driver Loaded");
  
  //List Devices Plugged Into This Pi
  sensor.list(function (err, listOfDeviceIds) {
    console.log(listOfDeviceIds);
  });

  while()
  {
    tempSensor.getAll(function (err, tempObj) {
        console.log(tempObj);
    });
  }
  
}

else
{
  console.log("Unable to Load DS1820 Driver/nPlease Run sudo modprobe w1-gpio && sudo modprobe w1-therm");
}


var device = awsIot.device({
   keyPath: <YourPrivateKeyPath>,
  certPath: <YourCertificatePath>,
    caPath: <YourRootCACertificatePath>,
  clientId: <YourUniqueClientIdentifier>,
    region: <YourAWSRegion>
});

//
// Device is an instance returned by mqtt.Client(), see mqtt.js for full
// documentation.
//
device
  .on('connect', function() {
    console.log('connect');
    device.subscribe('topic_1');
    device.publish('topic_2', JSON.stringify({ test_data: 1}));
    });

device
  .on('message', function(topic, payload) {
    console.log('message', topic, payload.toString());
  });
