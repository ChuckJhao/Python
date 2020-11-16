#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Python get command line option, using getopt module
import sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"EAWlbp")
    except getopt.GetoptError:
        print ('test.py -[EAW][lbp]')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt == '-E':
             print('-E')
        elif opt == '-A':
             print('-A')

                
if __name__ == "__main__":
    main(sys.argv[1:])

