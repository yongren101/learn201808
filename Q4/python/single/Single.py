class single_instance:
    
    __instance = None
    def __init__(self,config = 0):
        self.__config = config
    
    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance
        
a = single_instance()
b = single_instance()
if a==b:
    print('同一个类实例')