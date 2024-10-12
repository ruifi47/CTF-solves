#!/bin/bash

tshark -r list.pcap -Y http.request -T fields -e text        | \
  grep 'item: "command" = "echo'                             | \
  awk '{printf "%s\\n\n", $8}'                               | \
  sed 's/...$//'                                             | \
  cut -c 2-                                                  | \
  while read line; do echo "\n"; base64 -d <<< "$line"; done | \
  awk '{printf $6}'                                          | \
  cut -c 2-                                                  | \
  sed 's/.$//'                                               | \
  tr -d '\n'                                                 | \
  sed 's/\"//g'
#TFCCTF{b4s3_64_isnt_that_g00d}
