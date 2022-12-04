"""
Used with XBOX 360 Skylanders portals
"""

import vgamepad as vg
import os
os.environ['PYUSB_DEBUG'] = 'warn'#Can be: warn;error;debug;
import usb.core
import usb.util
import time
import array
from keyboard import press as kd
from keyboard import release as ku

#define gamepad
gamepad = vg.VX360Gamepad()
class pp():
    #W
    def on0(self):
        kd('w')
        COLOR(0x2f,0x2f,0xff)
    def off0(self):
        ku('w')
        
    #A
    def on1(self):
        kd('a')
        COLOR(0xf0,0xa0,0x90)
    def off1(self):
        ku('a')
        
    #S
    def on2(self):
        kd('s')
        COLOR(0xff,0x65,0x00)
    def off2(self):
        ku('s')
        
    #D
    def on3(self):
        kd('d')
        COLOR(0xff,0x20,0x0f)
    def off3(self):
        ku('d')
        
    #Q
    def on4(self):
        kd('q')
        COLOR(0xf1,0x00,0xff)
    def off4(self):
        ku('q')
        
    #E
    def on5(self):
        kd('e')
        COLOR(0xf1,0x00,0xff)
    def off5(self):
        ku('e')
    #C
    def on6(self):
        kd('c')
        COLOR(0x10,0xff,0x10)
    def off6(self):
        ku('c')
    #X
    def on7(self):
        kd('x')
        COLOR(0x10,0xff,0x10)
    def off7(self):
        ku('x')
    #B
    def on8(self):
        kd('b')
        COLOR(0x96,0x4b,0x00)
    def off8(self):
        ku('b')
    #Space
    def on9(self):
        COLOR(0xff,0x20,0x0f)
        kd('space')
        ku('space')
    def off9(self):
        pass
    #Ctrl
    def on10(self):
        kd('ctrl')
        COLOR(0xff,0x20,0x0f)
    def off10(self):
        ku('ctrl')
    #Shift
    def on11(self):
        kd('shift')
        COLOR(0xf0,0xa0,0x90)
    def off11(self):
        ku('shift')
    #MMLeft
    def on12(self):
        gamepad.right_joystick_float(-.5,0)
        gamepad.update()
        COLOR(0x10,0xff,0x10)
    def off12(self):
        gamepad.right_joystick_float(0,0)
        gamepad.update()
    #MMRight
    def on13(self):
        gamepad.right_joystick_float(.5,0)
        gamepad.update()
        COLOR(0xf1,0x00,0xff)
    def off13(self):
        gamepad.right_joystick_float(0,0)
        gamepad.update()
    #MMUp
    def on14(self):
        COLOR(0x2f,0x2f,0xff)
        gamepad.right_joystick_float(0,.5)
        gamepad.update()
    def off14(self):
        gamepad.right_joystick_float(0,0)
        gamepad.update()
    #MMDown
    def on15(self):
        gamepad.right_joystick_float(0,-.5)
        gamepad.update()
        COLOR(0xff,0x65,0x00)
    def off15(self):
        gamepad.right_joystick_float(0,0)
        gamepad.update()
    #Left Click
    def on16(self):
        gamepad.left_trigger_float(value_float=0.5)
        gamepad.update()
        COLOR(0xff,0xa0,0x90)
    def off16(self):
        gamepad.left_trigger_float(value_float=0.0)
        gamepad.update()
    #Right Click
    def on17(self):
        gamepad.right_trigger_float(value_float=0.5)
        gamepad.update()
        COLOR(0xff,0xa0,0x90)
    def off17(self):
        gamepad.right_trigger_float(value_float=0.0)
        gamepad.update()
    #Push To Talk
    def on18(self):
        kd('k')
        COLOR(0x00,0x00,0x00)
    def off18(self):
        ku('k')
    #Next Weapon
    def on19(self):
        gamepad.press_button(button=self.R_shoulder)
        gamepad.update()
        COLOR(0xff,0x65,0x00)
        gamepad.release_button(button=self.R_shoulder)
        gamepad.update()
    def off19(self):
        gamepad.release_button(button=self.R_shoulder)
        gamepad.update()
    #Previous Weapon
    def on20(self):
        gamepad.press_button(button=self.L_shoulder)
        gamepad.update()
        COLOR(0x00,0x00,0x00)
        gamepad.release_button(button=self.L_shoulder)
        gamepad.update()
    def off20(self):
        gamepad.release_button(button=self.L_shoulder)
        gamepad.update()
    def off(self):
        self.off0()
        self.off1()
        self.off2()
        self.off3()
        self.off4()
        self.off5()
        self.off6()
        self.off7()
        self.off8()
        self.off9()
        self.off10()
        self.off11()
        self.off12()
        self.off13()
        self.off14()
        self.off15()
        self.off16()
        self.off17()
        self.off18()
        self.off19()
        self.off20()
    D_up = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP
    D_down = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN
    D_left = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT
    D_right = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT
    Start = vg.XUSB_BUTTON.XUSB_GAMEPAD_START
    Back = vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK
    L_stick = vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB
    R_stick = vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB
    L_shoulder = vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER
    R_shoulder = vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER
    Guide = vg.XUSB_BUTTON.XUSB_GAMEPAD_GUIDE
    A = vg.XUSB_BUTTON.XUSB_GAMEPAD_A
    B = vg.XUSB_BUTTON.XUSB_GAMEPAD_B
    X = vg.XUSB_BUTTON.XUSB_GAMEPAD_X
    Y = vg.XUSB_BUTTON.XUSB_GAMEPAD_Y

