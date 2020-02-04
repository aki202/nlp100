#!/bin/sh

FILE='outputs/047.txt'
cut -f1 ${FILE} | sort | uniq -c | sort -r --numeric-sort
