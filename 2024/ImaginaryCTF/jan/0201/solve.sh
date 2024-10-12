#!/usr/bin/bash

ssh-keygen -f id_rsa.pub -e -m pem > rsa_key.pub
openssl rsa -pubin -in rsa_key.pub -text -noout | \
tail -n 3                                       | \
head -n 2                                       | \
tail -n 1                                       | \
python3 -c "print('ictf{'+input().replace(':', '').replace('    ', '')[-16:]+'}')"
#ictf{1952c49f998e01fd}
