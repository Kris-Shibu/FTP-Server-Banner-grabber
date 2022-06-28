from ftplib import *
import socket

while True:
    server = input("FTP Server to check: ")
    
    if server == "EXIT":
        print("Program Terminated")
        break

    try:
        ftp = FTP(server,timeout=5)
        ftp.login()
        print("Server: ",server,"IP: ",socket.gethostbyname(server))
        print("-"*69)

        print(ftp.getwelcome())
        print("-"*69)
        ftp.quit()

    

    except:
        print("The port appears to be filtered")
   