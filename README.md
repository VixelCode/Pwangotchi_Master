Simple Python3 program I put together to make interactions with a pwnagotchi easier. This is the first program I have written so please have patience as issues arise and I work on fixing them. If you have any suggestions, or just input on how to make the code more efficient please feel free to let me know!


Requirments
All file transfers are completed over ssh, therefore you will have to have root ssh enables in order to transfer files. 
Currently only tested on kali VM
    
To enable root ssh on your pwnagotchi, first ssh into your pwnagotchi

    sudo su
    passwd root
    'yourpassword'
    sudo nano /etc/ssh/sshd_config
    find the line that says '#PermitRootLogin prohibit-password'
    change it to say 'PermitRootLogin yes'
    service ssh restart

Intructions 
    
    cd /path/to/Pwnagotchi_Master
    sudo bash setup.sh
    sudo python3 Penagotchi_Master.py

Menu
   
Pwnagotchi Interactions
        
- SSH into pwnagotchi       
- Download handshakes from pwnagotchi       
- Erase handshakes from pwnagotchi
    
Backup Files
        
- Backup AI
    download brain.nn & brain.json files from pwnagotchi to backup folder
- Backup config.toml
- Download pwnagotchi.log file

Setup Pwnagotchi

- Upload config.toml

Handshake Interactions
 
- Seperates pcap files with valid handshakes using hcxpcapngtool
- Select from list of files to run hashcat on
- Prints in terminal a copy and paste string of all networks you have a valid handshake for to be pasted into your pwnagotchi's config.toml file.
  
