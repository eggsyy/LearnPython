from types import MethodType


class Student(object):
    __slots__ = ('name', 'age', 'score')


class GraduatedStudent(Student):
    pass


def set_age(self, age):
    self.age = age
Student.set_age = MethodType(set_age, None, Student)

s = Student()
s.name = 'Michael'
print s.name

s.set_age(15)
print s.age

s.score = 99
print s.score

g = GraduatedStudent()
g.sex = 'male'
print g.sex
