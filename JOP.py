#import
import os, sys, time
from time import sleep as timeout
def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()
#################################################

#print,os.system
os.system("clear")
os.system("figlet J O P | lolcat ")
print "   Author   >> Pound Hacker TH"
print "   Group    >> PlusX HK   "
print "   Version  >> 1       "
print "   Facebook >> https://www.facebook.com/profile.php?id=100053713133557 "
print
print "          [1] >>> DDosAttack   "
print
print "          [2] >>> ExifTool   "
print
print "          [3] >>> Install Tool hacking   "
print
print "          [0] >>> Exit The JOP\n "
print
#################################################

#Different commands
Select = raw_input("Select  >>>>  ")

if Select == "1" or Select == "01":
     os.system("python2 DDosAttack.py")

elif Select == "2" or Select == "02":
     os.system("clear")
     os.system("figlet Exif Tool | lolcat ")
     imageAddress = raw_input("imageAddress >>>>  ")
     os.system("clear")
     os.system("exiftool %s" % (imageAddress))
     print
     print "    [1] Exit The JOP\n "
     print "    [0] Back to main menu\n "
     Select1 = raw_input("Seletc1 >>  ")
     if Select1 == "1" or Select1 == "01":
      os.system("figlet E x i t | lolcat")
      timeout(2)
      sys.exit()
     elif Select1 == "0" or Select1 == "00":
      os.system("figlet Back to main menu | lolcat")
      timeout(2)
      restart_program()
     else:
      os.system("figlet E r r o r | lolcat ")
      timeout(2)
      restart_program()

elif Select == "3" or Select == "03":
     os.system("python2 installToolHacking.py")

elif Select == "0" or Select == "00":
     os.system("figlet E x i t | lolcat")
     timeout(2)
     sys.exit()

else:
     os.system("figlet E r r o r | lolcat ")
     timeout(2)
     restart_program()

#################################################

