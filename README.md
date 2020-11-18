# Current setup

My current setup consists of a KNX system together with ~~some NEXA/Telldus "smart" plugs and~~ a few ZigBee devices (mostly Aqara sensors).

## Tellstick + ConBee

Because the server running HA is located in the basement, I needed to figure out a way to extend the radio signal for the Tellstick Duo and ConBee dongles. My first idea was to buy longer USB cables, but I had to drop that idea quickly since they needed to be in lengths of tens of meters. I started to google around and found two suitable software approaches: `usbip` and `socat`. I experimented with `usbip` and quickly got a PoC working with the ConBee device. The final setup basically consists of a Raspberry Pi located underneath the first floor staircase, running `usbip` as a server, exposing the two USB devices on the network. The NUC simply mounts these devices (also with `usbip`, but in "client mode"), and they ultimately show up as any other USB device.

## Frigate

I'm using frigate (https://github.com/blakeblackshear/frigate) to detect object from my IP cameras.

# Tech specs

## KNX

### Actuators

- 1 x MDT AMS-0816.01
- 1 x MDT AKS-1216.02
- 1 x MDT AKD-0401.01
- 1 x MDT JAL-0410.01

### Wall panels

- 4 x Schneider Exxact WDE002933
- 2 x Schneider Exxact WDE002935
- 2 x Schneider Exxact WDE002943
- 1 x Schneider Exxact WDE002949
- 2 x MDT BE-TA55P4.01
- 1 x MDT BE-TA55P6.01

### Misc

- 1 x MDT SCN-IP000.01 (IP interface)
- 1 x MDT SCN-WS3HW.01 (Weather station)
- 1 x MDT STV-0640.01 (Power supply)

## ZigBee

### Sensors

- 9 x Aqara WSDCGQ11LM (Temperature/Humidity Sensor)
- 3 x Aqara AS006UEW01 (Window/Door Sensor)
- 6 x Aqara AS007UEW01 (Motion Sensor)
- 4 x Aqara AS009UEW01 (Vibration Sensor) 
- 1 x Aqara AS010UEW01 (Water Leak Sensor) 
- 3 x Aqara WXKG11LM (Wireless Mini Switch)

### Switches

- 1 x Innr SP 120
- 2 x IKEA TRÅDFRI

## ~~433 Mhz~~

~~Still got some old NEXA wall plugs that works good enough to not be replaced.~~
