#!/usr/bin/bash

tshark -r lost-at-sea.pcapng -Y 'http.request.method == "GET"' -T fields -e http.request.uri | head -n 1 | \
python3 -c 'print(__import__("urllib.parse").parse.unquote(input())[1:])'
