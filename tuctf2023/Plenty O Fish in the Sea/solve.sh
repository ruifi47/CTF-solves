#!/usr/bin/bash

f="./lost_map.log"

awk '!seen[$0]++' $f |
tail -n 5            |
tr -d '\n'           |
python3 -c 'print(__import__("urllib.parse").parse.unquote(input()))'
#TUCTF{83h!Nd_7h3_W@73rF@11}