## Current setup

My current setup consists of a KNX system together with a few ZigBee devices. ~I'm also running openHAB in parallel just to satisfy my Tellstick stuff (just can't get it to work in HA)~.

### Tellstick + ConBee

Because the server running HA is located in the basement, I needed to figure out a way to extend the radio signal for the Tellstick Duo and ConBee dongles. My first idea was to buy longer USB cables, but I had to drop that idea quickly since they needed to be in lengths of tens of meters. I started to google around and found two suitable software approaches: `usbip` and `socat`. I experimented with `usbip` and quickly got a PoC working with the ConBee device. The final setup basically consists of a Raspberry Pi located underneath the first floor staircase, running `usbip` as a server, exposing the two USB devices on the network. The NUC simply mounts these devices (also with `usbip`, but in "client mode"), and they ultimately show up as any other USB device.

### Docker

My Home Assistant instance is running inside a Docker container. I had some trouble getting my Tellstick Duo to work inside the container, so in case it helps someone, here's my `docker-compose.yml`. The key is the `TelldusClient/TelldusEvents` mount. I also created a custom image for HA since I wanted it to utilize my general purpose MariaDB server.

```yaml
version: '2.2'

services:
  home-assistant:
    container_name: home-assistant
    image: docker-registry.stoffus.com:5000/home-assistant-pymysql:1.0.1
    volumes:
      - ./config:/config
      - /etc/localtime:/etc/localtime:ro
      - ./tellstick.conf:/etc/tellstick.conf
      - /tmp/TelldusClient:/tmp/TelldusClient
      - /tmp/TelldusEvents:/tmp/TelldusEvents
    restart: always
    network_mode: host
    mem_limit: 1g
    devices:
      - /dev/ttyACM0 # ConBee
```
