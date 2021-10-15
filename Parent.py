#!/usr/bin/python3

import os
import sys
import random
import time

# Created by Akhmethanov Rinat (@koala1101). 11-902

if(len(sys.argv) < 2):
        print("Error! Please, check yours input args");
        os._exit(1);
else:
        N = int(sys.argv[1]);
        for i in  range (0, N):
                temp = os.fork();
                if (temp > 0):
                        if(i == 0):
                                print("The Pa process is pid=%d" % (os.getpid()));
                else:
                        os.execl("./Child.py", "Child.py", str(N));
                        break;
        for i in range (0, N):
                ans = os.wait();
                print("The Ch procces (pid=%d) was completed. Status: %d" % (ans[0], ans[1]));




