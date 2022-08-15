import subprocess

file1 = open('/home/taha/homework/pythonpingoutput.txt','w+')  
for ping in range(1,254):
    address = "192.168.1." + str(ping)
    res = subprocess.call(['ping', '-c', '3', address])
    if res == 0:
        print( "ping to", address, "OK")
        file1.write(address+"\n")

    elif res == 2:
        print("no response from", address)
    else:
        print("ping to", address, "failed!")
