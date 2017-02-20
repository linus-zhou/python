#! /usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, age): #初始化方法
        self.name = name
        self.age = age

def print_age(std):
    print('name:%s age:%s' % (std.name, std.age))

student = Student('linus', 23)
#student.name = 'linus'

print_age(student)
print(student.name)

print('end!')