#!/bin/sh

FILE='outputs/047.txt'
cut -f1,2 ${FILE} | sort | uniq -c | sort -r --numeric-sort
