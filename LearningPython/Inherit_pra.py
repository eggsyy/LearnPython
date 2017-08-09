class Animal(object):
    def run(self):
        print 'Animal is running'


class Dog(Animal):
    def run(self):
        print 'Dog is running'


class Cat(Animal):
    def run(self):
        print 'Cat is running'

dog = Dog()
dog.run()

cat = Cat()
cat.run()


def run_twice(animal):
    animal.run()
    animal.run()


class Tortoise(Animal):
    def run(self):
        print 'Tortoise is running slowly'
run_twice(Tortoise())


class Husky(Dog):
    def run(self):
        print 'Husky is running'

a = Animal()
d = Dog()
h = Husky()
print isinstance(h, Dog)
print type(a)
print type(h)
print type(Animal())
