#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class GPA:
  def __init__(self, name, score):
    self.name = name
    self.score = score

  def gpa_grade(data):
    if data.score >= 80:
        print(data.name + '\'GPA is A.')
    elif data.score >= 70:
        print(data.name + '\'GPA is B.')
    else: 
        print(data.name + '\'GPA is C.')
    
  def Order_of_books(book):
    if book.name[0] <= 'M':
        print(book.name, 'take book is 1st priority.')
    else:
        print(book.name, 'take book is 2nd priority.')

