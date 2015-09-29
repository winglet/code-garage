#!/bin/bash
mydir="/root/checkdu/"
fname=$mydir"checkdu_"$(date | sed s/" "/_/g )

echo $fname
df > $fname
dirs=("/home" "/tmp" "/var" "/etc" "/lib" "/opt" "/root" "/usr")
for i in "${dirs[@]}"
do
   :
   echo $i >> $fname
   du $i --max-depth=1 --time -x >> $fname
   echo "====" >> $fname
done

# place in /root/checkdu/
# crontab entry (crontab -e as root): 12 8,20 * * *  /root/checkdu/checkdu.sh
# new line here -- to avoid crontab bug 

#to get only top level dir run on results:
#cat res |  sed -n '/====/{g;1!p;};h'
