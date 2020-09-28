import time
t=time.process_time()
n=100000000
value=10**1000+1
for i in range(n):
    value2=value*value
elapsed_time=time.process_time()-t
print("N=",n,"value bits=",value.bit_length(),"time=",elapsed_time)

#value=10, time=9.046875
#value=10**10+1, time=11.40625
#value=10**100+1, time=23.09375
#value=10**1000+1, time=640.17836