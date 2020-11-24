#board Lolin32 V1.0.0
#WIFI-ESP-WROOM-32

#Install Python3, pip3 and rshell
sudo apt-get -y install python3
sudo apt-get -y install python3-pip
sudo pip3 install rshell

#Install the latest stable esptool.py release with pip
sudo pip3 install esptool

#Using esptool.py you can erase the flash with the command
esptool.py --port /dev/ttyS6 erase_flash

#Deploy the new firmware using
#Be careful with the newer firmware versions. Sometimes rshell does not work and the board cannot be connected. (esp32-idf3-20191220-v1.12.bin)
esptool.py --chip esp32 -p /dev/ttyS6 write_flash -z 0x1000 /mnt/c/esp/esp32-idf3-20180511-v1.9.4.bin


rshell --buffer-size=30 -p /dev/ttyS6

#REPL stands for Read Evaluate Print Loop, and is the name given to the interactive MicroPython prompt that you can access on the WiPy. 
#Using the REPL is by far the easiest way to test out your code and run commands. 
repl

#blink onboard LED
import utime
import machine
pin5 = machine.Pin(5, machine.Pin.OUT)
while True:
  pin5.value(1)
  utime.sleep_ms(500)
  pin5.value(0)
  utime.sleep_ms(500)