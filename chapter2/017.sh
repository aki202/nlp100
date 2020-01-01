#!/bin/sh

FILEPATH='hightemp.txt'

cut -f 1 ${FILEPATH} | sort | uniq
