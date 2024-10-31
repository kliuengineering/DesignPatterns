from abc import ABC, abstractmethod
import copy


class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class Car(Prototype):
    def __init__(self, make, model, color, feature=None):
        self.make = make
        self.model = model
        self.color = color
        self.features = feature if feature else []

    def add_feature(self, feature):
        self.features.append(feature)

    def clone(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        return f"Car(make={self.make}, model={self.model}, color={self.color}, features={self.features})"
    

class TestClas:
    def __str__(self):
        return f"This is a test class"
    

def main():
    prototype = Car("toyota", "camery", "white")
    variationA = prototype.clone()
    variationA.add_feature("luxury")
    variationB = prototype.clone()
    variationB.add_feature("sports")

    print(prototype)
    print(variationA)
    print(variationB)

if __name__ == "__main__":
    main()