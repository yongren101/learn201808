from abc import ABCMeta,abstractmethod


class BaseClass:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def getName(self):
        pass

class Class1(BaseClass):
    def getName(self):
        print('class1')

class Class2(BaseClass):
    def getName(self):
        print('class2')

class Class3(BaseClass):
    def getName(self):
        print('class3')

class Class4(BaseClass):
    def getName(self):
        print('class4')
   


