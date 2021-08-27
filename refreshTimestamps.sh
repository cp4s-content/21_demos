#/bin/bash
# This file will update the date and time on the STIX bundles
# requires the gsed (GNU sed) command to be installed on mac through homebrw
# Jonathan Tomasulo - Cybersecurity Specialist

#currentDate=`date '+%FT%T.000Z'`
currentDate='2031-08-27T15:49:50.000Z'
echo "$currentDate"
gsed -i "s/[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]\.[0-9][0-9][0-9]Z/$currentDate/g" *.json
echo "Dates Updated to: $currentDate Successfully"
