from abc import ABC , abstractmethod

class Model(ABC):
    @classmethod
    @property
    @abstractmethod
    def store(cls):
        raise NotImplementedError("'store' attr is required for Model!")
    
    def __new__(cls , *args , **kwargs) :
        instance =  super().__new__(cls)
        cls.store.append(instance)
        return instance
    
        