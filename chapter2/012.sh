#!/bin/sh

FILE='hightemp.txt'
echo 'Position = 1'
cut -f 1 ${FILE}
echo 'Position = 2'
cut -f 2 ${FILE}
