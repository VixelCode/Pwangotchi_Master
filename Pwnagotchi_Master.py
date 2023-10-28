#################################################### Pwnagotchi Master #########################################################
###################################################### By - Ghxst_ #############################################################

# Simple python3 proggram to make interactions with your pwnagotchi easier. This is the first program I have written so the code itself could probably be improved, but hey I'm learning and this is an accomplishment for me. 



## Pwnagotchi's ip - Default is 10.0.0.2 during setup, but if for some reason you changed it, you can change it here
pwn_ip = '10.0.0.2'


## Pwnagotchi's username - root is needed for handshake file trasnfer. Make sure you have root ssh enabledd on your pwnagotchi!
pwn_uname = 'root'















# This could be very easily changed into a way to download, upload, and erase files from a remote server via a shh connection


# Importing modules needed for program
import subprocess
import os
import paramiko
import sys
import logging
import time















# Fancy things
print(" ____ _    _ _  _   __   ___ _____ ____ ___ _   _ ____    __  __   __   ___ ____ ____ ____ \n"
"(  _ ( \/\/ | \( ) /__\ / __|  _  |_  _) __| )_( |_  _)  (  \/  ) /__\ / __|_  _| ___|  _ \ \n"
" )___/)    ( )  ( /(__)( (_-.)(_)(  )(( (__ ) _ ( _)(_    )    ( /(__)\\__ \ )(  )__) )   / \n"
"(__) (__/\__|_)\_|__)(__)___(_____)(__)\___|_) (_|____)  (_/\/\_|__)(__|___/(__)(____|_)\_) \n")

# Getting local machine variables
local_user = os.getlogin()
local_path = os.getcwd()

# Setting bash script variables
ssh_bash = (local_path + '/Scripts/ssh.sh')
seperate_bash = (local_path +'/Scripts/seperate.sh')
hashcat_bash = (local_path + '/Scripts/hashcat.sh')


# Setting path directories on local machine
loot_path = (local_path + '/loot/')
backups = (local_path + '/backups/')
hash_file = (local_path + '/combinded.hc22000')
cracked_file = (local_path + '/loot/cracked.txt')
whitelist = (local_path + '/whitelist.txt')

print()

# Setting path directories on pwnagotchi
pwn_handshake = '/root/handshakes/'
pwn_config = '/etc/pwnagotchi/config.toml'

# Redefining settings
ip = pwn_ip
username = pwn_uname

################################################################################################################################

# Defining pwnagotchi Interactions
def pwnagotchi_interactions():
    print("1 - SSH into pwnagotchi \n""2 - Download all pcap files \n" "3 - Erase all handshakes on pwnagotchi \n" "0 - Back")

    inter_choice = input("Enter choice : ")
    
    inter_choice = int(inter_choice)

    if inter_choice == 1: # SSH into pwnagotchi
        subprocess.call(ssh_bash, shell=True)
        pwnagotchi_interactions()

    if inter_choice == 2: # Download all pcap files
        password =input('Please enter your pwnagotchi password - ')
        server_path = pwn_handshake
        
         # Creating SSH connection
        ssh = paramiko.SSHClient() 
        ssh.load_host_keys(os.path.expanduser(os.path.join('~', '.ssh', 'known_hosts')))
        ssh.connect(ip, username=username, password=password)
        print("Connection Successfull \n")

        # Open sftp and get file in requested folder
        sftp = ssh.open_sftp()
        files = sftp.listdir(server_path)
        print("Downloading handshakes \n")
        
        # Downloading Files
        for file in files:
            sftp.get(server_path + file, loot_path + file)
        print("Download completed \n")
        pwnagotchi_interactions()

    if inter_choice == 3: # Delete all handshakes on pwnagotchi
        password =input('Please enter your pwnagotchi password - ')
        server_path = pwn_handshake

        print("WARNING YOUR ABOUT TO DELETE ALL HANDSHAKES ON PWNAGOTCHI - Please type yes to confirm : ")

        response = str(input())

        if response == str("yes"):

            # Creating SSH connection
            ssh = paramiko.SSHClient() 
            ssh.load_host_keys(os.path.expanduser(os.path.join('~', '.ssh', 'known_hosts')))
            ssh.connect(ip, username=username, password=password)
            print("Connection Successfull \n")

            # Open sftp and get file in requested folder
            sftp = ssh.open_sftp()
            files = sftp.listdir(server_path)
            print("Erasing handshakes \n")
            
            # Erasing Files
            for file in files:
                sftp.remove(server_path + file)
            print("Erased handshakes from pwnagotchi \n")
            pwnagotchi_interactions()

    if inter_choice == 0:
        main()

################################################################################################################################

