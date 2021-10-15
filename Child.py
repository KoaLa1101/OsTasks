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
        print("It's Ch procces (pid = %d). Sleeping time = %d" % (os.getpid(), int(sys.argv[1])));
        time.sleep(int(sys.argv[1]));
        print("Ch process ended (pid  = %d)" % (os.getpid()));
        os._exit(random.randint(0,1));



