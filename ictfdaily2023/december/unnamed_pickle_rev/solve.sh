#!/usr/bin/bash

python3 -c '__import__("pickletools").dis(open("./out.pickle", "rb").read())' | \
grep 1337 -B 1 								      | \
grep -E '(STRING|PUT)' 							      | \
awk '{print $4}' 							      | \
head -n 140 								      | \
paste -s -d' \n' 							      | \
sort -n -k2 								      | \
awk '{print $1}' 							      | \
sed "s/'//g" 								      | \
tr -d "\n"
#ictf{so_i_went_to_the_car_DILLership_but_all_they_had_were_caDILLacs}
