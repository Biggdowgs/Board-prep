import sys

import time

def slowprint(s):

	for c in s + '\n':
		sys.stdout.write(c)

		sys.stdout.flush()

		time.sleep(1./20)



def slowprint1(a):

    for c in a + '\n':

        sys.stdout.write(c)

        sys.stdout.flush()

        time.sleep(1./90)
        
def slowprint3(a):

    for c in a + '\n':

        sys.stdout.write(c)

        sys.stdout.flush()

        time.sleep(1./110)        
