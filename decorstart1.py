#class C:
#    @staticmethod # Синтаксис декорирования функций
#    def meth():
#        pass

# Эквивалент
#class C:
#    def meth():
#        pass
#    meth = staticmethod(meth)
class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances += 1
    @staticmethod
    def printNum():
        print(f"Num is: {Spam.numInstances}") # Количество созданных экземпляров

a = Spam()
b = Spam()
c = Spam()
a.printNum() # Работают вызовы из классов и экземпляров

class Methods():
    def imeth(self, x): # Нормальный метод экземпляра: передается self
        print([self, x])
    @staticmethod
    def smeth(x): # Статический метод: экземпляр не передается
        print([x])
    @classmethod
    def cmeth(cls, x): # Метод класса: получает класс, а не экземпляр
        print([cls, x])
    @property # Свойство: значение вычисляется при извлечении
    def name(self): 
        return "Bob" + self.__class__.__name__

obj = Methods()
obj.imeth(1)
obj.smeth(2)
obj.cmeth(3)
print(obj.name)

