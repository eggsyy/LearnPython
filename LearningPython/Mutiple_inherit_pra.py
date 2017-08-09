class Animal(object):
    pass


class Runnable(object):
    def run(self):
        print ('Running.')


class Flyable(object):
    def fly(self):
        print ('Flying')


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Flyable):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass

dog = Dog()
dog.run()
bat = Bat()
bat.fly()
# bat.run()            'Bat' object has no attribute 'run'
