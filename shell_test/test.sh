#!/bin/bash

round=$1
rundate="$2"

echo "round: $round"
echo "rundate: $rundate"

case $round in
1) roundTime="1530"
    echo "roundTime: $roundTime"
    ;;
2) roundTime="1705"
    echo "roundTime: $roundTime"
    ;;
3)  roundTime="1900"
    echo "roundTime: $roundTime"
    ;;
4)  echo "EOD round"
    ;;
*)  echo "error round input"
    exit
    ;;
esac

if [${#rundate} != 8]
then
    exit
else
    echo "good rundate"
fi

echo "here"