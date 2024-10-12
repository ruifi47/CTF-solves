#!/usr/bin/env python3
#import blackbox as blackbox
#import time
flag="pearl{j4il_time}"
whitelist=['a', 'c', 'h', 'q', 'r', 'w', '"', "'", '(', ')', '+', '-', '=', '?', '\\', '`', '|', ' ', '\t', '\n', '\r', '\x0b', '\x0c']
#def banner():
    #file=open("txt.txt","r").read()
    #print(file)
def main():
    #banner()
    cmd=input(">>> ")
    #time.sleep(2)
    #cmd=blackbox.normalise(cmd)
    if any(c in whitelist for c in cmd):
        try:
            print(eval(eval(cmd)))
        except:
            print("Sorry no valid output to show.")
    else:
        print("Your sentence has been increased by 2 years for attempted escape.")
main()