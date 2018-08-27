import classusers

class Factory:
    def __int__(self):
        pass
    
    def getObj(self, tag):
        obj = None
        if tag == 1:
            obj = classusers.Class1()
        elif tag == 2:
            obj = classusers.Class2()
        elif tag == 3:
            obj = classusers.Class3()
        elif tag == 4:
            obj = classusers.Class4()
        else:
            print('error')
        
        return obj
    
if __name__ == "__main__":
    f = Factory()
    obj = f.getObj(2)
    obj.getName()
