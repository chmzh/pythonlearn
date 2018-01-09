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
    class Proxy:
        def __call__(self, *args, **kwargs):
            return func(*args)
    return Proxy()


def decorator1(func):
    def onCall(*args):
        return func(*args)
        #return func(args)
    return onCall

class decorator3:
    def __init__(self,func):
        self.func = func

    def __call__(self, *args, **kwargs):
        self.func(*args)

@decorator3
def func2(a):
    print("fun2")

func2(1)

func3 = decorator1(func2)
func3(3)



def t(fun):
    def onCall(*args,**kwargs):
        result = fun(args)
        print("t(),",result)
    return onCall

def func(args): ...


func = t(func)

class Person:
    class Name:
        def __get__(self, instance, owner):
            return instance._name

        def __set__(self, instance, value):
            instance._name = value
        def __delete__(self,instance):
            del instance._name


    name = Name()
    def __init__(self,name):
        self._name = name
        pass
    @t
    def test(self):
        return 1
        pass


p = Person("test")
p2 = Person("test2")

p.name = "test1"

p.test()
print(p.name)

# del p.name
print(p2.name)

testFun = getattr(p,"test")
testFun()
