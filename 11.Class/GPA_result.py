#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from GPA_test import GPA

def main():
    classroom = [["John", 70], ["Xaiver", 85], ["Kevin", 50]]
    
    for c in classroom:
        student = GPA(c[0], c[1])
        student.gpa_grade()
        student.Order_of_books()
        print()
 

    
main()

