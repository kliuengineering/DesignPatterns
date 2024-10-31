from abc import ABC, abstractmethod


class Implementor(ABC):
    @abstractmethod
    def operationImpl(self) -> str:
        pass


class ConcreteImplementorA(Implementor):
    def operationImpl(self) -> str:
        return "Concrete Implementor A..."
    

class ConcreteImplementorB(Implementor):
    def operationImpl(self) -> str:
        return "Concrete Implementor B..."
    

class Abstraction(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class RefinedAbstraction(Abstraction):
    def __init__(self, implementor: Implementor):
        self._implementor = implementor

    def operation(self):
        return f"Refined Abstraction {self._implementor.operationImpl()}"
    

def main():
    implementorA = ConcreteImplementorA()
    abstractionA = RefinedAbstraction(implementorA)
    print(abstractionA.operation())

    implementorB = ConcreteImplementorB()
    abstractionB = RefinedAbstraction(implementorB)
    print(abstractionB.operation())


if __name__ == "__main__":
    main()