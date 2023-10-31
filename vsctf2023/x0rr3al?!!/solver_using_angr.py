from angr import *

proj = Project('./x0rr3al', load_options={'auto_load_libs': False}, main_opts={'base_addr': 0x00100000})

state = proj.factory.entry_state()
simgr = proj.factory.simgr(state)

win_addr = 0x00101b62

''' not needed for angr to find the flag '''
#avoid_addr = [0x001016ad, 0x0010156a]
#simgr.explore(find=win_addr, avoid=avoid_addr)

simgr.explore(find=win_addr)

if simgr.found:
    simulations = simgr.found[0]
    print(simulations.posix.dumps(0))
else:
    print('failed')
#vsctf{w34k_4nt1_d3bugg3rs_4r3_n0_m4tch_f0r_th3_31337}
