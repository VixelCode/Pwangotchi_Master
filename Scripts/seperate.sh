#! /bin/bash

cd $1

mkdir hashcat

FILES='*.pcap'

for f in $FILES
do
 "processing $f"
 FileName=$f
 hcxpcapngtool $f --all -o /home/ghoul/Pwnagotchi_Master/loot/hashcat/${f%.pcap}.hc22000 >> ./hashcat/hashcat.log
done
