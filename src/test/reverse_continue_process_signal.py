from rrutil import *

send_gdb('handle SIGKILL stop')

send_gdb('c')
expect_gdb('SIGKILL')
send_gdb('reverse-continue')
expect_gdb('SIGTRAP')

ok()
