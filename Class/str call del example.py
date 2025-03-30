class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_person(self):
        print("my name is {0}, my age is {1}".format(self.name, self.age))

    def __str__(self):
        return ("my name is {0}, my age is {1}".format(self.name, self.age))

    def __call__(self, *args, **kwargs):
        print("something important")

    def __del__(self):
        print("we are done")
p1 = Person("Eli", 35)
p1.get_person()
print(p1)
p1()