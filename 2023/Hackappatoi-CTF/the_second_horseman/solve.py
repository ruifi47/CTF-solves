from angr import *

BINARY_PATH = "./thesecondhorseman"
BASE_ADDR = 0x100000
WIN_ADDR = 0x10135c

proj = Project(BINARY_PATH, load_options={'auto_load_libs': False}, main_opts={'base_addr': BASE_ADDR})

state = proj.factory.entry_state()
simgr = proj.factory.simgr(state)

simgr.explore(find=WIN_ADDR)

if simgr.found:
    simulations = simgr.found[0]
    print(simulations.posix.dumps(0))
else:
    print('failed')
#What_future_do_you_w/sh_for_our_children?
