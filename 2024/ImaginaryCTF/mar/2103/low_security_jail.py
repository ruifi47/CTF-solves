#!/usr/local/bin/python
print("Welcome to the Low Security Jail!")
def blacklist(cmd):
    if cmd.isascii() == False:
        return False
    bad_cmds = ['"',"'","print","_",".","import","os","lambda", "system","breakpoint","(",")","@","getattr","setattr","globals","builtins","help","input","0","1","2","3","4","5","6","7","8","9","/","compile","eval","exec","open","read","cmd","isascii"]
    for i in bad_cmds:
        if i in cmd:
            return False
    return True
while True:
    inp = input("Enter command to execute: ")
    if blacklist(inp):
        exec(inp)
    else:
        print("Blacklisted command found! Exiting!")
        exit(0)