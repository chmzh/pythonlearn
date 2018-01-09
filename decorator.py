class Person:
    def __init__(self,target):
        self.wraped = target

    def __getattr__(self, item):
        return getattr(self.wraped,item)
    @staticmethod
    def t():
        print("test")
person = Person([1,2,3])

person.append(4)
Person.t()
print(person.wraped)


def decorator(func):
    def onCall(*args):
        return func(args)
    return onCall


@decorator
def func2(a):
    print("fun2")

func2()

decorator(func2)()