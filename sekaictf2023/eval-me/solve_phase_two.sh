#!/usr/bin/bash

tshark -r capture.pcapng -T fields -e http.file_data http.request_number eq 1 | \
  cut -c 10-11                                                                | \
  tr -d "\n"                                                                  | \
  python3 -c 'key="s3k@1_v3ry_w0w"; enc=input(); flag = __import__("pwn").xor(key.encode(), bytes.fromhex(enc)); print(flag.decode("utf-8"))'
#SEKAI{3v4l_g0_8rrrr_8rrrrrrr_8rrrrrrrrrrr_!!!_8483}