from angr import *

BINARY_PATH = "./rev_boxcutter/cutter"
BASE_ADDR = 0x100000
WIN_ADDR = 0x1011f2

''' specify addresses for angr to avoid (optional, but might help) '''
#AVOID_ADDR = [0x<CHANGE_ME>, 0x<CHANGE_ME>]

proj = Project(BINARY_PATH, load_options={'auto_load_libs': False}, main_opts={'base_addr': BASE_ADDR})

state = proj.factory.entry_state()
simgr = proj.factory.simgr(state)

simgr.explore(find=WIN_ADDR)
#simgr.explore(find=WIN_ADDR, avoid=AVOID_ADDR)

if simgr.found:
    simulations = simgr.found[0]
    print(simulations.posix.dumps(0))
else:
    print('failed')
#HTB{tr4c1ng_th3_c4ll5}
