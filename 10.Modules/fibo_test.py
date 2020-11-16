#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()
    
def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

def main():
    a = fib(6)
    print('test fib(6)=', a)

print(__name__)
if __name__ == '__main__':
    print(__name__)
    main()

