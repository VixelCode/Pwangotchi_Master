Simple Python3 program I put together to make interactions with a pwnagotchi easier. This is the first program I have written so please have patience as issues arise and I work on fixing them. 

Requirments
    All file transfers are completed over ssh, therefore you will have to have root ssh enables in order to transfer files. 
    
    To enable root ssh on your pwnagotchi
    ssh into your pwnagotchi
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
    sudo python3 Pwnagotchi_Master.py

Menu
   
    Pwnagotchi interactions
        
    SSH into pwnagotchi
        creates a ssh connection to your pwnagotchi
        
    Download handshakes
        downloads all files from pwnagotchi's handshakes folder to loot folder
        
    Erase handshakes
         erases all files in pwnagotchi's handshakes folder
        
    Download pwnlog
        download pwnagotchi's pwnagotchi.log file to backup folder
    
    Backup Files
        
    Backup AI
        download brain.nn & brain.json files from pwnagotchi to backup folder
        
    Backup config
        download config.toml file from pwnagotchi to backup folder

    Pwnagotchi Setup
        upload config.toml to /etc/pwnagotchi
