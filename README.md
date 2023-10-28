Simple Python3 program I put together to make interactions with a pwnagotchi easier. This is the first program I have written so please have patience as issues arise and I work on fixing them. 

Requirments
All file transfers are completed over ssh, therefore you will have to have root ssh enables in order to transfer files. 
    
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
    chmod +x loot
    chmod +x backup
    sudo python3 Pwnagotchi_Master.py

Menu
   
Pwnagotchi Interactions
        
- SSH into pwnagotchi       
- Download handshakes        
- Erase handshakes   
    
Backup Files
        
- Backup AI
    download brain.nn & brain.json files from pwnagotchi to backup folder
- Backup config.toml
- Download pwnagotchi.log file

Setup Pwnagotchi

- Upload config.toml

Handshake Interactions

Seperate valid handshakes 
- Seperates pcap files with valid handshakes using hcxpcapngtool
  
