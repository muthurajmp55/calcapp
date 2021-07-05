from auk import Ackermann

import logging
import json
from logging import Formatter, FileHandler
from datetime import datetime
import sys

	
def ackerman():
    try:
        print("Started Auckerman....")
        n = 13#request.args.get("n")
        m = 3 #request.args.get("m")
        sys.setrecursionlimit(50000)
        start_time = datetime.now()
        ackermann = Ackermann()
        v=ackermann.run(int(m),int(n))
        print('ackermann(%d,%d): %d' % (m, n,v ))
        end_time = datetime.now()
        time_diff = end_time - start_time
        print('execution time: %s' % time_diff)
        print('Number of calls: %d' % ackermann.count)
        if ackermann.cache != {}:
            print('Cache Hit count: %d' % ackermann.cache_hit)
            print('Cache Miss count: %d' % ackermann.cache_miss)
            print('Cache Hit ratio: %.2f' % ((float)(ackermann.cache_hit) / ackermann.cache_miss * 100))
        d={'input':{"n":n,"m":m},'ouput':v,'Message':"Success"}
        print(d)
        
    except Exception as e:
        d={'input':{"n":n,"m":m},'Message':"Error due to {}".format(str(e))}
        print(d)

ackerman()


