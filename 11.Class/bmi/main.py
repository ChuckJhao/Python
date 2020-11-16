#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from BMI import BMI

def main():
    David = BMI(68, 185)
    print('David\'s BMI is :', end ='')
    David.bmi_level()
    David.Taekwondo_level()
    print()
    
    Kevin = BMI(53, 172)
    print('Kevin\'s BMI is :', end ='')
    Kevin.bmi_level()
    Kevin.Taekwondo_level()
    print()

main()

