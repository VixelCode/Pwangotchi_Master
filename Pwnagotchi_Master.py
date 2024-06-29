#################################################### Pwnagotchi Master #########################################################
###################################################### By - Ghxst_ #############################################################

# Simple python3 proggram to make interactions with your pwnagotchi easier. This is the first program I have written so the code itself could probably be improved, but hey I'm learning and this is an accomplishment for me. If you have any suggestions or input on how to improve any of the coding please feel free to reach out to me on github! I'm always trying to learn new things.



## Pwnagotchi's ip - Default is 10.0.0.2 during setup, but if for some reason you changed it, you can change it here
pwn_ip = '10.0.0.2'


## Pwnagotchi's username - root is needed for handshake file trasnfer. Make sure you have root ssh enabledd on your pwnagotchi!
pwn_uname = 'root'


















# Importing modules needed for program
import subprocess
import os
import paramiko
import sys
import logging
import time
import logging
from datetime import date
















# Fancy things
print(" ____ _    _ _  _   __   ___ _____ ____ ___ _   _ ____    __  __   __   ___ ____ ____ ____ \n"
"(  _ ( \/\/ | \( ) /__\ / __|  _  |_  _) __| )_( |_  _)  (  \/  ) /__\ / __|_  _| ___|  _ \ \n"
" )___/)    ( )  ( /(__)( (_-.)(_)(  )(( (__ ) _ ( _)(_    )    ( /(__)\\__ \ )(  )__) )   / \n"
"(__) (__/\__|_)\_|__)(__)___(_____)(__)\___|_) (_|____)  (_/\/\_|__)(__|___/(__)(____|_)\_) \n")

# Getting local machine variables
local_user = os.getlogin()
local_path = os.getcwd()
date = date.today()

# Setting bash script variables
seperate_bash = (local_path +'/scripts/seperate.sh')
ssh_bash = (local_path + '/scripts/ssh.sh')
combine_bash = (local_path + '/scripts/combine.sh')

# Setting path directories on local machine
loot_path = (local_path + '/loot/')
hashcat_loot = (loot_path + 'hashcat/')
backups = (local_path + '/backups/')

# Hashcat setting
run_hashcat = f'hashcat -m22000'
wordlist = '/usr/share/wordlists/rockyou.txt'

# Setting default answer
default_answer = 'y'

# Setting path directories on pwnagotchi
pwn_handshake = '/root/handshakes/'
pwn_config = '/etc/pwnagotchi/config.toml'

# Redefining settings
ip = pwn_ip
username = pwn_uname

################################################################################################################################

# Logging information
logging.basicConfig(filename='logs.log', level=logging.INFO)

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
        password =input('Please enter your pwnagotchi password : ')
        server_path = pwn_handshake
        
         # Creating SSH connection
        ssh = paramiko.SSHClient() 
        ssh.load_host_keys(os.path.expanduser(os.path.join('~', '.ssh', 'known_hosts')))
        ssh.connect(ip, username=username, password=password)
        print("Connection Successful \n")

        # Open sftp and get file in requested folder
        sftp = ssh.open_sftp()
        files = sftp.listdir(server_path)
        print("Downloading handshakes \n")
        
        # Downloading Files
        for file in files:
            sftp.get(server_path + file, loot_path + file)
        print("Download completed \n")
        logging.info(f' Handshakes downloaded {date}')
        pwnagotchi_interactions()

    if inter_choice == 3: # Delete all handshakes on pwnagotchi
        password = input('Please enter your pwnagotchi password : ')
        server_path = pwn_handshake

        print("WARNING YOUR ABOUT TO DELETE ALL HANDSHAKES ON PWNAGOTCHI - Type y to confirm : ")

        response = str(input())

        if response == default_answer:

            # Creating SSH connection
            ssh = paramiko.SSHClient() 
            ssh.load_host_keys(os.path.expanduser(os.path.join('~', '.ssh', 'known_hosts')))
            ssh.connect(ip, username=username, password=password)
            print("Connection Successful \n")

            # Open sftp and get file in requested folder
            sftp = ssh.open_sftp()
            files = sftp.listdir(server_path)
            print("Erasing handshakes \n")
            
            # Erasing Files
            for file in files:
                sftp.remove(server_path + file)
            print("Erased handshakes from pwnagotchi \n")
            logging.info(f' Erased handhakes from pwnagotchi {date}')
            pwnagotchi_interactions()

    if inter_choice == 0:
        main()

    elif inter_choice != 1-3:
        pwnagotchi_interactions()

################################################################################################################################

