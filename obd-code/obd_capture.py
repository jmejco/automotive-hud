#!/usr/bin/env python

import obd_io
import serial
import platform
import obd_sensors
from datetime import datetime
import time

from obd_utils import scanSerial

class OBD_Capture():
    def __init__(self):
        self.port = None
        localtime = time.localtime(time.time())

    def connect(self):
        portnames = scanSerial()
        print portnames
        for port in portnames:
            self.port = obd_io.OBDPort(port, None, 2, 2)
            if(self.port.State == 0):
                self.port.close()
                self.port = None
            else:
                break

        if(self.port):
            print "Connected to "+self.port.port.name
            
    def is_connected(self):
        return self.port
        
    def capture_data(self):

        #Find supported sensors - by getting PIDs from OBD
        # its a string of binary 01010101010101 
        # 1 means the sensor is supported
        self.supp = self.port.sensor(0)[1]
        self.supportedSensorList = []
        self.unsupportedSensorList = []

        # loop through PIDs binary
        for i in range(0, len(self.supp)):
            if self.supp[i] == "1":
                # store index of sensor and sensor object
                self.supportedSensorList.append([i+1, obd_sensors.SENSORS[i+1]])
            else:
                self.unsupportedSensorList.append([i+1, obd_sensors.SENSORS[i+1]])
        
        for supportedSensor in self.supportedSensorList:
            print "supported sensor index = " + str(supportedSensor[0]) + " " + str(supportedSensor[1].shortname)        
        
        time.sleep(3)
        
        if(self.port is None):
            return None

        #Loop until Ctrl C is pressed        
        try:
            while True:
                localtime = datetime.now()
                current_time = str(localtime.hour)+":"+str(localtime.minute)+":"+str(localtime.second)+"."+str(localtime.microsecond)
                log_string = current_time + "\n"
                results = {}
                for supportedSensor in self.supportedSensorList:
                    sensorIndex = supportedSensor[0]
                    (name, value, unit) = self.port.sensor(sensorIndex)
                    if sensorIndex == 5:
                        Temp=open("/home/pi/fusion_charts/temp.html","w")
                        Temp.write("&value=" + str(value))
                        Temp.close()
                        log_string += name + " = " + str(value) + " " + str(unit) + "\n"
                    elif sensorIndex == 12:
                        RPM=open("/home/pi/fusion_charts/rpm.html","w")
                        RPM.write("&value=" + str(value/1000))
                        RPM.close()
                        log_string += name + " = " + str(value) + " " + str(unit) + "\n"
                    elif sensorIndex == 13:
                        spd=open("/home/pi/fusion_charts/speed.html","w")
                        spd.write("&value=" + str(value))
                        spd.close()
                        log_string += name + " = " + str(value) + " " + str(unit) + "\n"
                        
##                    (name, value, unit) = self.port.sensor(sensorIndex)
##                    print sensorIndex
##                    log_string += name + " = " + str(value) + " " + str(unit) + "\n"
                    
                print log_string,
                time.sleep(0.5)

        except KeyboardInterrupt:
            self.port.close()
            print("stopped")

if __name__ == "__main__":

    o = OBD_Capture()
    o.connect()
    time.sleep(3)
    if not o.is_connected():
        print "Not connected"
    else:
        o.capture_data()
