from gpiozero import Button
from signal import pause
from time import sleep
from math import pow, floor
import subprocess

# list of bits, representing the 32 buttons
binaryList = [0] * 32
# Report hex values, will be populated at a later date
hexList = [None] * 4
NULL_CHAR = chr(0)
report_length_file = open('/sys/kernel/config/usb_gadget/xac_joystick/functions/hid.usb0/report_length', 'r')
report_length      = int(report_length_file.read())

# image display maybe
# image = subprocess.Popen('feh --hide-pointer -x -q -B black -g 1280x800 /home/pi/images/eliteD.png'.split())
def clean_up():
    report = NULL_CHAR*report_length
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

def sendReport():
    # empty bytes are \0 and hex codes are \x followed by the two hex digits
    report = str(''.join(hexList))
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())
    #print('report: \''+str(report)+'\'')
    #print('bits: '+str(binaryList))

def compileReport():
    # go through the bytes we want to send. 4 because we have 32 buttons
    for x in range(len(hexList)):
        # initialise some stuff
        hexList[x] = None
        bitsReverseString = ''

        # get the bits
        bitsReverse = binaryList[x*8:(x*8)+8]
        # and then WE REVERSE THEM because they are backwards in the byte
        # without this, button 2 would be triggered by GPIO 7, and 1 by 8, etc.
        bitsReverse.reverse()

        for y in range(len(bitsReverse)):
            bitsReverseString += str(bitsReverse[y])
        
        hexVal = hex(int(bitsReverseString,2))#[2:]

        if (hexVal == '0x0' or hexVal == '0x00'):
            hexList[x] = '\0'
        else:
            # turns the hex string into an int and a unicode character that the computer interprets as a digit
            print(hexVal+' byte: '+str(x))
            hexList[x] = chr(int(hexVal,16))
            #hexList[x] = hexVal
            #if (len(hexVal) == 1):
                # [1:] trims the 0 from the from of the hex so we get x04 or x40 rather than 0x04 or 0x40
                #hexList[x] = r'\x'+hexVal+'0'
            #else: 
                #hexList[x] = r'\x'+hexVal
def modifyBit(butt, val='flip'):
    # button 1 is bit 0 so we -1 to turn the button number into the list position\
    pos = int(butt) 

    # check if its been changed to something valid
    if (val != 'flip') and (val==1 or val==2):
        # turn our button into the value
        binaryList[pos] = val
    else:
        # its just been flipped so we change it
        if (binaryList[pos] == 1):
            binaryList[pos] = 0
        else:
            binaryList[pos] = 1
def button(butt, val='flip'):
    modifyBit(butt, val)
    compileReport()
    sendReport()

def activate(butt):
    button(butt.pin.number, 1)
def deactivate(butt):
    button(butt.pin.number, 0)

# def screen():
    # image = subprocess.Popen('feh --hide-pointer -x -q -B black -g 256x160 images/atreides.png'.split())

# Using GPIO 0 to 15
gpio_0 = Button(0)
gpio_0.when_pressed = activate
gpio_0.when_released = deactivate

gpio_1 = Button(1)
gpio_1.when_pressed = activate
gpio_1.when_released = deactivate

gpio_2 = Button(2)
gpio_2.when_pressed = activate
gpio_2.when_released = deactivate

gpio_3 = Button(3)
gpio_3.when_pressed = activate
gpio_3.when_released = deactivate

gpio_4 = Button(4)
gpio_4.when_pressed = activate
gpio_4.when_released = deactivate

gpio_5 = Button(5)
gpio_5.when_pressed = activate
gpio_5.when_released = deactivate

gpio_6 = Button(6)
gpio_6.when_pressed = activate
gpio_6.when_released = deactivate

gpio_7 = Button(7)
gpio_7.when_pressed = activate
gpio_7.when_released = deactivate

gpio_8 = Button(8)
gpio_8.when_pressed = activate
gpio_8.when_released = deactivate

gpio_9 = Button(9)
gpio_9.when_pressed = activate
gpio_9.when_released = deactivate

gpio_10 = Button(10)
gpio_10.when_pressed = activate
gpio_10.when_released = deactivate

gpio_11 = Button(11)
gpio_11.when_pressed = activate
gpio_11.when_released = deactivate

gpio_12 = Button(12)
gpio_12.when_pressed = activate
gpio_12.when_released = deactivate

gpio_13 = Button(13)
gpio_13.when_pressed = activate
gpio_13.when_released = deactivate

gpio_14 = Button(14)
gpio_14.when_pressed = activate
gpio_14.when_released = deactivate

gpio_15 = Button(15)
gpio_15.when_pressed = activate
gpio_15.when_released = deactivate

# Gpio 16 to 19 will be for internal changes

clean_up()
clean_up()
clean_up()

pause()
