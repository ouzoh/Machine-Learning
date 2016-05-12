#!/bin/python

import sys

def mapper():
    # read standard input line by line
    for line in sys.stdin:
        # strip off extra whitespace, split on tab and put the data in an array
        print line
        data = line.strip().split("\t")
        print data

        #print data
        # This is the place you need to do some defensive programming
        # what if there are not exactly 6 fields in that line?
        # YOUR CODE HERE
        #print data
        if len(data) == 10:
            print "yes"
            #if len(row) == 5  & float(4): ##and float(cost) and string(store): ## while (len(data) == 6):
            remote_host, remote_user, remote_logname, time_received, time_GMT, request1, request2, request3,\
            status, byteSize = data
            #if float(cost) and str(store):
            print "{0}\t{1}".format(remote_host, request2)


test_text = """10.223.157.186\t-\t-\t[15/Jul/2009:15:50:35\t-0700]\t"GET\t/assets/js/lowpro.js\tHTTP/1.1"\t200\t10469"""

# This function allows you to test the mapper with the provided test string
def main():
	import StringIO
	sys.stdin = StringIO.StringIO(test_text)
	mapper()
	sys.stdin = sys.__stdin__

main()
