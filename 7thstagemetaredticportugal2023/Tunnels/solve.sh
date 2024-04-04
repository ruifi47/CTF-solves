#!/usr/bin/bash

tshark -r traffic_capture.pcapng -Y icmp -T fields -e data | \
xxd -r -p                                                  | \
head -n 6                                                  | \
tail -n 1                                                  | \
awk '{printf $NF}'                                         | \
python3 -c 'print(input().split("\"")[2])'                 | \
base64 -d
#CTFUA{tr4ff1c_c4p_d0ne}
