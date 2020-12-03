# ADS1015 Tango device server
This a Tango device server written in PyTango for an ADS1015 ADC using the i2c bus of a Raspberry Pi.

# Installation
## udev rule
If the device server is started by tango-starter, it is necessary to adjust a udev rule, otherwise it lacks permission to access the i2c bus:
```
sudo nano /etc/udev/rules.d/99-com.rules
```
The MODE of the corresponding udev rule has to be changed to 0666:
```
sudo nano /etc/udev/rules.d/99-com.rules
```
Reload and apply the udev rule by
```
sudo udevadm control --reload
sudo udevadm trigger --action=add
```
## ADS1015 python library
The python library is installed as follows (install using sudo for tango-starter operation):
```
sudo pip install ads1015
```

## Authors
Martin Hennecke
