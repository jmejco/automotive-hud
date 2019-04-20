# Automotive HUD

The basic idea of this project is to create a heads-up display for automobiles that effectively
replaces the existing information console. The traditional console is usually placed below the 
driver’s line of sight in most automobiles. This makes drivers shift their attention from the road while looking at the console. This project is a novel approach to bring the information displayed on the console to the driver’s line of sight and presenting it in a way that is aesthetically pleasing and non-distracting. A transparent Graphic User Interface is created which contains the basic information needed in a vehicle such as the speed, RPM and engine temperature. A Raspberry Pi runs this GUI and the display from the Pi is projected on to the windshield of the car using a pico projector. A transparent rear projection film is applied on the windshield of the car to improve visibility while projecting directly on to glass. The data from the car is obtained using an On Board Diagnostics (OBD) adapter which connects to the car and transmits data over Bluetooth to  the  Raspberry Pi.  The  real  time  data  is  processed  into  a  GUI using  a  Python program running inside the Raspberry Pi.

## Demo

![Console Simulation](https://imgur.com/lBZdoPY.jpg)

