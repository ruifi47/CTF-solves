#!/bin/bash

tshark -r lost-at-sea.pcapng -Y 'http.request.method == "GET"' -T fields -e http.request.uri | \
	head -n 1 									     | \
	python3 -c 'print(__import__("urllib.parse").parse.unquote(input())[1:])'
#flag{b4by_5h4rk_do0_d0o_d00_d0o_d0o_1n_th3_s34}