pp = pp()

#device initiation
dev = usb.core.find()
dev.set_configuration()
cfg = dev.get_active_configuration()
interface = cfg[(0, 0)].bInterfaceNumber
usb.util.release_interface(dev, interface)
usb.util.claim_interface(dev, interface)

#3rd byte
rESTART = 0x52
qUERY = 0x51
aCTIVATE = 0x41
sTATUS = 0x53
cOLOR = 0x43
#4th byte
ON = 0x01
OFF = 0x00
SKYLANDER1 = 0x10
SKYLANDER2 = 0x11
SKYLANDER1 = 0x12
SKYLANDER2 = 0x13

#Getting skylander hex codes
file_read = open('SkylanderHex.txt', "r")
Codes = file_read.readlines()
Codes = [bad.replace('\n','') for bad in Codes]
print('done')

def RESET():
    bytestr = array.array('B',[0x0b,0x14,rESTART])
    for i in range(20-len(bytestr)):
        bytestr.append(0x00)
    dev.write(0x2,bytestr)


def ACTIVATE():
    bytestr = array.array('B',[0x0b,0x14,aCTIVATE,ON])
    for i in range(20-len(bytestr)):
        bytestr.append(0x00)
    dev.write(0x2,bytestr)

def DEACTIVATE():
    bytestr = array.array('B',[0x0b,0x14,aCTIVATE,OFF])
    for i in range(20-len(bytestr)):
        bytestr.append(0x00)
    dev.write(0x2,bytestr)
    
def STATUS():
    bytestr = array.array('B',[0x0b,0x14,sTATUS])
    for i in range(20-len(bytestr)):
        bytestr.append(0x00)
    dev.write(0x2,bytestr)

def QUERY(SKYLANDER):
    bytestr = array.array('B',[0x0b,0x14,qUERY,int(SKYLANDER)])
    for i in range(20-len(bytestr)):
        bytestr.append(0x00)
    dev.write(0x2,bytestr)
    return [hex(u)[2:] for u in dev.read(0x81,32)]

def COLOR(R,G,B):
    bytestr = array.array('B',[0x0b,0x14,cOLOR,R,G,B])
    for i in range(20-len(bytestr)):
        bytestr.append(0x00)
    dev.write(0x2,bytestr)
    

RESET()
ACTIVATE()
responce = 'poopypoopoo'
def main(responce,SKY):
    responce = QUERY(SKY)
    responce = QUERY(SKY)
    skyCode = responce[responce.index('51')+3:responce.index('51')+7]
    print(responce)
    if skyCode == ['0','0','0','0']:
        pp.off()
        RESET()
        ACTIVATE()
        return print('skylander removed sc')
    exec(f'pp.on{Codes.index(str(skyCode))}()')
    while responce[3] != '0':
        STATUS()
        responce = [hex(u)[2:] for u in dev.read(0x81,32)]
    pp.off()
    RESET()
    ACTIVATE()
    print('skylander removed')
while True:
    try:
        STATUS()
        srt = [hex(u)[2:] for u in dev.read(0x81,32,1000)[0:4]]
        if srt[2] == '53':
            if srt[3] == '1' or srt[3] == '3':
                print(srt[3],'should be 1 or 2')
                main(responce,0x10)
            elif srt[3] == '4':
                print(srt[3],'should be 4 or 8')
                main(responce,0x11)
            elif srt[3] == '10':
                print(srt[3],'should be 10 or 20')
                main(responce,0x12)
            elif srt[3] == '40':
                print(srt[3],'should be 40 or 80')
                main(responce,0x13)
            elif srt[3] == '2' or srt[3] == '8' or srt[3] == '20' or srt[3] == '80':
                dev.reset()
                RESET()
                ACTIVATE()
                pp.off()
            elif srt[3] == '0':
                pass
            else:
                print(f'for some reason it was {srt[3]}')
    except KeyboardInterrupt:
        DEACTIVATE()
        usb.util.release_interface(dev, interface)
        break
DEACTIVATE()
usb.util.release_interface(dev, interface)
print('interrupted')
