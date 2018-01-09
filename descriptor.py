class Descriptor:
    def __get__(self, instance, owner):
        print(self,instance,owner,sep="\n")
    def __set__(self, instance, value):
        print(self, instance, value, sep="\n")
    def __delete__(self, instance): ... # Return nothing (None)


class Subject:
    descriptor = Descriptor()

sub = Subject()
sub.descriptor = 1