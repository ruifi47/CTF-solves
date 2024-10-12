#!/bin/bash

tshark -r frames.pcap -T fields -e wlan.ssid | \
  xxd -r -p                                  | \
  base64 -d                                  | \
  grep 'bctf{'                               | \
  head -n 1
#bctf{tw0_po1nt_4_g33_c0ng3s7i0n}
