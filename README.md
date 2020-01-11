## Current setup

My current setup consists of a KNX system together with some NEXA/Telldus "smart" plugs and a few ZigBee devices (mostly Aqara sensors).

### Tellstick + ConBee

Because the server running HA is located in the basement, I needed to figure out a way to extend the radio signal for the Tellstick Duo and ConBee dongles. My first idea was to buy longer USB cables, but I had to drop that idea quickly since they needed to be in lengths of tens of meters. I started to google around and found two suitable software approaches: `usbip` and `socat`. I experimented with `usbip` and quickly got a PoC working with the ConBee device. The final setup basically consists of a Raspberry Pi located underneath the first floor staircase, running `usbip` as a server, exposing the two USB devices on the network. The NUC simply mounts these devices (also with `usbip`, but in "client mode"), and they ultimately show up as any other USB device.
