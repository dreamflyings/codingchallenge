#!/bin/bash 

#
# ### Problem ###
# https://leetcode.com/problems/tenth-line/description/
#

i=1

while read -r l; do
  if [ $i == 10 ]; then
    echo $l
    exit 0
  fi
  i=$(expr $i + 1)
done < file.txt

exit 1
