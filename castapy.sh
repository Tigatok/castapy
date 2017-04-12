#!/bin/sh
`python /home/tmarshall/Projects/castapy/castapy.py`
difference=`diff new.txt old.txt | grep ">"`
echo "$difference"
if [ "$difference" != "" ]; then
  `mpg123 /home/tmarshall/Projects/castapy/ntfc.mp3`
fi
