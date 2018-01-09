class Super:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        print('fetch...')
        return self.__name
    @name.setter
    def name(self, value):
        print('change...')
        self.__name = value
    @name.deleter
    def name(self):
        print('remove...')
        del self.__name

    # name = property(getName, setName, delName, "name property docs")


class Person(Super):
    pass


bob = Person('Bob Smith')  # bob has a managed attribute
print(bob.name)  # Runs getName
bob.name = 'Robert Smith'  # Runs setName
del bob.name  # Runs delName
print('-' * 20)
sue = Person('Sue Jones')  # sue inherits property too
print(sue.name)
print(Person.name.__doc__)  # Or help(Person.name)

#
# class PropSquare:
#
#
#     def __init__(self, start):
#         self.value = start
#
#
#     def getX(self):  # On attr fetch
#         return self.value ** 2
#
#     def setX(self, value):  # On attr assign
#         self.value = value
#     X = property(getX, setX)  # No delete or docs
# P = PropSquare(3)  # Two instances of class with property
# Q = PropSquare(32)  # Each has different state information
# print(P.X)  # 3 ** 2
# P.X = 4
# print(P.X)  # 4 ** 2
# print(Q.X)  # 32 ** 2 (1024)