# Defining Backup Files
def pwnagotchi_backup():
    print("1 - Backup brain.nn & brain.json \n" "2 - Backup config.toml \n" "3 - Download pwnagotchi.log \n" "0 - Back")

    bkfl_choice = input("Enter choice : ")
    
    bkfl_choice = int(bkfl_choice)

    if bkfl_choice == 1: # Backup brain.nn and brain.json
        # Creating SSH connection
        password =input('Please enter your pwnagotchi password - ')
        ssh = paramiko.SSHClient() 
        ssh.load_host_keys(os.path.expanduser(os.path.join('~', '.ssh', 'known_hosts')))
        ssh.connect(ip, username=username, password=password)
        print("Connection Succesful \n")
        
        # Download brain.nn file
        server_path = str('/' + '/root/brain.nn')
        sftp = ssh.open_sftp()
        sftp.get(server_path, str(backups) + "brain.nn")
       
        # Download brain.json file
        server_path = str('/' + '/root/brain.json')
        sftp = ssh.open_sftp()
        sftp.get(server_path, str(backups) + "brain.json")
        print("brain.nn & brain.json downloaded \n")
        pwnagotchi_backup()

    if bkfl_choice == 2: # Download config.toml

        server_path = pwn_config

        # Creating SSH connection
        password =input('Please enter your pwnagotchi password - ')
        ssh = paramiko.SSHClient() 
        ssh.load_host_keys(os.path.expanduser(os.path.join('~', '.ssh', 'known_hosts')))
        ssh.connect(ip, username=username, password=password)
        print("Connection Succesful \n")
        
        # Download config.toml file
        sftp = ssh.open_sftp()
        sftp.get(server_path, str(backups) + "config.toml")
        print("Downloaded config.toml \n")
        pwnagotchi_backup()
    
    if bkfl_choice == 3: # Download pwnagotchi.log

        server_path = pwn_config
        
        # Creating SSH connection
        password =input('Please enter your pwnagotchi password - ')
        ssh = paramiko.SSHClient() 
        ssh.load_host_keys(os.path.expanduser(os.path.join('~', '.ssh', 'known_hosts')))
        ssh.connect(ip, username=username, password=password)
        print("Connection Succesful \n")
        
        # Download pwnagotchi file
        sftp = ssh.open_sftp()
        sftp.get(server_path, str(backups) + "pwnagotchi.log")
        print("Downloaded pwnagotchi log \n")
        pwnagotchi_interactions()
    

    if bkfl_choice == 0:
        main()

################################################################################################################################

# Defining pwnagotchi setup
def pwnagotchi_setup():
    print("1 - Move config.toml file \n" "0 - Back")

    stup_choice = input("Enter your choice : ")
    
    stup_choice = int(stup_choice)

    if stup_choice == 1:
        
        server_path = pwn_config

        # Creating SSH connection
        password =input('Please enter your pwnagotchi password - ')
        ssh = paramiko.SSHClient() 
        ssh.load_host_keys(os.path.expanduser(os.path.join('~', '.ssh', 'known_hosts')))
        ssh.connect(ip, username=username, password=password)
        print("Connection Succesful \n")
        
        # Uploading config.toml file
        config_toml = input("EXAMPLE - /home/user/config/toml \n " "Enter full path to your config.toml file - ")
        print("\n")
        sftp = ssh.open_sftp()
        sftp.put(config_toml, server_path)
        print("Uploaded config.toml \n")
        pwnagotchi_setup()

    if stup_choice == 0:
        main()

################################################################################################################################

def handshake_interactions():
    print("1 - Seperate valid handshakes \n" "2 - Hashcat combined.txt \n" "3 - Whitelist networks with valid handshakes \n" "0 - Back")
    
    hndske_choice = input("Enter choice : ")
    
    hndske_choice = int(hndske_choice)
    
    if hndske_choice == 1: # Seperating pcap files with good handshakes
        subprocess.call(['bash', seperate_bash, loot_path])
        #subprocess.call(seperate_bash, shell=True)
        print("Seperated valid handshake files \n")

    if hndske_choice == 2: # Hashcat combinded.txt
        print("Coming soon!")
        handshake_interactions()       
            
            
    if hndske_choice == 3:
        print("Coming soon!")
        handshake_interactions()

    if handshake_interactions == 0:
        print("Coming soon!")
        handshake_interactions()

# Main Menu
def main():
    print("1 - Pwnagotchi Interactions \n" "2 - Backup Files \n" "3 - Pwnagotchi Setup \n" "4 - Handshake Interactions \n" "0 - Exit \n")

    choice = input("Enter choice : ")

    choice = int(choice)

    options = [1, 2, 0]

    if choice == 1:
        pwnagotchi_interactions()

    if choice == 2:
        pwnagotchi_backup()

    if choice == 3:
        pwnagotchi_setup()

    if choice == 4:
        handshake_interactions()

    if choice == 0:
        print("Exiting \n")
        exit

main()

