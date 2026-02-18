from abc import ABC, abstractmethod


class AbstractProductA(ABC):
    @abstractmethod
    def usefulFunctionA(self) -> str:
        pass


class AbstractProductB(ABC):
    @abstractmethod
    def usefulFunctionB(self) -> str:
        pass


class ConcreteProductA1(AbstractProductA):
    def usefulFunctionA(self) -> str:
        return "Italian Espresso"


class ConcreteProductB1(AbstractProductB):
    def usefulFunctionB(self) -> str:
        return "Italian Herbal Tea"


class ConcreteProductA2(AbstractProductA):
    def usefulFunctionA(self) -> str:
        return "British Filter Coffee"


class ConcreteProductB2(AbstractProductB):
    def usefulFunctionB(self) -> str:
        return "British Black Tea"



class AbstractFactory(ABC):
    @abstractmethod
    def createProductA(self) -> AbstractProductA:
        pass

    @abstractmethod
    def createProductB(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):
    def createProductA(self) -> AbstractProductA:
        return ConcreteProductA1()

    def createProductB(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    def createProductA(self) -> AbstractProductA:
        return ConcreteProductA2()

    def createProductB(self) -> AbstractProductB:
        return ConcreteProductB2()


class Client:
    def __init__(self, f: AbstractFactory):
        self.factory = f

    def someOperation(self):
        productA = self.factory.createProductA()
        productB = self.factory.createProductB()

        print(productA.usefulFunctionA())
        print(productB.usefulFunctionB())


print("Factory 1 (Italian drinks):")
client1 = Client(ConcreteFactory1())
client1.someOperation()

print("\nFactory 2 (British drinks):")
client2 = Client(ConcreteFactory2())
client2.someOperation()
