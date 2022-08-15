from socket import *
import time

startTime = time.time()

if __name__ == '__main__':
        target = open('/home/taha/homework/pythonpingoutput.txt','r')
        Lines = target.readlines()
        for line in Lines:

                t_IP = line.rstrip('\n')
                print ('Starting scan on host: ', t_IP) 
                for i in range(50, 500):
                        s = socket(AF_INET, SOCK_STREAM)
                        conn = s.connect_ex((t_IP, i))
                        if(conn == 0) :
                                print ('Port %d: OPEN' % (i,))
                        s.close()
print('Time taken:', time.time() - startTime)
