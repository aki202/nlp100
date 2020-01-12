#!/bin/sh

FILE='outputs/045.txt'
sort ${FILE} | uniq -c | sort -k 1 -n -r
