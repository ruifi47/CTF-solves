from angr import *

BINARY_PATH = "./magic_number"
BASE_ADDR = 0x100000
WIN_ADDR = 0x100b11

''' specify addresses for angr to avoid (optional, but might help) '''
AVOID_ADDR = [0x100d61]

proj = Project(BINARY_PATH, load_options={'auto_load_libs': False}, main_opts={'base_addr': BASE_ADDR})

state = proj.factory.entry_state()
simgr = proj.factory.simgr(state)

simgr.explore(find=WIN_ADDR, avoid=AVOID_ADDR)

if simgr.found:
    simulations = simgr.found[0]
    print(simulations.posix.dumps(0))
else:
    print('failed')
#b'00000050000@\x04\x00\x0008747910916R\x82\x00\x00'
'''
$ nc 0.cloud.chals.io 32732
*************************************************************************
                       _                                _               
 _ __ ___   __ _  __ _(_) ___     _ __  _   _ _ __ ___ | |__   ___ _ __ 
| '_ ` _ \ / _` |/ _` | |/ __|   | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
| | | | | | (_| | (_| | | (__    | | | | |_| | | | | | | |_) |  __/ |   
|_| |_| |_|\__,_|\__, |_|\___|___|_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
                 |___/      |_____|                                     
**************************************************************************
Select your option: 
50000
50000
Alright Guess The Magic Number ... : 
8747910916
8747910916
guess is 2650405211509321 
flag{y444ay_u_f0und_t43_m4gic_nUmb3r}
'''
