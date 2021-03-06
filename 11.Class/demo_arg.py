#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
        
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
        
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
            
        elif opt in ("-i", "--ifile"):
            inputfile = arg
            
        elif opt in ("-o", "--ofile"):
            outputfile = arg
            
    print('輸入的文件為：', inputfile)
    print('輸出的文件為：', outputfile)

    
    
if __name__ == "__main__":
    main(sys.argv[1:])

