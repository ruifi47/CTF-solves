#!/bin/bash

awk '!seen[$0]++' lost_map.log | \
tail -n 5            	       | \
tr -d '\n'           	       | \
python3 -c 'print(__import__("urllib.parse").parse.unquote(input()))'
#TUCTF{83h!Nd_7h3_W@73rF@11}
