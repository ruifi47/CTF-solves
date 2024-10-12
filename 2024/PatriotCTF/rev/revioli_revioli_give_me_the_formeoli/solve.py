from angr import *

BINARY_PATH = "./revioli"
BASE_ADDR = 0x100000
WIN_ADDR = 0x1015dd

proj = Project(BINARY_PATH, load_options={'auto_load_libs': False}, main_opts={'base_addr': BASE_ADDR})

state = proj.factory.entry_state()
simgr = proj.factory.simgr(state)

simgr.explore(find=WIN_ADDR)

if simgr.found:
    simulations = simgr.found[0]
    print(simulations.posix.dumps(0))
else:
    print('failed')
#ITALY_01123581321345589144233377
