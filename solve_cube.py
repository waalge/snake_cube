#!/usr/bin/python3

from toy import * 

strip_lengths = ([2,3,4,3,2,3,2,3,2,3,2,3,5])
start = ([0,0,0,0,0,0,0,0,0,0,0,0])
strip_lengths = [ 3,4, 4,4, 2,4, 2,4, 2,2, 2,2, 2,2, 2,2, 2,3, 2,4, 3,3, 2,4, 2,3, 2,2, 2,2, 2,3, 2,2, 2,2, 4,2, 4 ]
#start = [0, 0, 0, 3, 0, 0, 1, 2, 0, 3, 3, 0, 0, 2, 0, 2, 3, 3, 2, 1, 2, 2, 1, 3, 0, 0, 2, 1, 1, 3, 2, 1, 2, 3, 0, 0, 2]
start = [0, 0, 3, 0, 0, 2, 3, 0, 2, 0, 0, 1, 1, 1, 2, 0, 3, 3, 2, 1, 2, 0, 1, 1, 2, 1, 1, 2, 2, 3, 1, 2, 1, 0, 3, 3, 3, 3, 0] 
start = [0, 0, 3, 1, ]
ii = 0 
T = Toy(strip_lengths) 
T.start(start)
print("Begin") 
local_min = len(T._strips) 
T.run(verbose = True) 
#while T.increment():
#    ii += 1
#    local_min = min([local_min, T._live_strip_n]) 
#    if (ii%100 == 0):
#        print("Run: ", ii,T._live_strip_n, local_min)
#        print("Run: ", T.progress())
#        local_min = len(T._strips) 
#    pass 
print("ii, ", ii) 
if T.fail(): 
    print("Yes Fail?", T.fail()) 

