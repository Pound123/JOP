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
os.system("figlet Tool | lolcat")
print 
print "     Install Tool Hacking      "
print 
print "     [1] Show Tool Hacking  "
print "     [2] DDos-Attack Tool  "
print "     [3] Phishing Tool "
print 
print "     [0] Exit The installToolHacking\n"
print
#################################################

#Different commands
Select = raw_input("Select [1,2,3,0]>>  ")

if Select == "1" or Select == "01":
   print
   print "    [01] XTRACK "
   print "    [02] WishFish "
   print "    [03] blackeye "
   print "    [04] TBomb "
   print "    [05] DDos-Attack "
   print "    [06] DDos "
   print "    [07] Planetwork-DDOS "
   print "    [08] SocialSploit "
   print "    [09] zphisher "
   print
   print "    [00] Back to main menu\n "
   ToolSelect = raw_input("ToolSelect [$] ")
   if ToolSelect == "1" or ToolSelect == "01":
     os.system("figlet XTRACK | lolcat")
     os.system("pkg install git -y")
     os.system("git clone https://github.com/MALW4R3/XTRACK")
   elif ToolSelect == "2" or ToolSelect == "02":
     os.system("figlet WishFish | lolcat")
     os.system("pkg install php -y")
     os.system("pkg install wget -y")
     os.system("pkg install openssh -y")
     os.system("git clone https://github.com/kinghacker0/WishFish")
   elif ToolSelect == "3" or ToolSelect == "03":
     os.system("figlet Blackeye | lolcat")
     os.system("pkg install git -y")
     os.system("git clone https://github.com/An0nUD4Y/blackeye")
   elif ToolSelect == "4" or ToolSelect == "04":
     os.system("figlet TBomb | lolcat")
     os.system("pkg install git -y")
     os.system("pkg install python -y")
     os.system("git clone https://github.com/thevicky48/TBomb")
   elif ToolSelect == "5" or ToolSelect == "05":
     os.system("figlet DDos-Attack | lolcat")
     os.system("pkg install git -y")
     os.system("git clone https://github.com/Ha3MrX/DDos-Attack")
   elif ToolSelect == "6" or ToolSelect == "06":
     os.system("figlet DDos | lolcat")
     os.system("pkg install git -y")
     os.system("git clone https://github.com/Bell-A-7KA/DDos")
   elif ToolSelect == "7" or ToolSelect == "07":
     os.system("figlet Planetwork-DDOS | lolcat")
     os.system("pkg install git -y")
     os.system("git clone https://github.com/Hydra7/Planetwork-DDOS")
   elif ToolSelect == "8" or ToolSelect == "08":
     os.system("figlet SocialSploit | lolcat")
     os.system("pkg install -y git")
     os.system("git clone https://github.com/Cesar-Hack-Gray/SocialSploit")
   elif ToolSelect == "9" or ToolSelect == "09":
     os.system("figlet zphisher | lolcat")
     os.system("apt update -y")
     os.system("apt install git curl php wget -y")
     os.system("git clone https://github.com/htr-tech/zphisher")
   elif ToolSelect == "0" or ToolSelect == "00":
     os.system("figlet Back to main menu | lolcat")
     timeout(2)
     restart_program()
   else:
     os.system("figlet E r r o r | lolcat ")
     timeout(2)
     restart_program()

elif Select == "2" or Select == "02":
     print
     print "    [1] DDos-Attack   "
     print "    [2] Planetwork-DDOS "
     print "    [3] DDos "
     print
     print "    [0] Back to main menu\n "
     ToolDDosAttack = raw_input("ToolDDosAttack >> ")
     if ToolDDosAttack == "1" or ToolDDosAttack == "01":
      os.system("figlet DDos-Attack | lolcat")
      os.system("pkg install git -y")
      os.system("git clone https://github.com/Ha3MrX/DDos-Attack")
     elif ToolDDosAttack == "2" or ToolDDosAttack == "02":
      os.system("figlet Planetwork-DDOS | lolcat")
      os.system("pkg install git -y")
      os.system("git clone https://github.com/Hydra7/Planetwork-DDOS")
     elif ToolDDosAttack == "3" or ToolDDosAttack == "03":
      os.system("figlet DDos | lolcat")
      os.system("pkg install git -y")
      os.system("git clone https://github.com/Bell-A-7KA/DDos")
     elif ToolDDosAttack == "0" or ToolDDosAttack == "00":
      os.system("figlet Back to main menu | lolcat")
      timeout(2)
      restart_program()
     else:
      os.system("figlet E r r o r | lolcat ")
      timeout(2)
      restart_program()

elif Select == "3" or Select == "03":
      print 
      print "    [1] SocialSploit "
      print "    [2] blackeye "
      print "    [3] zphisher "
      print
      print "    [0] Back to main menu\n "
      ToolPhishing = raw_input("PhishingTool >> ")
      if ToolPhishing == "1" or ToolPhishing == "01":
       os.system("figlet SocialSploit | lolcat")
       os.system("pkg install git -y")
       os.system("git clone https://github.com/Cesar-Hack-Gray/SocialSploit")
      elif ToolPhishing == "2" or ToolPhishing == "02":
       os.system("figlet blackeye | lolcat")
       os.system("pkg install git -y")
       os.system("git clone https://github.com/An0nUD4Y/blackeye")
      elif ToolPhishing == "3" or ToolPhishing == "03":
       os.system("figlet zphisher | lolcat")
       os.system("apt update -y")
       os.system("apt install git curl php wget -y")
       os.system("git clone https://github.com/htr-tech/zphisher")
      elif ToolPhishing == "0" or ToolPhishing == "00":
       os.system("figlet Back to main menu | lolcat")
       timeout(2)
       restart_program()
      else:
       os.system("figlet E r r o r | lolcat ")
       timeout(2)
       restart_program()

elif Select == "0" or Select == "00":
     os.system("figlet E x i t | lolcat")
     timeout(2)
     sys.exit()
      
else:
     os.system("figlet E r r o r | lolcat ")
     timeout(2)
     restart_program()
#################################################
