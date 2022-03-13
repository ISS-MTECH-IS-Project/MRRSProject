from unicodedata import name


class Symptom():
    name:str
    weight:float
    penalty:float
    confirmed:bool
    def __init__(self, name):
        return

class Disease():
    name:str
    totalWeight:float
    weight:float
    confidence:float
    def __init__(self, name):
        return

class Treaatment():
    def __init__(self, id):
        return

class Question():
    def __init__(self, id):
        return

class Case():
    id:int
    satisfied:int
    concluded:bool
    def __init__(self, id):
        return



# SingletonMeta
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]