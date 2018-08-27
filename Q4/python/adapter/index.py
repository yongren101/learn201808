class Dog(object):
    def call(self):
        print('汪汪!!')

class BlackDog(object):
    def specialCall(self):
        print('旺吾~~')

class Adpater(object):
    def __init__(self, adpatee):
        self.adpatee = adpatee

    def call(self):
        self.adpatee.specialCall()

if __name__ == '__main__':
    objects = []
    a = Dog()
    b = BlackDog()
    
    a.call()
    Adpater(b).call()