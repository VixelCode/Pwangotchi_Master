#! /bin/bash

cd $1

FILES='*.pcap'

for f in $FILES
do
 FileName=$f
 hcxpcapngtool $f --all -o $1/hashcat/${f%.pcap}.hc22000 >> ./hashcat/hashcat.log

done
