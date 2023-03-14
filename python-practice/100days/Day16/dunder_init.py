class MyClass:
    pass

o1 = MyClass()
o2 = MyClass()

type(o1)

type(o2)

o1.x = 10
o1.y = [10,20,30]

vars(o1) ##Returns a dictionary

o2.a = {1,2,3,4}
o2.b = {'a':1, 'b':2, 'c':3}

vars(o2)

class myClass:
    def __init__(self, x, y):
        print(f"now running MyClass.__init__, with {x=} and {y=}")
        self.x = y
        self.y = y

o1 = MyClass(10,20)

vars(o1)

o2 = MyClass({1,2,3,4,5}, {'a':1, 'b':2})

vars(o2)

