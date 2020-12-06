# setmylights

## User based color selector for my own xmas lights
- User can set color values and apply it to current state of the xmas lights
- A real time feed shows if the color changes
- User can add their names and be shown in the guest log


## Tech Stack

### LED Strips and Controller
- WS2812b 300led/5m strip
- NodeMCU running micropython
- Power supply 5V/10A rating

### Video Stream
- Raspberry Pi Zero W
- PiCam
- Motion OS

### Webserver
- Hosted at AWS EC2 t2.micro (free lol)
- Nginx server
- Flask framework

### Operation
- Webserver, Video stream, & Led control are running independently.
- Led control built script which request Webserver to get recent color state (values)
- Webserver sets the color state whenever a user clicks apply
- Video stream is running locally on my raspberry pi, so i needed to port forward from my router to be accessible to public network. Then a reverse proxy server is configured on Nginx to forward Video stream to the webserver.