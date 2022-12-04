"""
Used with XBOX 360 Skylanders portals
"""


import os
os.environ['PYUSB_DEBUG'] = 'warn'#Can be: warn;error;debug;
import usb.core
import usb.util
import array
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
#4th-6th byte
ON = 0x01
OFF = 0x00
SKYLANDER1 = 0x10
SKYLANDER2 = 0x11
SKYLANDER1 = 0x12
SKYLANDER2 = 0x13

def RESET():
    bytestr = array.array('B',[0x0b,0x14])
    command = [rESTART]
    for i in command:
        bytestr.append(int(i))
    for i in range(20-len(bytestr)):
        bytestr.append(0x00)
    dev.write(0x2,bytestr)


def ACTIVATE():
    bytestr = array.array('B',[0x0b,0x14])
    command = [aCTIVATE,ON]
    for i in command:
        bytestr.append(i)
    for i in range(20-len(bytestr)):
        bytestr.append(0x00)
    dev.write(0x2,bytestr)

def DEACTIVATE():
    bytestr = array.array('B',[0x0b,0x14])
    command = [aCTIVATE,OFF]
    for i in command:
        bytestr.append(i)
    for i in range(20-len(bytestr)):
        bytestr.append(0x00)
    dev.write(0x2,bytestr)
    
def STATUS():
    bytestr = array.array('B',[0x0b,0x14])
    command = [sTATUS]
    for i in command:
        bytestr.append(int(i))
    for i in range(20-len(bytestr)):
        bytestr.append(0x00)
    dev.write(0x2,bytestr)

def QUERY(SKYLANDER):
    bytestr = array.array('B',[0x0b,0x14])
    command = [qUERY,0x10]
    for i in command:
        bytestr.append(int(i))
    for i in range(20-len(bytestr)):
        bytestr.append(0x00)
    dev.write(0x2,bytestr)
    
RESET()
ACTIVATE()
QUERY(SKYLANDER1)

responce = ''
print('starting')
#Setting skylander hex codes
lines = []

def main(responce,SKY):
    resCode = False
    show = True
    while True:
        while '51' not in responce:
            try:
                #print('in main')
                QUERY(SKY)
                responce = [hex(u)[2:] for u in dev.read(0x81,32)]
                #print(f'Post Query{SKYLANDER}')
            except Exception:
                #RESET()
                #ACTIVATE()
                STATUS()
                QUERY(SKY)
        resCode = str(responce[responce.index('51')+3:responce.index('51')+7])+"\n"
        if resCode == "['0', '0', '0', '0']\n":
            #sprint(resCode)
            return None
        else:
            pass
        return resCode
why = 0
while True:
    
    try:
        STATUS()
        try:
            srt = [hex(u)[2:] for u in dev.read(0x81,32,1000)[0:4]]
            
        except:
            pass
        why +=1
        if srt[2] == '53' and srt[3] != '0':
            #print(srt[3])
            if srt[3] == '1':
                x = main(responce,0x10)
                if x not in lines and x != None:
                    print(x)
                    lines.append(x)
            elif srt[3] == '4':
                x = main(responce,0x11)
                if x not in lines and x != None:
                    print(x)
                    lines.append(x)
            elif srt[3] == '10':
                x = main(responce,0x12)
                if x not in lines and x != None:
                    print(x)
                    lines.append(x)
            elif srt[3] == '40':
                x = main(responce,0x13)
                if x not in lines and x != None and x != "['0', '0', '0', '0']\n":
                    print(x)
                    lines.append(x)
                RESET()
                ACTIVATE()
            elif srt[3] == '2' or srt[3] == '8' or srt[3] == '20' or srt[3] == '80':
                RESET()
                ACTIVATE()
            else:
                pass
        else:
            pass
    except KeyboardInterrupt:
        DEACTIVATE()
        usb.util.release_interface(dev, interface)
        dev.reset()
        print('interrupted')
        print(lines)
        break
with open('SkylanderHex.txt', "w") as file:
    [file.write(_) for _ in lines]
    print('done')

