# Skylanders-portal-controler
This is a script I made to use different skylanders and a skylanders portal to control a game. The game this was built for is Valorant. This was only tested on a windows computer using xbox 360 portals. It can only support 1 skylander at a time currently. not shure if i will add supporrt for multiple. There is a bit of input delay on this and i have tried my est to lessen it but it's still there. This isn't the most fun to play especially a shooter or a gme where you have to move arround a lot. This was just made to see if i could not for actual use.
## Requirements
Main stuff:
  * ReWasd (7$ lifetime license or 7day free trial works with both)
  * Python (3.9 64bit is the only version I have tested)
  * 21 different skylanders
  * a portal (obviously)
  * Zadig (used to install libusbk)

Python libraries:
  + vgamepad
  + array
  + pyusb
  + keyboard
  + os (should already have)
  + time (should already have)

## Tutorial part
will make video tutorial eventually hen there is one it will be here:
##### Portal setup
First install zadig from here https://zadig.akeo.ie looks sketch af I know but it works.

Next you ned to connect your portal to your pc and open zadig. 

Press options and check list all devices. 

Then click on the big bar with the arrow and select either 'PORTAL' or 'Spyro Portal' and set the driver to libusbK and press replace driver.

##### Setting the skylanders

_If i'm being honest im not shure what is being read so there is a chance that you have two different Skylanders with the same code if so let me know on my discord server (at the bottom of the page) or create an issue._

First you need to connect your portal if it isn't connected already and open "Fine Hex Codes.py" with any ide. VScode or the python IDLE

Next place the skylanders you want in the order of the inputs that you want them
>w, a, s, d, q, e, c, x, b, space, control, shift, mouse left, mouse right, mouse up, mouse down, left click, right click, k, scroll down, scroll up

after you get all 21 unique skylanders registered it hsould stop. Check the SkylanderHex.txt file to nake shure that there are 21 codes there.

##### ReWasd setup

open rewasd

click on the right joystick and click mouse

click on the left shoulder button and make it scroll down and make the right one scroll up

save the layout and turn off editing because it will sometimes overwrite the layout.

If you made it this far you should be done tey it out. For Valorant unoplug your mouse before you open Val because of the anti-cheat only one cursor moving device will work at a time.

Any issues post in the correct channel in the discord server here:

  https://discord.gg/H6QMSJwdJU
  
Or create a github issue
