#!/bin/sh

FILEPATH='hightemp.txt'

sort --numeric-sort --reverse -k 3 ${FILEPATH}