# Defining Backup Files
def pwnagotchi_backup():
    print("1 - Backup brain.nn & brain.json \n" "2 - Backup config.toml \n" "3 - Download pwnagotchi.log \n" "0 - Back")

    bkfl_choice = input("Enter choice : ")
    
    bkfl_choice = int(bkfl_choice)

    if bkfl_choice == 1: # Backup brain.nn and brain.json
        # Creating SSH connection
        password =input('Please enter your pwnagotchi password : ')
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
        logging.info(f' Downloaded brain.nn & brain.josn {date}')
        pwnagotchi_backup()

    if bkfl_choice == 2: # Download config.toml

        server_path = pwn_config

        # Creating SSH connection
        password =input('Please enter your pwnagotchi password : ')
        ssh = paramiko.SSHClient() 
        ssh.load_host_keys(os.path.expanduser(os.path.join('~', '.ssh', 'known_hosts')))
        ssh.connect(ip, username=username, password=password)
        print("Connection Succesful \n")
        
        # Download config.toml file
        sftp = ssh.open_sftp()
        sftp.get(server_path, str(backups) + "config.toml")
        print("Downloaded config.toml \n")
        logging.info(f' Downoaded config.toml {date}')
        pwnagotchi_backup()
    
    if bkfl_choice == 3: # Download pwnagotchi.log

        server_path = pwn_config
        
        # Creating SSH connection
        password =input('Please enter your pwnagotchi password : ')
        ssh = paramiko.SSHClient() 
        ssh.load_host_keys(os.path.expanduser(os.path.join('~', '.ssh', 'known_hosts')))
        ssh.connect(ip, username=username, password=password)
        print("Connection Succesful \n")
        
        # Download pwnagotchi file
        sftp = ssh.open_sftp()
        sftp.get(server_path, str(backups) + "pwnagotchi.log")
        print("Downloaded pwnagotchi log \n")
        logging.info(f' Pwnagotchi.log downloaded {date}')
        pwnagotchi_backup()
    
    if bkfl_choice == 0:
        main()

    elif bkfl_choice != 1-3:
        pwnagotchi_backup()
################################################################################################################################

# Defining pwnagotchi setup
def pwnagotchi_setup():
    print("1 - Upload backup config.toml file \n" "0 - Back")

    stup_choice = input("Enter your choice : ")
    
    stup_choice = int(stup_choice)

    if stup_choice == 1:
        
        server_path = pwn_config

        # Creating SSH connection
        password =input('Please enter your pwnagotchi password : ')
        ssh = paramiko.SSHClient() 
        ssh.load_host_keys(os.path.expanduser(os.path.join('~', '.ssh', 'known_hosts')))
        ssh.connect(ip, username=username, password=password)
        print("Connection Succesful \n")
        
        # Uploading config.toml file
        config_toml = backups + 'config.toml'
        print("\n")
        sftp = ssh.open_sftp()
        sftp.put(config_toml, server_path)
        print("Uploaded config.toml \n")
        logging.info(f'config.toml file uploaded {date}')
        pwnagotchi_setup()

    if stup_choice == 0:
        main()

    elif stup_choice != 1:
        pwnagotchi_setup()
################################################################################################################################

def handshake_interactions():
    print("1 - Seperate valid handshakes \n" "2 - Hashcat \n" "3 - Copy and paste to whitelist \n" "0 - Back")
    
    hndske_choice = input("Enter choice : ")
    
    hndske_choice = int(hndske_choice)
    
    if hndske_choice == 1: # Seperating pcap files with good handshakes
        subprocess.call(['bash', seperate_bash, loot_path])
        subprocess.call(['bash', combine_bash, hashcat_loot])
        logging.info(f' Seperated valid handshakes {date}')
        print("Seperated valid handshake files \n")
        handshake_interactions()


    if hndske_choice == 2: # List files in the hashcat folder and asking for user input for which one to run hashcat against
        valid_hashcat = os.listdir(hashcat_loot)
        hashcat_log = valid_hashcat.index('hashcat.log')
        valid_hashcat.pop(hashcat_log)
        for handshake in valid_hashcat:
            print(f'{valid_hashcat.index(handshake)} : {handshake}')      
        hashcat_file = int(input("Select a network : "))
        hashcat_file_name = valid_hashcat[hashcat_file]
        os.system(f'{run_hashcat} {hashcat_loot}{hashcat_file_name} {wordlist}')
    
    if hndske_choice == 3: # Copy and paste for whitelist on pwnagotchi
        print("Below network names are all the networks you have a valid handshake for ready to pasted into your config.toml file. \n")
        valid_handshakes = os.listdir(hashcat_loot)
        if len(valid_handshakes) == 0:
            print("No valid handshakes, get out there and capture some! \n")
            handshake_interactions()
        if "combined.hc22000" in valid_handshakes :
            valid_handshakes.remove("combined.hc22000")
        if "hashcat.log" in valid_handshakes :
            valid_handshakes.remove("hashcat.log")
        if valid_handshakes == 0 : 
            print("No valid handshakes, get out there and capture some! \n")
        for file in valid_handshakes :
            split_hndske = ()
            split_hndske = file.split("_")
            if len(split_hndske) ==2:
                split_hndske.pop(1)
            for file in split_hndske :
                print('"' + file + '",')
        print("\n")
    
    if hndske_choice == 0:
        main()

    elif hndske_choice != 1-3:
        handshake_interactions()

################################################################################################################################

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
        print("Happy Hunting! \n")
        exit()
    elif choice != 1-4:
        main()
main()

