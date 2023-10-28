#! /bin/bash

cd $1

mkdir hashcat

FILES='*.pcap'

for f in $FILES
do
 "processing $f"
 FileName=$f
 hcxpcapngtool $f --all -o {$1}/hashcat/${f%.pcap}.hc22000 >> ./hashcat/hashcat.log
done
