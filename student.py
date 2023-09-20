class Student:
    _schoolName = 'xy school'
    def __init__(self, name, age):
        self._name = name
        self._age = age
    def display(self):
        print('this is private method.')

