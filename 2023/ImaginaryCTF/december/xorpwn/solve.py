import gdb
# gdb -x solve.py ./chall
breakpoint_address = 0x401b86
gdb.execute(f"b *{breakpoint_address}")
gdb.execute("r")
out = gdb.execute("x/50s $rsp", to_string=True)
print(__import__("re").findall("ictf{.*?}", out)[0])
gdb.execute("q")
#ictf{xor_is_awesome}
