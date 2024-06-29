#! /bin/bash

cd $1

FILES='*.hc22000'

for f in $FILES
do
 cat $f >> combined.hc22000

done
