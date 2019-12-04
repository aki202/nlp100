#!/bin/sh

FILE1='col1.txt'
FILE2='col2.txt'

paste -d '\t' ${FILE1} ${FILE2}
